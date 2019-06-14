import unittest
from SI507project_tools import *

#Testing to make sure that there are more than one players per season. Ideally the cached data should include 20 players.
class Player_Count(unittest.TestCase):
    def test_Player_instances(self):
        players = Player.query.all()
        self.assertTrue(len(players) > 0)

#Testing that every Season has a name value.
class Season_Name(unittest.TestCase):
    def test_Arena_instances(self):
        seasons = Arena_Season.query.all()
        for item in seasons:
            self.assertTrue(len(item.name) > 0)

#Filtering a known Season ID and verifying that that the association table is populated with 20 players for that season. This will verify that the association table was constructed correctly.
class Leaderboard_Filter(unittest.TestCase):
    def test_id_check(self):
        lbid = leaderboard.query.filter_by(season_id='2041d318-dd22-47c2-a487-2818ecf14e41')
        self.assertEqual(len(lbid), 20)

if __name__ == "__main__":
    unittest.main(verbosity=2)
