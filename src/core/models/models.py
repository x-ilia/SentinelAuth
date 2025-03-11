from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

# from src.core.models.base import Base

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization = relationship('Organization', back_populates='users')
    groups = relationship('Group', secondary='user_groups', back_populates='users')
    projects = relationship('Project', secondary='user_projects', back_populates='users')
    def __repr__(self):
        return '<Name %s\n email %s>'.format(self.first_name, self.email)


class Organization(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    name = Column(String, nullable=False)
    users = relationship('User', back_populates='organization')
    groups = relationship('Group', back_populates='organization')
    projects = relationship('Project', back_populates='organization')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    name = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization = relationship('Organization', back_populates='groups')
    users = relationship('User', secondary='user_groups', back_populates='groups')
    projects = relationship('Project', secondary='group_projects', back_populates='groups')


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    name = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization = relationship('Organization', back_populates='projects')
    users = relationship('User', secondary='user_projects', back_populates='projects')
    groups = relationship('Group', secondary='group_projects', back_populates='projects')

class UserGroup(Base):
    __tablename__ = 'usergroups'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)

class UserProject(Base):
    __tablename__ = 'user_projects'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)

class GroupProject(Base):
    __tablename__ = 'group_projects'
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
