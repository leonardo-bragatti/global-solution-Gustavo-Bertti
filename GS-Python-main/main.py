from menu import menu
from database.__init__ import create_tables
from sqlalchemy import inspect

create_tables()
menu()