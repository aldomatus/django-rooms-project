from django.db import models


class User(models.Model):
    user_id = models.SmallAutoField(primary_key=True)
    user_email = models.CharField(unique=True, max_length=120)
    is_admin = models.BooleanField(null=False, default=False)
