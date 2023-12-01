import panel as pn
import param as pm
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from auto_crud_param.crud import CRUDListParameter, CRUDMultiSelect
from auto_crud_param.orm import parameterized_to_model

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


class MyCRUDApp(pm.Parameterized):
    # Example usage
    crud_param = CRUDListParameter()

    def __init__(self):
        super().__init__()
        self.crud_param.items = ['Item 1', 'Item 2', 'Item 3']  # Set initial items here
        self.crud_widget = CRUDMultiSelect(self.crud_param)

    def panel(self):
        return pn.Row(self.crud_widget.panel())


# Create and show the app
app = MyCRUDApp()
app.panel().servable()
