from django.db import models


class GolfCourse(models.Model):
  id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=250)
  course_city = models.CharField(max_length=250)
  course_state = models.CharField(max_length=250)


class Hole(models.Model):
  id = models.AutoField(primary_key=True)
  course = models.ForeignKey(GolfCourse,
                              on_delete=models.CASCADE)
  hole_number = models.IntegerField()
  yards = models.IntegerField()
  handicap = models.IntegerField()
  par = models.IntegerField()


class Game(models.Model):
  id = models.AutoField(primary_key=True)
  course = models.ForeignKey(GolfCourse, 
                              on_delete=models.CASCADE)
  played_date = models.DateField()


class Score(models.Model):
  id = models.AutoField(primary_key=True)
  hole = models.ForeignKey(Hole, 
                            on_delete=models.CASCADE)
  score = models.IntegerField()
  game = models.ForeignKey(Game, 
                            on_delete=models.CASCADE)
