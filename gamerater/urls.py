from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from gameraterapi.views import GameView, CategoryView
from gameraterapi.views import register_user, login_user
from gameraterapi.views.image import ImageView
from gameraterapi.views.rating import RatingView
from gameraterapi.views.review import ReviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')
router.register(r'reviews', ReviewView, 'review')
router.register(r'ratings', RatingView, 'rating')
router.register(r'images', ImageView, 'rating')
router.register(r'games', GameView, 'game')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]