from flask import Flask, render_template, request, session, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv('SECRET','randomstring123')