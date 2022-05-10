from django.db import models

from gameraterapi.models.rating import Rating

class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=300)
    designer = models.CharField(max_length=55)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time_minutes = models.IntegerField()
    age_rec = models.IntegerField()
    categories = models.ManyToManyField("Category",
                                    through="GameCategory",
                                    related_name="games")

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Rating.objects.filter(game=self)

        if(len(ratings) == 0):
            return "No ratings"
        else:
            # Sum all of the ratings for the game
            total_rating = 0
            for rating in ratings:
                total_rating += rating.rating

            # Calculate the average and return it.
            
            average = total_rating / len(ratings)
            return average
            # If you don't know how to calculate average, Google it.
