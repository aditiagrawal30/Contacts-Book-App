# Contacts-Book-App

Contacts Book App is an application based project, designed for people to store the contact details. Rather than going through the pages of their diaries to search the person information, he/she can simply use this software to view any of his/her stored contacts. A user can also add or update or delete the contact information according to his need. 

#Libraries and Tools:
Python 2.7
WxPython
SQLAlchemy
ObjectListView
SQLite

The implementation of the system is based on MVC (Model-View-Controller) architecture using Python language, where WxPython is for GUI, SQLAlchemy for ORM and SQL Toolkit, and SQLite as database.

Model(back.py): Contains SQAlchemy, which is famous for its ORM, using which classes can be mapped to the database, thereby allowing the model and database schema to develop in a cleanly separated way from the beginning.

View (main.py): In this module, a few custom items like addModRecord,commonDlgs and logic are imported. The addModRecord  is a dialog that is used to add a record and edit one as well. The commonDlgsis just used for creating message dialogs. The logic module is where all the SQLAlchemy code is executed.

Controller(logic.py): Acts like glue which holds the model and the view together. It uses the model for queries and for adding, editing and deleting the contact.

