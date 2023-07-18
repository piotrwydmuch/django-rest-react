from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    salary = models.FloatField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title