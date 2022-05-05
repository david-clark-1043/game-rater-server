from django.db import models

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

    # @property
    # def joined(self):
    #     return self.__joined

    # @joined.setter
    # def joined(self, value):
    #     self.__joined = value