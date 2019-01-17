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

#@app.route("/contactus")
#def contactus():
#    return render_template("contactus.html")

#@app.route("/signup", methods=["POST"])
#def sign_up():
#    form_data = request.form
#    print (form_data["email"])
#    return "All ok"

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result = "All OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())

app.run(debug=True)
# Calling run on the app object.