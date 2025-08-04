from django.db import models
from django.contrib.auth.models import User

class UserProfile(model.Model):
    user = models.oneToOneField(User, on_delete=models.CASECADE, related_name='profile')
    phone_number = models.CharFeild(max_length=15, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username