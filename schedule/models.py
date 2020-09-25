from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django_currentuser.db.models import CurrentUserField


class Comment(models.Model):
    created_by= CurrentUserField(User)
    name = models.CharField(max_length=254)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
class Meta:
    abstract = True

    def __str__(self):
        
        super(Comment, self).save()
        return self.name, self.user.username