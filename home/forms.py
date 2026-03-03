from django import forms
from .models import ContactMessage, Resume


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ismingiz", "class": "inp"}),
            "phone": forms.TextInput(attrs={"placeholder": "Telefon", "class": "inp"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email", "class": "inp"}),
            "message": forms.Textarea(attrs={"placeholder": "Xabar", "class": "inp", "rows": 4}),
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            "full_name", "phone", "email", "location",
            "profession", "skills", "experience",
            "portfolio_url", "cv_file", "is_public"
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "inp"}),
            "phone": forms.TextInput(attrs={"class": "inp"}),
            "email": forms.EmailInput(attrs={"class": "inp"}),
            "location": forms.TextInput(attrs={"class": "inp"}),
            "profession": forms.TextInput(attrs={"class": "inp"}),
            "skills": forms.Textarea(attrs={"class": "inp", "rows": 3}),
            "experience": forms.Textarea(attrs={"class": "inp", "rows": 3}),
            "portfolio_url": forms.URLInput(attrs={"class": "inp"}),
        }