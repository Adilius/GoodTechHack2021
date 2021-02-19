from flask import Flask, render_template
import os

template_dir = os.path.abspath('../GoodTechHack2021/templates')
app = Flask(__name__, template_folder=template_dir) #Create flask application instance

@app.route('/')
def index():
    title = "Good Tech Hack 2021"
    return render_template("index.html", title=title)