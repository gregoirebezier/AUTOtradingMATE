#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

def my_sql_serv():

    #----CREATE A DATABASE NAMED "crypto_client" -----#
    #mydb = mysql.connector.connect(
    #    host="CompleteThisLine",
    #    user="CompleteThisLine",
    #    password="CompleteThisLine",
    #)
    #mycursor = mydb.cursor()
    #mycursor.execute("CREATE DATABASE crypto_client")
    #mycursor.execute("SHOW DATABASES")

    #-----CONNECTION TO DATABASE "crypto_client" -----#
    #mydb = mysql.connector.connect(
    #    host="CompleteThisLine",
    #    user="CompleteThisLine",
    #    password="CompleteThisLine",
    #    database="crypto_client"
    #)
    mycursor = mydb.cursor()

    #------DELETE THE TABLE-----#
    #try:
    #    mycursor.execute("DROP TABLE clients")
    #except:
    #    pass


    #-----CREATE A TABLE------#
    #mycursor.execute("CREATE TABLE clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, api_key VARCHAR(255) NOT NULL, api_secret VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, MoneyToTrade INT UNSIGNED)")
    #mycursor.execute("SHOW TABLES") #check the table I created


    #----LINE TO UNCOMMENT TO ADD NEWCLIENT-----#
    #sql = "INSERT INTO clients (name, api_key, api_secret, email, MoneyToTrade) VALUES (%s, %s, %s, %s, %s)"
    #NewClient = ("CompleteThisLineYOURNAME", "CompleteThisLineAPI_KEY", "CompleteThisLineAPI_SECRET", "CompleteThisLineMAIL@gmail.com", "CompleteThisLineMoneyTotalToTrade")
    #mycursor.execute(sql, NewClient)
    #mydb.commit()

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