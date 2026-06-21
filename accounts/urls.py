from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile_view, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("projects/", views.projects_view, name="projects"),
     path(
    "project/<int:project_id>/",
    views.project_detail,
    name="project_detail"
),
    path("create-project/", views.create_project, name="create_project"),
    path("join-project/<int:project_id>/", views.join_project, name="join_project"),
    path("project-requests/", views.project_requests, name="project_requests"),
    path("accept-request/<int:request_id>/",
    views.accept_request,
    name="accept_request"
),
    path(
    "withdraw-request/<int:project_id>/",
    views.withdraw_request,
    name="withdraw_request"
),

path(
    "reject-request/<int:request_id>/",
    views.reject_request,
    name="reject_request"
),

path(
    "my-projects/",
    views.my_projects,
    name="my_projects"
),

path(
    "",
    views.home_view,
    name="home"
),

path(
    "students/",
    views.students_view,
    name="students"
),

path(
    "skills/",
    views.skills_view,
    name="skills"
),

path(
    "groups/",
    views.groups_view,
    name="groups"
),

path(
    "student/<int:profile_id>/",
    views.student_profile,
    name="student_profile"
),

path(
    "join-group/<int:group_id>/",
    views.join_group,
    name="join_group"
),

path(
    "my-groups/",
    views.my_groups,
    name="my_groups"
),

path(
    "leave-group/<int:group_id>/",
    views.leave_group,
    name="leave_group"
),

path(
    "logout/",
    views.logout_view,
    name="logout"
),

path(
    "create-group/",
    views.create_group,
    name="create_group"
),

path(
    "group/<int:group_id>/",
    views.group_detail,
    name="group_detail"
),
]