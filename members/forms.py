from django import forms
from .models import Contact, Member
from django.contrib.auth.forms import UserCreationForm
from .form_attrs import field_attrs
from django.utils.safestring import mark_safe

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 5}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'message': 'Your Message',
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('First name is required.')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('Last name is required.')
        return last_name

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field, attrs in field_attrs.items():
            if field in self.fields:
                self.fields[field].widget.attrs.update({
                    'placeholder': attrs['placeholder'],
                    'class': 'form-control form-control-lg',
                })
            self.fields[field].label = attrs['label']
            self.fields[field].label_suffix = ' *'
            self.fields[field].help_text = attrs['help_text']
            self.fields[field].error_messages = attrs['error_messages']

    def as_div(self):
        return mark_safe(
            '\n'.join(
                f'<div class="form-group mb-3">'
                f'{field.label_tag(attrs={"class": "form-label"})}{field}'
                f'{"".join(f"<div class=\"text-danger\">{error}</div>" for error in field.errors)}'
                f'</div>'
                if not field.is_hidden else str(field)
                for field in self
            )
        )