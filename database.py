#will contain all database configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# dialect[+driver]://user:password@host/database_name
#driver the name of a DBAPI, such as psycopg2, pyodbc, cx_oracle, etc. Alternatively, the URL can be an instance of ~sqlalchemy.engine.url.URL
db_url = 'postgresql://postgres:root@localhost:5432/master'

engine=create_engine(db_url)

sessionLocal = sessionmaker(bind=engine)

base = declarative_base()