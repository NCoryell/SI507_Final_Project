import requests
import json
import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Functions to gather and cache data from the 343 Industries API
CACHE_FNAME = "Season_1_Team_Arena_cached_data.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}
def get_halo_info(player):
    baseurl = "https://www.haloapi.com/stats/h5/player-leaderboards/csr/2fcc20a0-53ff-4ffb-8f72-eebb2e419273/c98949ae-60a8-43dc-85d7-0feb0b92e719"
    params_diction = {}
    headers = {}
    params_diction['player'] = player
    resp = requests.get(baseurl, params=params_diction, headers={"Ocp-Apim-Subscription-Key":"dda726bf5f8141439b8179d29626de13"})
    python_obj = json.loads(resp.text)
    CACHE_DICTION = python_obj
    fw = open(CACHE_FNAME, 'w')
    fw.write(json.dumps(CACHE_DICTION))
    fw.close()
    return python_obj

#print(get_halo_info('Nato234'))

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

#SQL database construction
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Halo5_sample.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

#collections =

class Arena_Season(db.Model):
    __tablename__ = "seasons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    start_date = db.Column(db.String(64))
    end_date = db.Column(db.String(64))
    leaderboard_id = db.Column(db.Integer)

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    gamertag = db.Column(db.String(64))
    tier = db.Column(db.Integer)
    csr = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    leaderboard_id = db.Column(db.Integer)

#class Season:
#    def __init__(self, info):
#        self.title = info[3]
#
#    self __str__(self):
#        return "{}<br>".format(self.title)

class Stats:
    def __init__(self, info):
        self.gamertag = info[object]

    def __str__(self):
        return "{}<br>".format(self.gamertag)
