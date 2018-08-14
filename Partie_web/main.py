# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:31:50 2018

@author: nisha
"""
from __future__ import division, print_function
from connectionBD import connection_BD
from requetesSQL import *
import pandas as pd

# Flask utils
from flask import Flask, request, render_template, redirect
#from gevent.wsgi 
#import WSGIServer

#%%

app = Flask(__name__)

@app.route("/") #page d'acceuil 
def index():
    return render_template("home.html", message = "Hello World!")
