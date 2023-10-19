import os
import time
import subprocess
import requests
import logging
from os import system, chdir
from flask import Flask, request, redirect, url_for, render_template

application = Flask(__name__)

passwd = "tjftmddl413**"

@application.route('/', methods=['GET', 'POST'])
def frontend():
    return render_template('frontend.html')

@application.route('/find', methods=['PUT'])
def find():
    게임이름 = request.form["게임이름"]
    return f"""
<div hx-target="result_form">
  <div><label>게임이름:</label>{게임이름}</div>
</div>
"""

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80)