from django.test import TestCase
from datetime import date
from golfscores.models import GolfCourse, Hole, Game, Score

# Create your tests here.
class GolfScoreIntegrationTests(TestCase):
  def setUp(self):
    new_course = GolfCourse.objects.create(course_name='Odana Hills', 
                                            course_city='Madison', 
                                            course_state='WI')
    Hole.objects.create(course=GolfCourse.objects.get(id=1),
                        hole_number=1,
                        yards=343,
                        handicap=13,
                        par=4)
  
  def test_record_hole(self):
    """
      Check that I can record my score if I played golf on Odana Hills today and parred hole 1
    """
    selected_course = GolfCourse.objects.get(course_name='Odana Hills')
    selected_hole = Hole.objects.get(course=selected_course,
                                      hole_number=1)
    new_game = Game.objects.create(course=selected_course,
                                    played_date=date.today())
    new_score = Score.objects.create(hole=selected_hole,
                                      score=4,
                                      game=new_game)
    self.assertEquals(4, Score.objects.get(game=new_game, 
                                            hole=selected_hole).score) 