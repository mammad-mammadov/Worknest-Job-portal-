from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/')
    motivation_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
    
class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} saved {self.job.title}"