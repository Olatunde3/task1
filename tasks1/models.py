from django.db import models

# Create your models here.

class Slack(models.Model):
    slack_name = models.CharField(max_length=50)
    current_day = models.CharField(max_length=10)
    utc_time = models.DateTimeField( auto_now_add=True)
    track = models.CharField(max_length=50)
    github_file_url = models.CharField(max_length=150)
    github_repo_url = models.CharField(max_length=150)

    def __str__(self):
        return self.slack_name