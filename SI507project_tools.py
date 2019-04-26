import requests
import json
import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Functions to gather and cache data from the 343 Industries API
CACHE_FNAME = "Season_0_Team_Arena_cached_data.json"
def get_halo_info():
    baseurl = "https://www.haloapi.com/stats/h5/player-leaderboards/csr/2041d318-dd22-47c2-a487-2818ecf14e41/c98949ae-60a8-43dc-85d7-0feb0b92e719"
    params_diction = {}
    headers = {}
    params_diction['count'] = 20
    resp = requests.get(baseurl, params=params_diction, headers={"Ocp-Apim-Subscription-Key":"dda726bf5f8141439b8179d29626de13"})
    python_obj = json.loads(resp.text)
    CACHE_DICTION = python_obj
    fw = open(CACHE_FNAME, 'w')
    fw.write(json.dumps(CACHE_DICTION))
    fw.close()
    return python_obj

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Halo5_sample.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

collections = db.Table('collections',
    db.Column('player_id', db.String(64), db.ForeignKey('players.id'), primary_key=True),
   db.Column('playlist_id', db.String(64), db.ForeignKey('playlists.id'), primary_key=True)
   )

class Arena_Season(db.Model):
   __tablename__ = "seasons"
   name = db.Column(db.String(64), primary_key=True)
   season_id = db.Column(db.String(64))
   start_date = db.Column(db.String(64))
   end_date = db.Column(db.String(64))
   playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))
   playlists = db.relationship("Playlist", backref='seasons')

#Change relationship between two tables to many to many
class Playlist(db.Model):
   __tablename__ = "playlists"
   id = db.Column(db.String(64), primary_key=True)
   name = db.Column(db.String(64))
   description = db.Column(db.String(64))
   game_mode = db.Column(db.String(64))
   seasons = db.Column(db.String(64), db.ForeignKey('seasons.name'))

class Player(db.Model):
   __tablename__ = "players"
   id = db.Column(db.Integer, primary_key=True)
   gamertag = db.Column(db.String(64))
   tier = db.Column(db.Integer)
   csr = db.Column(db.Integer)
   rank = db.Column(db.Integer)
   playlist_id = db.Column(db.String(64), db.ForeignKey('playlists.id'))
   playlists = db.relationship("Playlist", backref='players')

def get_season_data(season):
    seasons_info = []
    seasons_info.append(season['name'])
    seasons_info.append(season['startDate'])
    seasons_info.append(season['endDate'])
    seasons_info.append(season['id'])
    seasons_info.append(season['playlists'][0]['id'])
    return seasons_info

with open('metadata_cached_data.json', 'r') as f:
    season_metadata = json.load(f)
with open('Season_0_Team_Arena_cached_data.json', 'r') as f:
    season_0_leaderboard = json.load(f)
with open('Season_1_Team_Arena_cached_data.json', 'r') as f:
    season_1_leaderboard = json.load(f)
with open('Season_2_Team_Arena_cached_data.json', 'r') as f:
    season_2_leaderboard = json.load(f)
with open('Season_3_Team_Arena_cached_data.json', 'r') as f:
    season_3_leaderboard = json.load(f)
with open('Season_4_Team_Arena_cached_data.json', 'r') as f:
    season_4_leaderboard = json.load(f)
with open('Season_5_Team_Arena_cached_data.json', 'r') as f:
    season_5_leaderboard = json.load(f)
with open('Season_6_Team_Arena_cached_data.json', 'r') as f:
    season_6_leaderboard = json.load(f)
with open('Season_7_Team_Arena_cached_data.json', 'r') as f:
    season_7_leaderboard = json.load(f)
with open('Season_8_Team_Arena_cached_data.json', 'r') as f:
    season_8_leaderboard = json.load(f)
with open('Season_9_Team_Arena_cached_data.json', 'r') as f:
    season_9_leaderboard = json.load(f)
with open('Season_10_Team_Arena_cached_data.json', 'r') as f:
    season_10_leaderboard = json.load(f)
with open('Season_11_Team_Arena_cached_data.json', 'r') as f:
    season_11_leaderboard = json.load(f)
with open('Season_12_Team_Arena_cached_data.json', 'r') as f:
    season_12_leaderboard = json.load(f)
#
# with open
#
# class Season:
#    def __init__(self, info):
#        self.title = info[3]
#
#    self __str__(self):
#        return "{}<br>".format(self.title)
#
#
#
# class Stats:
#    def __init__(self, info):
#        self.gamertag = info[object]
#
#    def __str__(self):
#        return "{}<br>".format(self.gamertag)
#
# if __name__ == '__main__':
#    db.create_all()
# app.run()
