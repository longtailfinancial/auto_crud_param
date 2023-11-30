import param as pm
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from auto_crud_param import parameterized_to_model

Base = declarative_base()


# Example usage
class A(pm.Parameterized):
    name = pm.String(default='Item A')
    value = pm.Number(default=0)


AModel = parameterized_to_model(A, Base)

# Set up the database (for example, using SQLite)
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
