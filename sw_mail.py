#!/usr/bin/python

import imaplib
import email

demo = True

if not demo: 

    USER = "xxxx"
    PASS = "xxxx"
    SERVER = "xxx.xxx.xx"

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(USER,PASS)

    mcnt = 0

    # Posteingang auswaehlen
    type, data = mail.select('INBOX')

    # nach bestimmtem Substring im Betreff (leer "" alles) filtern und in Liste ablegen

    type, [mids] = mail.uid('search',None,'(UNSEEN SUBJECT "")')

    # type, [mids] = mail.uid('search',None,'(SUBJECT "")')

    if mids:

        # fuer alle ermittelten Mail-IDs
        for id in mids.split():
            mcnt = mcnt + 1 
        print("-------------------------------------------")
        print("Anzahl Nachrichten:")
        print(mcnt)
        print("-------------------------------------------")
          
    else:
        print("Keine neuen Nachrichten gefunden.")

    mail.close()
    mail.logout()

else:

    mcnt = 3

    print("-------------------------------------------")
    print("Anzahl Nachrichten (Demo): 3")
    print("-------------------------------------------")




