from django.shortcuts import render
from golfscores.models import GolfCourse, Hole, Score, Game
from django.http import HttpResponse
# Create your views here.
def index(request):
  all_games = Game.objects.all()
  context = {}
  return render(request, 'golfscores/index.html', context)
