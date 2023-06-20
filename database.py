from sqlalchemy import create_engine, text

db_connect = "mysql+pymysql://iierkby7ym1jeib5rqqb:pscale_pw_PrGPJcxAGPoUzdxDBQ3gkZ2iH4uEDDMUgGig9qjJPxX@aws.connect.psdb.cloud/websiteflask?charset=utf8mb4"
engine = create_engine(db_connect,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_fromdb():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    return_all = result.all()
    jobs = []
    for row in return_all:
      # Thay 'column1', 'column2' bằng tên các cột thực tế
      jobs.append(row)
    return jobs
