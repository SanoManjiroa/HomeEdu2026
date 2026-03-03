from django.shortcuts import get_object_or_404, render
from .models import Course, CourseLesson

def course_list(request):
    courses = Course.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, course_id: int):
    course = get_object_or_404(Course, id=course_id, is_published=True)
    lessons = CourseLesson.objects.filter(course=course, is_published=True).order_by("order")
    return render(request, "courses/course_detail.html", {"course": course, "lessons": lessons})

def lesson_detail(request, lesson_id: int):
    lesson = get_object_or_404(CourseLesson, id=lesson_id, is_published=True, course__is_published=True)
    return render(request, "courses/lesson_detail.html", {"lesson": lesson})
