from sqlalchemy import PrimaryKeyConstraint, Column, String, Integer, ForeignKey;
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    
    def __repr__(self):
        return f"ID: {self.id}, " \
        + f"Name: {self.name}"
    
# class Task(Base):



#     id = Column(Integer())
#     name = Column(String())

