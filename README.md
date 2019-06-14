# SI507 Final Project: Halo 5 Arena Statistics
 
Nate Coryell



[Link to this repository](https://github.com/NCoryell/SI507_Final_Project)



---



## Project Description

This project will create a FLask application that will display information related to the video game Halo 5 competitive multiplayer seasons. The 343 Industries API provides metadata bout about competitive seasons and players. 

The following information about each season has been cached: name, season id, start date, and end date. The following information about the top twenty players from each season is also cached: gamertag, tier, CSR, and rank. 

This information is loaded into the database Halo5_seasons.db. The database consists of three tables, diagrammed in Final_Project_Diagram.jpg. An association table named Leaderboard connects the players in the Players table with the seasons in the Seasons table in which they are ranked.

Three Flask app paths are defined and described below.


HTML, Javascript, and CSS code link pages and format the information from the databases into tables.



## How to run



1. Install all requirements with `pip install -r requirements.txt
2. Run SI507final_project.py



## How to use



1. Navigate to the url displayed in the console.

2. Explore the options in the gray field.
3. Selecting Seasons will display a table containing information about competitive seasons.
4. Selecting Players will display information about players present in competitive season leaderboards.



## Routes in this application


- `/` -> this is the home page

- `/Seasons` -> this route contains a table consisting of Season data
- `/Players` -> this route contains a table consisting of Player data

## How to run tests

1. First... (e.g. access a certain directory if necessary)

2. Second (e.g. any other setup necessary)

3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!



## In this repository:


- Final_Project
  - SI507final_project.py
  - SI507project_tools.py
  - SI507project_tests.py

  - README.md
  - requirements.txt
  - Final_Project_Diagram.jpg
  - metadata_cached_data.json
  - Season_0_Team_Arena_cached_data.json
  - Season_1_Team_Arena_cached_data.json
  - Season_2_Team_Arena_cached_data.json
  - Season_3_Team_Arena_cached_data.json
  - Season_4_Team_Arena_cached_data.json
  - Season_5_Team_Arena_cached_data.json
  - Season_6_Team_Arena_cached_data.json
  - Season_7_Team_Arena_cached_data.json
  - Season_8_Team_Arena_cached_data.json
  - Season_9_Team_Arena_cached_data.json
  - Season_10_Team_Arena_cached_data.json
  - Season_11_Team_Arena_cached_data.json
  - Season_12_Team_Arena_cached_data.json
- Screenshots
  - Homepage.jpg
  - Players.jpg
  - Seasons.jpg
- templates
  - home_template.html
  - players_template.html
  - seasons_template.html



---

## Code Requirements for Grading

Please check the requirements you have accomplished in your code as demonstrated.

- [x] This is a completed requirement.

- [ ] This is an incomplete requirement.



Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.



### General

- [x] Project is submitted as a Github repository

- [x] Project includes a working Flask application that runs locally on a computer

- [x] Project includes at least 1 test suite file with reasonable tests in it.

- [x] Includes a `requirements.txt` file containing all required modules to run program

- [x] Includes a clear and readable README.md that follows this template

- [x] Includes a sample .sqlite/.db file

- [x] Includes a diagram of your database schema

- [x] Includes EVERY file needed in order to run the project

- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working



### Flask Application

- [x] Includes at least 3 different routes

- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course

- [x] Interactions with a database that has at least 2 tables

- [x] At least 1 relationship between 2 tables in database

- [x] Information stored in the database is viewed or interacted with in some way



### Additional Components (at least 6 required)

- [ ] Use of a new module

- [ ] Use of a second new module

- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)

- [x] A many-to-many relationship in your database structure

- [ ] At least one form in your Flask application

- [x] Templating in your Flask application

- [x] Inclusion of JavaScript files in the application

- [x] Links in the views of Flask application page/s

- [ ] Relevant use of `itertools` and/or `collections`

- [ ] Sourcing of data using web scraping

- [x] Sourcing of data using web REST API requests

- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset

- [ ] Caching of data you continually retrieve from the internet in some way



### Submission

- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)

- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
