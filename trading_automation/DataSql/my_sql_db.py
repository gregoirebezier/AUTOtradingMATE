#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

def my_sql_serv():
    mydb = mysql.connector.connect(
        host="CompleteThisLine",
        user="CompleteThisLine",
        password="CompleteThisLine",
        database="crypto_client"
    )
    mycursor = mydb.cursor()

    #------DELETE THE TABLE-----#
    #try:
    #    mycursor.execute("DROP TABLE clients")
    #except:
    #    pass

    #----CREATE A DATABASE-----#
    #mycursor.execute("CREATE DATABASE crypto_client") #create database named crypto_client
    #mycursor.execute("SHOW DATABASES")


    #-----CREATE A TABLE------#
    #mycursor.execute("CREATE TABLE clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), api_key VARCHAR(255), api_secret VARCHAR(255), email VARCHAR(255))")
    #mycursor.execute("SHOW TABLES") #check the table I created


    #----LINE TO UNCOMMENT TO ADD NEWCLIENT-----#
    #sql = "INSERT INTO clients (name, api_key, api_secret, email) VALUES (%s, %s, %s, %s)"
    #NewClient = ("CompleteThisLineYOURNAME", "CompleteThisLineAPI_KEY", "CompleteThisLineAPI_SECRET", "CompleteThisLineMAIL@gmail.com")
    #mycursor.execute(sql, NewClient)


    #-----DELETE A SPECIFIC LINE TO TABLE-----#
    #mycursor.execute("DELETE FROM clients WHERE name='Blabla'")


    #-----PRINT ALL THE TABLE-----#
    #mycursor.execute("SELECT * FROM clients")
    #toto = mycursor.fetchall()
    #for element in toto:
    #    print(element)


def main():
    my_sql_serv()
main()