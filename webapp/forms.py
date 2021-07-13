from django.forms import ModelForm, FileInput
from django import forms
from django.contrib.auth import get_user_model

from webapp.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'image': FileInput(attrs={'type': 'image'})
        }


non_allowed_usernames = ['abc']
# check for unique email & username

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "user-name",
                "required": 1,
                # "placeholder": "Usuario"
            }

        ))
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "user-email",
                "required": 1,
                # "placeholder": "Correo electrónico"
            }
        ))
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "required": 1,
                # "placeholder": "Contraseña"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password",
                "required": 1,
                # "placeholder": "Confirmar Contraseña"
            }
        )
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas son distintas.")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "user-name",
            "required": 1,
            "autofocus": 1,
            # "placeholder": "Nombre de usuario"
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password",
                "required": 1,
                # "placeholder": "Contraseña"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)  # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username
