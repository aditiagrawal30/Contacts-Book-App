
from back import Person, CBook_Olv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#----------------------------------------------------------------------
def addRecord(data):
  
    person = Person()
    person.mail = data["person"]["mail"]
    person.contact_number = data["person"]["contact_number"]
    person.first_name = data["person"]["first_name"]
    person.last_name = data["person"]["last_name"]
  
    
    # connect to session and commit data to database
    session = connectToDatabase()
    session.add(person)
    session.commit()
    session.close()
    
#----------------------------------------------------------------------
def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    engine = create_engine("sqlite:///ContactBook.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

#----------------------------------------------------------------------
def convertResults(results):
    """
    Convert results to CBook_Olv objects
    """
    print
    details = []            
    for record in results:
        person = CBook_Olv(record.first_name, record.last_name, record.mail,
                 record.contact_number)                    
        details.append(person)
    return details

#----------------------------------------------------------------------
def deleteRecord(val):
    """
    Delete a record from the database
    """
    session = connectToDatabase()
    record = session.query(Person).filter_by(mail=val).one()
    session.delete(record)
    session.commit()
    session.close()
    
#----------------------------------------------------------------------
def editRecord(val, row):
    """
    Edit a record
    """
    session = connectToDatabase()
    record = session.query(Person).filter_by(mail=val).one()
    print
    record.first_name = row["first_name"]
    record.last_name = row["last_name"]
    record.mail = row["mail"]
    record.contact_number = row["contact_number"]
    session.add(record)
    session.commit()
    session.close()

#----------------------------------------------------------------------
def getAllRecords():
    """
    Get all records and return them
    """
    session = connectToDatabase()
    result = session.query(Person).all()
    details = convertResults(result)
    session.close()
    return details

#----------------------------------------------------------------------
def searchRecords(filterChoice, keyword):
    """
    Searches the database based on the filter chosen and the keyword
    given by the user
    """
    session = connectToDatabase()
  
    if filterChoice == "first_name":
        qry = session.query(Person)
        result = qry.filter(Person.first_name.contains('%s' % keyword)).all()
    elif filterChoice == "mail":
        qry = session.query(Person)
        result = qry.filter(Person.mail.contains('%s' % keyword)).all()
    else:
        qry = session.query(Person)
        result = qry.filter(Person.contact_number.contains('%s' % keyword)).all()    
    details = convertResults(result)
    session.close()
    return details
