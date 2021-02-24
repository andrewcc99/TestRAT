import socket
import socketserver
import os
import time
import webbrowser
import locale
import threading
import sys
from tkinter import *
from tkinter.ttk import *
from pip._vendor import requests


portClient = 80
portServer = 80
a_website = r"https://www.google.com/"
datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())



#TCP Socket Server

def startServer():
    s = socket.socket()
    print
    "Socket successfully created"

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', portServer))
    print
    "socket binded to %s" % (portServer)

    # put the socket into listening mode
    s.listen(5)
    print
    "socket is listening"

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print
        'Got connection from', addr

        # send a thank you message to the client.
        c.send('Thank you for connecting')
        c.close()


#Client side connection

def startClient():

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print
        "Socket successfully created"

    except socket.error as err:
        print
        "socket creation failed with error %s" % (err)

    try:

        host_ip = socket.gethostbyname('www.google.com')

    except socket.gaierror:

        # this means could not resolve the host
        print
        "there was an error resolving the host"
        sys.exit()

    # connecting to the server
    s.connect((privateIP, portClient))


startServer()
root = Tk()
root.geometry('100x100')

# This will create style object
style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).

style.configure('W.TButton', font=
('calibri', 10, 'bold', 'underline'),
                foreground='red')

# Style will be reflected only on
# this button because we are providing
# style only on this Button.
''' Button 1'''

btn1 = Button(root, text='Connect',
              style='W.TButton',
              command=None)
btn1.grid(row=0, column=3, padx=100)

''' Button 2'''
btn2 = Button(root, text='Click me !', command=None)
btn2.grid(row=1, column=3, pady=10, padx=100)

root.mainloop()

