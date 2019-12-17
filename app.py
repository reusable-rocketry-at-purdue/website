from flask import Flask, flash, request, redirect, render_template, send_from_directory
import os

app = Flask(__name__)
	
@app.route('/')
def mainPage():
	return render_template("comingSoon.html")

if __name__ == '__main__':
    app.run(debug = True)