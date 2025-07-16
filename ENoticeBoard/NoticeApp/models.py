# blogApp/models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.content}) ({self.author}) ({self.created_at}) ({self.updated_at})"
    class Meta:
        verbose_name = "Notice"  # Singular
        verbose_name_plural = "Notices"  # Plural