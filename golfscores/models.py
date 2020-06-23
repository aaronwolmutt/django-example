from django.db import models


class GolfCourse(models.Model):
  course_id = models.IntegerField(primary_key=True, 
                                  auto_created=True)
  course_name = models.TextField

class Hole(models.Model):
  hole_id = models.IntegerField(primary_key=True,
                                auto_created=True)
  course_id = models.ForeignKey(GolfCourse,
                                on_delete=models.CASCADE)
  hole_number = models.IntegerField
  yards = models.IntegerField
  handicap = models.IntegerField
  par = models.IntegerField

class Score(models.Model):
  score_id = models.IntegerField(primary_key=True, 
                                  auto_created=True)
  hole_id = models.ForeignKey(Hole, 
                                on_delete=models.CASCADE)
  played_date = models.DateField
  score = models.IntegerField