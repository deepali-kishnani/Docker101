import os
import socket
import sys

from flask import Flask
from pyfiglet import figlet_format


app = Flask(__name__)

@app.route("/")
def start():
    s = figlet_format('Dell EMC Docker101', font='starwars')
    return s

if __name__ == "__main__":
    app.run(host='0.0.0.0')
