in:
  type: gcs
  bucket: gcpkr-bitcoin-keras
  path_prefix: preprocess/2017
  auth_method: private_key #default
  service_account_email: gcpkr-bitcoin@gcpkr-bitcoin.iam.gserviceaccount.com
  p12_keyfile: /home/Tora/embulk-example/gcpkr-bitcoin-fc5a651b02f6.p12
  application_name: Tora
  parser:
    charset: UTF-8
    newline: LF
    type: csv
    delimiter: ','
    quote: '"'
    escape: '"'
    null_string: 'NULL'
    trim_if_not_quoted: false
    skip_header_lines: 1
    allow_extra_columns: false
    allow_optional_columns: false
    columns:
    - {name: traded_at, type: long}
    - {name: open, type: double}
    - {name: high, type: double}
    - {name: low, type: double}
    - {name: close, type: double}
out:
   type: bigquery
   mode: append
   auth_method: private_key
   service_account_email: gcpkr-bitcoin@gcpkr-bitcoin.iam.gserviceaccount.com    # 구글 클라우드 서비스 계정 ID
   p12_keyfile: /home/Tora/embulk-example/gcpkr-bitcoin-fc5a651b02f6.p12   # 구글 클라우드 비공개 다운받은 키 경로
   project: gcpkr-bitcoin   # 구글 클라우드 프로젝트명
   dataset: test_de   # 빅쿼리 데이터셋
   table: preprocess   # 빅쿼리 테이블명
   auto_create_table: true   # 스키마를 안만들어져 있으면 자동으로 만들어주게끔 설정
   gcs_bucket: gcpkr-bitcoin-bigquery   # Google Cloud Storage 버킷 이름
   auto_create_gcs_bucket: true   # 만약 Google Cloud Storage 버킷이 없으면 생성
   ignore_unknown_values: true   # 알 수 없는 값이 들어왔을때 무시
   allow_quoted_newlines: true   # quote가 들어올때 새로운 라인 생성
   auto_create_dataset: true   # 빅쿼리에 미리 데이터셋이 만들어져 있지 않으면 자동으로 생성