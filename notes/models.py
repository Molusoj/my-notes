from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.


class Note(models.Model):
    # TODO: Define fields here
    title = models.CharField(max_length=220)
    slug = models.SlugField()
    date_added = models.DateTimeField(default=datetime.now())
    note = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def summary(self):
        return self.note[:200]

    def pub_date_pretty(self):
        return self.date_added.strftime('%b %e,%y')

    class meta:
        ordering = ('-date_added',)
