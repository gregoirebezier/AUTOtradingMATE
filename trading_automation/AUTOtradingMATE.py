#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from email.message import EmailMessage
import smtplib
import mysql.connector

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

class VarProg:
    EmailSendingTo = []
    money_trade = []
    api_secret = []
    money_buy = []
    api_key = []
    erase_sell = 0
    erase_buy = 0

def send_mail(var):
    EMAIL_ADDRESS = "CompleteThisLine@gmail.com"
    EMAIL_PASSWORD = "CompleteThisLine"
    try:
        report_check()
    except:
        pass
    with open('files/statistic.txt', 'r') as file:
        data = file.read()
    file.close()
    for people in var.EmailSendingTo:
        msg = EmailMessage()
        msg['Subject'] = "Rapport de la semaine" #subject of the email
        msg['From'] = EMAIL_ADDRESS #your email adress you want to send with 
        msg['To'] = people #email of the people you will send the message
        msg.set_content(data) #content of the mail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    file1 = open("files/statistic.txt","r+")
    file1.truncate(0)
    file1.close()

#this function check then benefice of the differents trade in the week
def report_check():
    tab = []
    out = str(check_output(["bash", "BashScript/get_benefice.sh"]))
    out = out.replace("b'", "")
    out = out.replace("'", "")
    tab = out.split("\\n")
    put_benef(tab)

#this function write the benefice to the statistic.txt before sending the message
def put_benef(tab):
    with open("files/statistic.txt", "r") as reading:
        lines = reading.readlines()
    with open("files/statistic.txt", "w") as reading:
        for i, element in enumerate(lines):
            correction = element.replace("\n", "")
            sentence = correction + "\t\t" + tab[i] + "\n"
            reading.write(sentence)
    reading.close()

#this function write the differente buy and sell of the different pair in statistic.txt
def statistics(order, paire, price):
    if (order == 1):
        ordre = "achat"
    else:
        ordre = "vente"
    try:
        if (order == 0):
            with open("files/statistic.txt", "r") as reading:
                lines = reading.readlines()
            with open("files/statistic.txt", "w") as reading:
                for element in lines:
                    if (paire in element and "vente" not in element):
                        correction = element.replace("\n", "")
                        sentence = "\n" + str(correction) + "\t\t|\t" + str(paire) + "\t\t" + str(price) + "\t\t" + str(ordre)
                        reading.write(sentence)
                    else:
                        reading.write(element)
            reading.close()
        else:
            result1 = open("files/statistic.txt", "a")
            result1.write("\n\n" + str(paire) + "\t\t" + str(price) + "\t\t" + str(ordre))
            result1.close()
    except:
        return (0)

def erase_ligne(index):
    temp = -1
    try:
        with open("files/trade.txt", "r") as f:
            lines = f.readlines()
        with open("files/trade.txt", "w") as f:
            for line in lines:
                temp += 1
                if (temp == index):
                    #print(line)
                    #print("line deleted")
                    continue
                else:
                    f.write(line)
        f.close()
    except:
        return (0)

def vente2_test(pair, client):
    try:
        #print(pair)
        price = client.get_asset_balance(asset=pair)
        price_to_sell = float(price["free"])
        return (price_to_sell)
    except:
        return (0)

#this function manage when a crypto money must me sell
def vente_crypto(pair, client):
    pair = pair.replace("\n", "")
    if ("_1" in pair):
        pair = pair.replace("_1", "")
        paire = pair + "USDT"
        price_to_sell = vente2_test(pair, client)
        money_to_sell = price_to_sell * 0.6
    elif ("_2" in pair):
        pair = pair.replace("_2", "")
        paire = pair + "USDT"
        price_to_sell = vente2_test(pair, client)
        temp = (0.67 * price_to_sell)
        money_to_sell = (temp + price_to_sell) * 0.2
    elif ("_3" in pair):
        pair = pair.replace("_3", "")
        paire = pair + "USDT"
        price_to_sell = vente2_test(pair, client)
        money_to_sell = price_to_sell
    else:
        paire = pair + "USDT"
        price_to_sell = vente2_test(pair, client)
        money_to_sell = price_to_sell
        #print(client.get_asset_balance(asset=pair))
    i = 10
    while (i != 0):
        try:
            i -= 1
            client.order_market_sell(symbol=paire, quantity=round(money_to_sell, i))
            statistics(0, paire, price_to_sell)
            #print("sell success")
            return (0)
        except:
            continue
    #print("sell failed")
    return (0)

#this function manage when a crypto money must me buy
def achat_crypto(pair, client, money_trade):
    if ("_L" in pair):
        pair = pair.replace("_L", "")
        money_trade = float(money_trade) * 2
    if (" 1" in pair):
        pair = pair.replace(" 1", "")
    if ("1" in pair):
        pair = pair.replace("1", "")
    paire = pair.replace("\n", "")
    try:
        pair_price = client.get_symbol_ticker(symbol=paire)
        real_price = float(money_trade) / 20 / float(pair_price["price"])
    except:
        return (1)
    #print(client.get_symbol_ticker(symbol=paire))
    i = 10
    while (i != 0):
        try:
            i -= 1
            client.order_market_buy(symbol=paire, quantity=round(real_price, i))
            statistics(1, paire, real_price)
            #print("buy success")
            return (0)
        except:
            continue
    #print("buy failed")
    return (1)

#this function manage the message parsed buy the parser.sh and check if there is crypto money to buy
def check_message():
    temp = 0
    try:
        money = None
        result1 = open("files/trade.txt", "r")
        for ligne in result1:
            if (temp == 0):
                temp += 1
            elif (temp >= 1):
                break
            if ("USDT" in ligne):
                money = ligne.replace("USDT1", "")
            elif ("BTC" in ligne):
                money = ligne.replace("BTC1", "")
        result1.close()
        return (money)
    except:
        return (None)

#try to see if there is so crypto money to sell
def check_sell(client):
    temp2 = 0
    try:
        result = open("files/trade.txt", "r")
        for ligne in result:
            if ("0" in ligne):
                if ("USDT" in ligne):
                    money = ligne.replace("USDT0", "")
                if ("BTC" in ligne):
                    money = ligne.replace("BTC0", "")
                vente_crypto(money, client)
                temp2 += 1
            else:
                continue
        result.close()
    except:
        if (temp2 >= 1):
            return (1)
        else:
            return (None)
    if (temp2 >= 1):
        return (1)
    else:
        return (None)

#erase the line after it have been sell
def erase_line_sell():
    temp2 = 0
    try:
        result = open("files/trade.txt", "r")
        for i, ligne in enumerate(result):
            if ("0" in ligne):
                erase_ligne(i-temp2)
                temp2 += 1
            else:
                continue
        result.close()
    except:
        return (0)

#manage the differents clients of the sql database, if there are new clients, it will add the new clients every weeks
def my_sql_serv(var):
    mydb = mysql.connector.connect(
        host="CompleteThisLine",
        user="CompleteThisLine",
        password="CompleteThisLine",
        database="crypto_client"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT api_key FROM clients")
    api_key1 = mycursor.fetchall()
    mycursor.execute("SELECT api_secret FROM clients")
    api_secret1 = mycursor.fetchall()
    mycursor.execute("SELECT email FROM clients")
    EmailSendingTo1 = mycursor.fetchall()
    mycursor.execute("SELECT MoneyToTrade FROM clients")
    MoneyToTrade1 = mycursor.fetchall()

    for element in EmailSendingTo1:
        var.EmailSendingTo.append(element[0])
    for element in api_key1:
        var.api_key.append(element[0])
    for element in api_secret1:
        var.api_secret.append(element[0])
    for element in MoneyToTrade1:
        var.money_buy.append(element[0])
#put all var to 0 every weeks
def init_var(var):
    var.EmailSendingTo = []
    var.money_trade = []
    var.api_secret = []
    var.money_buy = []
    var.api_key = []

def main():
    var = VarProg()
    tempo = False
    delay = 0
    x = time.time()
    time.sleep(1)
    while (True):
        #every weeks check if new clients, and add them to the loop
        if time.time() - x >= delay: # if the amount of time since enter was pressed is the delay
            init_var(var)
            my_sql_serv(var)
            delay = 604800
        #this is the game loop for buy and sell crypto
        while (True):
            for i, person in enumerate(var.api_key):
                client = Client(person, var.api_secret[i])
                if (check_sell(client) != None):
                    var.erase_sell = 1
                pair = check_message()
                if (pair is not None and "0" not in pair):
                    if (achat_crypto(pair, client, var.money_buy[i]) == 0):
                        var.erase_buy = 1
            if (var.erase_buy == 1):
                erase_ligne(0)
                var.erase_buy = 0
            if (var.erase_sell == 1):
                erase_line_sell()
                var.erase_sell = 0
            if (tempo == True):
                send_mail(var)
                tempo = False
                x = time.time()
            if time.time() - x >= delay:
                tempo = True
                break
            time.sleep(60)
main()