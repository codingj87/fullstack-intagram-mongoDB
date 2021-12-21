from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_index=True, blank=True, help_text="사용자 이름")
    age = models.CharField(max_length=32, blank=True, help_text="나이")
    