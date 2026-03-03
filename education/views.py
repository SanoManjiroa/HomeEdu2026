from django.shortcuts import get_object_or_404, render
from .models import Grade, Subject, Topic

def grades_list(request):
    grades = Grade.objects.all()
    return render(request, "education/grades.html", {"grades": grades})

def subjects_by_grade(request, grade_id: int):
    grade = get_object_or_404(Grade, id=grade_id)
    subjects = Subject.objects.filter(grade=grade, is_published=True).order_by("name")
    return render(request, "education/subjects.html", {"grade": grade, "subjects": subjects})

def topics_by_subject(request, subject_id: int):
    subject = get_object_or_404(Subject, id=subject_id, is_published=True)
    topics = Topic.objects.filter(subject=subject, is_published=True).order_by("order", "title")
    return render(request, "education/topics.html", {"subject": subject, "topics": topics})

def topic_detail(request, topic_id: int):
    topic = get_object_or_404(Topic, id=topic_id, is_published=True)
    return render(request, "education/topic_detail.html", {"topic": topic})
