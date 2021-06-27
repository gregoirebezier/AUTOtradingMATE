#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.message import EmailMessage
import smtplib
import time
import subprocess
from subprocess import check_output

#This is a script to send you a message if a program stopped (he check it every half days)
def send_email():
    EMAIL_ADDRESS = "CompleteThisLine@gmail.com"
    EMAIL_PASSWORD = "CompleteThisLine"

    x = 0

    msg = EmailMessage()
    msg['Subject'] = "Arret d'une ou plusieurs application !" #le sujet du mail
    msg['From'] = EMAIL_ADDRESS #Ton adresse mail avec laquelle tu veux envoyer le mail
    msg['To'] = 'CompleteThisLine@gmail.com' #l'adresse mail a qui tu veux envoyer le message
    msg.set_content("Take care, an applications on the VPS stopped working !\nIP : CompleteThisLine") #le message du mail

    while x < 1:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        x += 1


def report_check():
    out = str(check_output(["bash", "../BashScript/check.sh"]))
    if ("ERROR" in out):
        return (84)
    return (0)


def main():
    while True:
        if (report_check() == 84):
            send_email()
            return (0)
        time.sleep(86400)
main()