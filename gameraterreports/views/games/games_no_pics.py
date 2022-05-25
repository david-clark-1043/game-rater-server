"""Module for generating games in category count report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gameraterreports.views.helpers import dict_fetch_all

class GamesNoPicsList(View):
    def get(self, request):
        return ""