from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactInfo
from .forms import ContactMessageForm

def contact_page(request):
    info = ContactInfo.objects.first()
    form = ContactMessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Xabaringiz yuborildi. Tez orada bog‘lanamiz.")
        return redirect("contact:contact")
    return render(request, "contact/contact.html", {"info": info, "form": form})
