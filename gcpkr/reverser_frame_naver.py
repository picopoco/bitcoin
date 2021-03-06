import pandas as pd
import pandas as pd

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]

# 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

# 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다.
code_df = code_df[['회사명', '종목코드']]

# 한글로된 컬럼명을 영어로 바꿔준다.
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
code_df.head()
print (code_df.head())


# 종목 이름을 입력하면 종목에 해당하는 코드를 불러와
# 네이버 금융(http://finance.naver.com)에 넣어줌
def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)

    print("요청 URL = {}".format(url))
    return url


# 신라젠의 일자데이터 url 가져오기
item_name = '신라젠'
url = get_url(item_name, code_df)

# 일자 데이터를 담을 df라는 DataFrame 정의
df = pd.DataFrame()

# 1페이지에서 20페이지의 데이터만 가져오기
for page in range(1, 21):
    pg_url = '{url}&page={page}'.format(url=url, page=page)
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

# df.dropna()를 이용해 결측값 있는 행 제거
df = df.dropna()

# 상위 5개 데이터 확인하기
print (df.head())


def get_stochastic(df, n=15, m=5, t=3):
    # 입력받은 값이 dataframe이라는 것을 정의해줌
    df = pd.DataFrame(df)

    # n일중 최고가
    ndays_high = df.high.rolling(window=n, min_periods=1).max()
    # n일중 최저가
    ndays_low = df.low.rolling(window=n, min_periods=1).min()

    # Fast%K 계산
    kdj_k = ((df.close - ndays_low) / (ndays_high - ndays_low)) * 100
    # Fast%D (=Slow%K) 계산
    kdj_d = kdj_k.ewm(span=m).mean()
    # Slow%D 계산
    kdj_j = kdj_d.ewm(span=t).mean()

    # dataframe에 컬럼 추가
    df = df.assign(kdj_k=kdj_k, kdj_d=kdj_d, kdj_j=kdj_j).dropna()

    return df

# df = get_stochastic(df)
# print (df.head())

import plotly.offline as offline
import plotly.graph_objs as go
from plotly import tools

# jupyter notebook 에서 출력
offline.init_notebook_mode(connected=True)

kdj_k = go.Scatter(
    x=df.date,
    y=df['kdj_k'],
    name="Fast%K")

kdj_d = go.Scatter(
    x=df.date,
    y=df['kdj_d'],
    name="Fast%D")

kdj_d2 = go.Scatter(
    x=df.date,
    y=df['kdj_d'],
    name="Slow%K")

kdj_j = go.Scatter(
    x=df.date,
    y=df['kdj_j'],
    name="Slow%D")

trade_volume = go.Bar(
    x=df.date,
    y=df['volume'],
    name="volume")

# data = [kdj_k, kdj_d]
data1 = [kdj_d2, kdj_j]
data2 = [trade_volume]

# data = [celltrion]
# layout = go.Layout(yaxis=dict(
#         autotick=False,
#         ticks='outside',
#         tick0=0,
#         dtick=10,
#         ticklen=8,
#         tickwidth=4,
#         tickcolor='#000'
#     ))

fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)

for trace in data1:
    fig.append_trace(trace, 1, 1)

for trace in data2:
    fig.append_trace(trace, 2, 1)
# fig = go.Figure(data=data, layout=layout)

offline.iplot(fig)
