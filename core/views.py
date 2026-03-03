from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from courses.models import Course
from vacancies.models import Vacancy
from parents_content.models import ParentContent
from education.models import Subject

@login_required
def dashboard(request):
    user = request.user
    context = {"user": user}
    # recommended content
    context["top_courses"] = Course.objects.filter(is_published=True).order_by("-created_at")[:4]
    context["top_vacancies"] = Vacancy.objects.filter(is_active=True).order_by("-created_at")[:4]
    if user.role == "student" and user.grade_id:
        context["subjects"] = Subject.objects.filter(grade=user.grade, is_published=True).order_by("name")[:10]
    if user.role == "parent":
        context["parent_items"] = ParentContent.objects.filter(is_published=True).order_by("-created_at")[:6]
    return render(request, "dashboard/dashboard.html", context)
