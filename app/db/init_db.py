from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.models import Base
import sys
sys.path.append(".")
from app.core.config import DATABASE_URL
from app.models import Base

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created.")
