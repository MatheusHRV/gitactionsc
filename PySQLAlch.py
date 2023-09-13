# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:53:44 2023

@author: VIM1CA
"""

import pyodbc
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def insert_data_into_MySQLdatabase(connection_string, 
                                   person_id, 
                                   last_name, 
                                   first_name, 
                                   age):
    
    connection_string = connection_string
    print(connection_string)
    print(person_id)
    print(last_name)
    print(first_name)
    print(age)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base = declarative_base()
    
    class Persons(Base):
        __tablename__ = 'Persons'
        Personid = Column(Integer, primary_key=True)
        LastName = Column(String(255))
        FirstName = Column(String(255))
        Age = Column(Integer)
        
    new_person = Persons(
        Personid=person_id,
        LastName=last_name,
        FirstName=first_name,
        Age=age,
    )
    
    session.add(new_person)
    
    session.commit()
    
    session.close()


insert_data_into_MySQLdatabase(
        connection_string = (
            "DSN=SampleDNS;"
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=CA-C-002AG\SQLEXPRESS;"
            "Database=SampleDB;"
            "Trusted_Connection=yes;"
        ),
        person_id = '6',
        last_name = 'Teste', 
        first_name = 'Silvio', 
        age = '15',
    )

