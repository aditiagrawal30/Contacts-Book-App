
from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Unicode
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///ContactBook.db", echo=True)
DeclarativeBase = declarative_base(engine)
metadata = DeclarativeBase.metadata

########################################################################
class CBook_Olv(object):
    """
    CBook model for ObjectListView
    """

    #----------------------------------------------------------------------
    def __init__(self,first_name,  last_name, mail, contact_number):
        self.first_name = first_name
	self.last_name = last_name
        self.mail = mail  
        self.contact_number = contact_number

########################################################################
class Person(DeclarativeBase):
    """"""
    __tablename__ = "contact_details"
    
    first_name = Column("first_name", String(50))
    last_name = Column("last_name", String(50))
    mail = Column("mail", Unicode, primary_key=True)
    contact_number = Column("contact_number",Unicode(10))
        
metadata.create_all()

