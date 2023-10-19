#will contain all database configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# after the double slash url contains user:password@host/database_name
db_url = 'postgresql://postgres:root@localhost/master'

engine=create_engine(db_url)

sessionLocal = sessionmaker(bind=engine)

base = declarative_base()