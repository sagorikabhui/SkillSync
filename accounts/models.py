from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    college = models.CharField(
        max_length=100
    )

    year = models.CharField(
        max_length=50
    )

    bio = models.TextField()

    can_teach = models.TextField()

    wants_to_learn = models.TextField()

    def __str__(self):
        return self.user.username
    
class Project(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    skills_required = models.CharField(
        max_length=300
    )

    team_size = models.IntegerField()
    
    description = models.TextField(
    blank=True
    )
    
    github_link = models.URLField(
    blank=True,
    null=True
)
    
    status = models.CharField(
    max_length=20,
    default="Planning"
)
    
    progress = models.IntegerField(
    default=0
)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
    
class JoinRequest(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    def __str__(self):
        return f"{self.student.username} -> {self.project.title}"
    
class Group(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.name
    
class GroupMember(models.Model):

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return f"{self.student.username} - {self.group.name}"