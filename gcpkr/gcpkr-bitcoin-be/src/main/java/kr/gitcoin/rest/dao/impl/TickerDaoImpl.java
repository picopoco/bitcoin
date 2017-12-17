package kr.gitcoin.rest.dao.impl;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.mybatis.spring.support.SqlSessionDaoSupport;

import kr.gitcoin.rest.GitcoinConstants;
import kr.gitcoin.rest.dao.TickerDao;
import kr.gitcoin.rest.model.GitcoinCriteria;
import kr.gitcoin.rest.model.TickerVo;

public class TickerDaoImpl extends SqlSessionDaoSupport
    implements TickerDao, GitcoinConstants {

  private static final String ns = "kr.gitcoin.rest.Ticker";
  private static Map<String, String> sqls = null;

  public TickerDaoImpl() {
    if (sqls == null) {
      sqls = new HashMap<String, String>();
      for (String sql : SQLS) {
        sqls.put(sql, ns + "." + sql);
      }
    }
  }

  public long count(GitcoinCriteria criteria) {
    return getSqlSession().selectOne(sqls.get(SQL_COUNT), criteria);
  }

  public void create(TickerVo vo) {
    // TODO Auto-generated method stub
  }

  public void delete(long ts) {
    // TODO Auto-generated method stub
  }

  public TickerVo get(long ts) {
    return getSqlSession().selectOne(sqls.get(SQL_GET), ts);
  }

  public List<TickerVo> list(GitcoinCriteria criteria) {
    return getSqlSession().selectList(sqls.get(SQL_LIST), criteria);
  }

  public void update(long ts, TickerVo vo) {
    // TODO Auto-generated method stub
  }

}
