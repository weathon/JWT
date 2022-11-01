from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
import bcrypt
from sqlalchemy.orm import Session
try:
    with open("/home/wg25r/PSDSQL","r") as f: 
        SQLPWD = f.read()
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://wg25r:"+SQLPWD+"@localhost/COSC310"
except:
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:" # Easiler for testing



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "users_2" 

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True)
    passwordSalt = Column(String(65), index=True)
Base.metadata.create_all(engine)

# generating the salt
# salt = bcrypt.gensalt()
  
# # Hashing the password
# hash = bcrypt.hashpw("123456".encode('utf-8'), salt)
# print(salt, hash)
# print(bcrypt.checkpw("123456".encode('utf-8'),hash))

def signup(username, password):
    with Session(engine) as session:
        u = session.query(User).filter(User.username == username)
        if len(list(u)) != 0:
            return -1
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        db_user = User(username = username, passwordSalt=hash)
        session.add(db_user)
        session.commit()

def login(username, password):
    with Session(engine) as session:
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm huiyi django
        u = session.query(User).filter(User.username == username)
    return bcrypt.checkpw(password.encode('utf-8'),list(u)[0].passwordSalt.encode("utf-8"))
# signup("test"," ")

# print(login("test"," "))
