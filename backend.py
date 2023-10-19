import os
import time
import subprocess
import requests
import logging
from steam import Steam
from os import system, chdir
from flask import Flask, request, redirect, url_for, render_template

application = Flask(__name__)

passwd = "tjftmddl413**"

KEY = "0FFABCFDC4DFBCBDE48CB28D09B17653"
steam = Steam(KEY)

@application.route('/', methods=['GET', 'POST'])
def frontend():
    return render_template('frontend.html')

@application.route('/find', methods=['PUT'])
def find():
    게임이름 = request.form["게임이름"]
    games = steam.apps.search_games(게임이름)
    
    return_text='<div id="results">'
    for i in range (len(games["apps"])):
        id = games["apps"][i]["id"]
        name = games["apps"][i]["name"].encode().decode("unicode-escape")
        return_text = return_text + f'<button hx-get="/find/{id}" hx-swap="outerHTML" hx-target="#results"  class="btn btn-primary">{name}</button>'
    return_text = return_text + '</div>'
    return return_text

@application.route('/find/<string:id>', methods=['GET'])
def find2(id):
    game = steam.apps.search_games(id)
    korean = requests.get(f"https://store.steampowered.com/api/appdetails?cc=KR&filters=price_overview&appids={id}/").json()[str(id)]["data"]["price_overview"]["final_formatted"][2:] + "원"
    name = game["apps"][0]["name"]
    link = game["apps"][0]["link"]
    image = game["apps"][0]["img"]
    return f'<div id="result_game"><div>{name}</div><div>{link}</div><img src="{image}"><div>{korean}</div></div>'

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80)