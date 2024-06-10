from sqlalchemy import Table, Column, Integer, ForeignKey
from collabinnovate import db

group_membership = Table('group_membership', db.Model.metadata,
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)