# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:42:15 2019

@author: ottil
"""

from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result = "All OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())

if __name__ =="__main__":
    app.run(debug=True)
