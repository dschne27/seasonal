import os

from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
    
if __name__ == "__main__":
    app.run(debug=True)