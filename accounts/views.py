from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Project, JoinRequest
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout



def signup(request):

    if request.method == "POST":

        username = request.POST["username"]

        email = request.POST["email"]

        password = request.POST["password"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        
        Profile.objects.create(
            user=user,
            college="",
            year="",
            bio="",
            can_teach="",
            wants_to_learn=""
            )

        return redirect("login")
    
    return render(
        request,
        "accounts/signup.html"
    )
    
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        return render(
            request,
            "accounts/login.html",
            {
                "message": "Invalid Username or Password"
            }
        )

    return render(
        request,
        "accounts/login.html"
    )
    
@login_required
def my_projects(request):

    created_projects = Project.objects.filter(
        owner=request.user
    )

    joined_projects = Project.objects.filter(
        joinrequest__student=request.user,
        joinrequest__status="Accepted"
    )

    for project in created_projects:

        project.accepted_count = JoinRequest.objects.filter(
            project=project,
            status="Accepted"
        ).count()

    return render(
        request,
        "accounts/my_projects.html",
        {
            "created_projects": created_projects,
            "joined_projects": joined_projects
        }
    )
    
@login_required
def profile_view(request):

    profile = request.user.profile

    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile
        }
    )
  

def projects_view(request):

    projects = Project.objects.all()

    if request.user.is_authenticated:
        joined_projects = JoinRequest.objects.filter(
        student=request.user,
        status="Pending"
    ).values_list(
        "project_id",
        flat=True
    )
    else:
        joined_projects = []

    for project in projects:

        accepted_members = JoinRequest.objects.filter(
            project=project,
            status="Accepted"
        ).count()

        project.is_full = accepted_members >= project.team_size

    return render(
        request,
        "accounts/projects.html",
        {
            "projects": projects,
            "joined_projects": joined_projects
        }
    )
    
@login_required
def create_project(request):

    if request.method == "POST":

        title = request.POST["title"]

        description = request.POST["description"]

        skills_required = request.POST["skills_required"]

        team_size = request.POST["team_size"]

        github_link = request.POST["github_link"]

        status = request.POST["status"]

        # progress = request.POST["progress"]

        Project.objects.create(

            owner=request.user,

            title=title,

            description=description,

            skills_required=skills_required,

            team_size=team_size,

            github_link=github_link,

            status=status,

            

        )

        return redirect("/accounts/projects/")

  
@login_required
def join_project(request, project_id):

    project = Project.objects.get(id=project_id)

    existing_request = JoinRequest.objects.filter(
        project=project,
        student=request.user
    ).first()

    if existing_request:

        existing_request.status = "Pending"
        existing_request.save()

    else:

        JoinRequest.objects.create(
            project=project,
            student=request.user
        )

    return redirect("/accounts/projects/")
  
@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        profile.college = request.POST["college"]
        profile.year = request.POST["year"]
        profile.bio = request.POST["bio"]
        profile.can_teach = request.POST["can_teach"]
        profile.wants_to_learn = request.POST["wants_to_learn"]

        profile.save()

        return redirect("/accounts/profile/")

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "profile": profile
        }
    )
    
    
@login_required
def project_requests(request):

    requests = JoinRequest.objects.filter(
        project__owner=request.user
    )

    return render(
        request,
        "accounts/project_requests.html",
        {
            "requests": requests
        }
    )
    
@login_required
def accept_request(request, request_id):

    join_request = JoinRequest.objects.get(
        id=request_id
    )

    join_request.status = "Accepted"

    join_request.save()

    return redirect(
        "/accounts/project-requests/"
    )
    
@login_required
def reject_request(request, request_id):

    join_request = JoinRequest.objects.get(
        id=request_id
    )

    join_request.status = "Rejected"

    join_request.save()

    return redirect(
        "/accounts/project-requests/"
    )
    
@login_required
def withdraw_request(request, project_id):

    JoinRequest.objects.filter(
        student=request.user,
        project_id=project_id,
        status="Pending"
    ).delete()

    return redirect(
        "/accounts/projects/"
    )
    
def home_view(request):

    return render(
        request,
        "accounts/index.html"
    )
    
def students_view(request):

    profiles = Profile.objects.all()

    return render(
        request,
        "accounts/students.html",
        {
            "profiles": profiles
        }
    )
    
def student_profile(request, profile_id):

    profile = Profile.objects.get(
        id=profile_id
    )

    return render(
        request,
        "accounts/student_profile.html",
        {
            "profile": profile
        }
    )
    
def skills_view(request):

    profiles = Profile.objects.all()

    return render(
        request,
        "accounts/skills.html",
        {
            "profiles": profiles
        }
    )
    

def groups_view(request):

    groups = Group.objects.all()

    if request.user.is_authenticated:
        joined_groups = GroupMember.objects.filter(
        student=request.user
    ).values_list(
        "group_id",
        flat=True
    )
    
    else:
        joined_groups = []

    return render(
        request,
        "accounts/groups.html",
        {
            "groups": groups,
            "joined_groups": joined_groups
        }
    )
    
@login_required
def join_group(request, group_id):

    group = Group.objects.get(
        id=group_id
    )

    already_joined = GroupMember.objects.filter(
        group=group,
        student=request.user
    ).exists()

    if not already_joined:

        GroupMember.objects.create(
            group=group,
            student=request.user
        )

    return redirect("/accounts/groups/")

@login_required
def my_groups(request):

    groups = Group.objects.filter(
        groupmember__student=request.user
    )

    return render(
        request,
        "accounts/my_groups.html",
        {
            "groups": groups
        }
    )
    
@login_required
def leave_group(request, group_id):

    GroupMember.objects.filter(
        group_id=group_id,
        student=request.user
    ).delete()

    return redirect("/accounts/my-groups/")

def logout_view(request):

    logout(request)

    return redirect("/accounts/login/")

@login_required
def create_group(request):

    if request.method == "POST":

        name = request.POST["name"]
        description = request.POST["description"]

        Group.objects.create(
            name=name,
            description=description,
            created_by=request.user
        )

    return redirect("groups")

def project_detail(request, project_id):

    project = Project.objects.get(
        id=project_id
    )

    members = JoinRequest.objects.filter(
        project=project,
        status="Accepted"
    )

    return render(
        request,
        "accounts/project_detail.html",
        {
            "project": project,
            "members": members
        }
    )
    
def group_detail(request, group_id):

    group = Group.objects.get(
        id=group_id
    )

    members = GroupMember.objects.filter(
        group=group
    )

    return render(
        request,
        "accounts/group_detail.html",
        {
            "group": group,
            "members": members
        }
    )