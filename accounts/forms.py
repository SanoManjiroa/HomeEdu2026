from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            if hasattr(f.widget, 'attrs'):
                f.widget.attrs.setdefault('class', 'input')

    password1 = forms.CharField(widget=forms.PasswordInput, label="Parol")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Parolni tasdiqlang")

    class Meta:
        model = User
        fields = ["email", "full_name", "age", "phone", "role", "grade"]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Parollar mos kelmadi")
        role = cleaned.get("role")
        grade = cleaned.get("grade")
        if role == "student" and not grade:
            self.add_error("grade", "Student uchun sinf tanlang")
        if role == "parent":
            cleaned["grade"] = None
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            if hasattr(f.widget, 'attrs'):
                f.widget.attrs.setdefault('class', 'input')

    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Parol")

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            if hasattr(f.widget, 'attrs'):
                f.widget.attrs.setdefault('class', 'input')

    class Meta:
        model = User
        fields = ["full_name", "age", "phone", "role", "grade", "avatar"]

    def clean(self):
        cleaned = super().clean()
        role = cleaned.get("role")
        grade = cleaned.get("grade")
        if role == "student" and not grade:
            self.add_error("grade", "Student uchun sinf tanlang")
        if role == "parent":
            cleaned["grade"] = None
        return cleaned
