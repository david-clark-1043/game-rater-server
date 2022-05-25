"""View module for handling requests about games"""


from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gameraterapi.models import Game, Gamer


class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game
        Returns:
            Response -- JSON serialized game
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games
        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()

        # Add in the next 3 lines
        # game_category = request.query_params.get('category', None)
        # if game_category is not None:
        #     games = games.filter(game_type_id=game_category)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer)

        game = serializer.instance
        game.categories.add(*request.data["categories"])
        game = GameSerializer(game)
        return Response(game.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        game = Game.objects.get(pk=pk)
        serializer = CreateGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # game_categories = GameCategory.objects.filter(game_id=pk)
        game.categories.remove(*game.categories.all())
        game.categories.add(*request.data["categories"])

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE method for games"""
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = (
                    'id',
                    'title',
                    'description',
                    'designer',
                    'gamer',
                    'year_released',
                    'number_of_players',
                    'est_time_minutes',
                    'age_rec',
                    'categories',
                    'average_rating'
                )
        depth = 2

class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
                    'id',
                    'title',
                    'description',
                    'designer',
                    'year_released',
                    'number_of_players',
                    'est_time_minutes',
                    'age_rec'
        )
