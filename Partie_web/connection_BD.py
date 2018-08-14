# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:33:28 2018

@author: nisha
"""

import mysql.connector
from mysql.connector import errorcode


def connection_BD():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='bisneu95', 
                                      host='localhost', 
                                      database='ai4food')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return(cnx)
    
