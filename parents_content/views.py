from django.shortcuts import get_object_or_404, render
from .models import ParentContent

def parent_list(request):
    items = ParentContent.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "parents/parent_list.html", {"items": items})

def parent_detail(request, item_id: int):
    item = get_object_or_404(ParentContent, id=item_id, is_published=True)
    return render(request, "parents/parent_detail.html", {"item": item})
