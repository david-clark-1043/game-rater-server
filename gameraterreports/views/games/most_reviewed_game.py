"""Module for generating top 5 games report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from gameraterreports.views.helpers import dict_fetch_all

class MostReviewedGameList(View):
    def get(self, request):
        return ""