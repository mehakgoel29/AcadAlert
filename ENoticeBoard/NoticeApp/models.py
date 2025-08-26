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

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('administrative', 'Administrative'),
        ('event', 'Event'),
        ('exam', 'Exam'),
        ('fee', 'Fee Related'),
        ('general', 'General'),
        ('holiday', 'Holiday'),
        ('sports', 'Sports'),
        ('placement', 'Placement'),
        ('scholarship', 'Scholarship'),
    ]
    STATUS_CHOICES = (
    ('approved', 'Approved'),
    ('pending', 'Pending'),
)

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    target_audience = models.CharField(max_length=50, default="all")
    attachment = models.FileField(upload_to="attachments/", null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    approved = models.BooleanField(default=False)  # admin approval ke liye
    #approved = models.BooleanField(default=False)  
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # agar approved tick ho gaya → status = Approved
            if self.approved:
                self.status = "approved"
            else:
                self.status = "pending"
            super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Notice"  # Singular
        verbose_name_plural = "Notices"  # Plural