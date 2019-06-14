import requests
import json
import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

season_dict = {}

CACHE_FNAME = "Season_0_Team_Arena_cached_data.json"
def get_player_info():
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

def load_season_data(input):
    with open(input, 'r') as f:
        season_metadata = json.load(f)
    for item in season_metadata:
        season = get_or_create_season(item['name'], item['id'], item['startDate'], item['endDate'])
        season_dict[item['id']] = season

def load_player_data(input):
    with open(input, 'r') as f:
        player_data = json.load(f)
    playlist_id = player_data['Links']['Self']['Path'][28:64]
    for item in player_data['Results']:
        player = get_or_create_players(item['Player']['Gamertag'], item['Score']['Tier'], item['Score']['Csr'], item['Score']['Rank'], playlist_id)

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Halo5_seasons.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

leaderboard = db.Table('leaderboard',db.Column('season_id',db.String(64), db.ForeignKey('seasons.season_id')),db.Column('player_id',db.Integer, db.ForeignKey('players.id')))

class Arena_Season(db.Model):
   __tablename__ = "seasons"
   name = db.Column(db.String(64))
   season_id = db.Column(db.String(64), primary_key=True)
   start_date = db.Column(db.String(64))
   end_date = db.Column(db.String(64))
   players = db.relationship('Player', secondary=leaderboard,backref=db.backref('seasons',lazy='dynamic'),lazy='dynamic')

class Player(db.Model):
   __tablename__ = "players"
   id = db.Column(db.Integer, primary_key=True)
   gamertag = db.Column(db.String(64))
   tier = db.Column(db.String(64))
   csr = db.Column(db.String(64))
   rank = db.Column(db.String(64))

def get_or_create_season(season_name, season_id, start_date, end_date):
    season = Arena_Season.query.filter_by(name=season_name).first()
    if season:
        season.start_date = start_date
        season.season_id = season_id
        season.end_date = end_date
        session.add(season)
        session.commit()
        return season
    else:
        season = Arena_Season(name=season_name, season_id=season_id, start_date=start_date, end_date=end_date)
        session.add(season)
        session.commit()
        return season

def get_or_create_players(player_name, tier, csr, rank, season_name):
    player = Player.query.filter_by(gamertag=player_name).first()
    if player:
        player.tier = tier
        player.csr = csr
        player.rank = rank
        season_dict[season_name].players.append(player)
        session.add(player)
        session.commit()
        return player
    else:
        player = Player(gamertag=player_name, tier=tier, csr=csr, rank=rank)
        season_dict[season_name].players.append(player)
        session.add(player)
        session.commit()
        return player

@app.route('/')
def index():
    return render_template('home_template.html')

@app.route('/Seasons')
def pull_season():
    seasons = Arena_Season.query.all()
    names = []
    ids = []
    start = []
    end = []
    for s in seasons:
        names.append(s.name)
        ids.append(s.season_id)
        start.append(s.start_date)
        end.append(s.end_date)
    return render_template('seasons_template.html',names=names, ids=ids, start=start, end=end)

@app.route('/Players')
def pull_players():
    players = Player.query.all()
    gamertag = []
    tier = []
    csr = []
    rank = []
    season_name = []
    for p in players:
        gamertag.append(p.gamertag)
        tier.append(p.tier)
        csr.append(p.csr)
        rank.append(p.rank)
    return render_template('players_template.html', gamertag=gamertag, tier=tier, csr=csr, rank=rank)

# load_season_data('metadata_cached_data.json')
# load_player_data('Season_0_Team_Arena_cached_data.json')
# load_player_data('Season_1_Team_Arena_cached_data.json')
# load_player_data('Season_2_Team_Arena_cached_data.json')
# load_player_data('Season_3_Team_Arena_cached_data.json')
# load_player_data('Season_4_Team_Arena_cached_data.json')
# load_player_data('Season_5_Team_Arena_cached_data.json')
# load_player_data('Season_6_Team_Arena_cached_data.json')
# load_player_data('Season_7_Team_Arena_cached_data.json')
# load_player_data('Season_8_Team_Arena_cached_data.json')
# load_player_data('Season_9_Team_Arena_cached_data.json')
# load_player_data('Season_10_Team_Arena_cached_data.json')
# load_player_data('Season_11_Team_Arena_cached_data.json')
# load_player_data('Season_12_Team_Arena_cached_data.json')

if __name__ == '__main__':
    db.create_all()
app.run()
