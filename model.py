from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime,Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Users(Base):
    __tablename__='users'

    id=Column(UUID(as_uuid=True),primary_key=True,nullable=False)
    slug=Column(String)
    email=Column(String)
    phone=Column(String)
    role=Column(Enum('admin','customer','staff',name='user_roles'))
    name=Column(String)
    avatar=Column(String)
    locale=Column(String)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
    last_login=Column(DateTime)
    email_validated=Column(Boolean)
    phone_validated=Column(Boolean)
    bio=Column(String)
    company=Column(String)
    
