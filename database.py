from sqlalchemy import create_engine, text
import os
db_connect = os.environ['DB_CONNECT']

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
