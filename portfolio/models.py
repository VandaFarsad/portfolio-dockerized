from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="projects")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="skills")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
