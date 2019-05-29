from sqlalchemy import Column, Integer, String, DateTime
from flask import jsonify

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, index=True)

    def __init__(self, email=None):
        self.email = email

    def assign_properties(self, **kwargs):
        for prop, val in kwargs.items():
            if hasattr(self, prop):
                setattr(self, str(prop), val)

    def json_rep(self):
        data = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at
        }
        return data

    def __repr__(self):
        return "<User {}>".format(self.first_name)
