from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False)
    city = models.CharField(max_length=200, blank=False, null=False)
    mascot = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField()
    
    def __unicode__(self):
      return self.name

class Player(models.Model):

    first_name = models.CharField("First Name", max_length=200, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=200, blank=False, null=False)
    
    team = models.ForeignKey(Team)
    
    class Meta:
      verbose_name = "Player"
      verbose_name_plural = "Players"
      
    def __unicode__(self):
      return '%s %s' % (self.first_name, self.last_name)
      
