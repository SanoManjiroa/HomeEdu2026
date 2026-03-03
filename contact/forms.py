from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            if hasattr(f.widget, 'attrs'):
                f.widget.attrs.setdefault('class', 'input')

    class Meta:
        model = ContactMessage
        fields = ["full_name", "phone", "email", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
