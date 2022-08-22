from flask import Flask, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv('SECRET','randomstring123')