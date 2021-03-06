"""Module for generating top 5 games report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gameraterreports.views.helpers import dict_fetch_all

class GamesGreaterThan5PlayersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT *
                FROM gameraterapi_game g
                WHERE g.number_of_players > 5
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_more_than_5_players = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                game = {
                    "id": row['id'],
                    "title": row['title'],
                    "description": row['description'],
                    "designer": row['designer'],
                    "year_released": row['year_released'],
                    "est_time_minutes": row['est_time_minutes'],
                    "number_of_players": row['number_of_players'],
                    "age_rec": row['age_rec'],
                    "gamer_id": row['gamer_id']
                }
                games_more_than_5_players.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/list_games_more_than_5_players.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "games_more_than_5_players_list": games_more_than_5_players
        }

        return render(request, template, context)
