from django.db import models

class DistributedTask(models.Model):
    name = models.CharField(max_length=200)
    map_func = models.TextField()
    reduce_func = models.TextField()
    then_func = models.TextField()
    data = models.TextField()

    # pub_date = models.DateTimeField('date published')
