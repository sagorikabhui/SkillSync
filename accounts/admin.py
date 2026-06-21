from django.contrib import admin
from .models import Profile, Project, JoinRequest, Group, GroupMember

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(JoinRequest)
admin.site.register(Group)
admin.site.register(GroupMember)