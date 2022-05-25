"""Module for generating games in category count report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gameraterreports.views.helpers import dict_fetch_all

class GamesNoPicsList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT g.*
                FROM gameraterapi_game g
                LEFT JOIN gameraterapi_image i
                    ON i.game_id = g.id
                WHERE i.url ISNULL

            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_no_pics = []

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
                games_no_pics.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/list_games_no_pics.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "games_no_pics_list": games_no_pics
        }

        return render(request, template, context)