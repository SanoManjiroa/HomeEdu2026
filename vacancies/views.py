from django.shortcuts import get_object_or_404, render
from .models import Vacancy

def vacancy_list(request):
    q = request.GET.get("q", "").strip()
    items = Vacancy.objects.filter(is_active=True)
    if q:
        items = items.filter(title__icontains=q)
    items = items.order_by("-created_at")
    return render(request, "vacancies/vacancy_list.html", {"items": items, "q": q})

def vacancy_detail(request, vacancy_id: int):
    item = get_object_or_404(Vacancy, id=vacancy_id, is_active=True)
    return render(request, "vacancies/vacancy_detail.html", {"item": item})
