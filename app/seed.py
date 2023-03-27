from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, User)

if __name__ == '__main__':
    engine = create_engine('sqlite:///mydb.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    # session.query().delete()

    faker = Faker()