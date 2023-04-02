from django.db import models

from account.models import CustomUser
from main.models import Film


# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} -> {self.film}"


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


