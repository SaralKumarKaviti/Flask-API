from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


Base=declarative_base()

class Register(Base):
	__tablename__='register'

	id = Column(Integer,primary_key=True)
	name=Column(String(100))
	surname=Column(String(100))
	email=Column(String(50))
	className=Column(String(30))
	mobile=Column(String(20))
	fatherName = Column(String(50))
	motherName = Column(String(50))
	gender = Column(String(10))
	



engine=create_engine('sqlite:///student.db')
Base.metadata.create_all(engine)
print("Database is Created!!!")