from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordResetForm,
    UsernameField
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string

from .tasks import send_email_password_reset


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        required=True,
        widget=forms.TextInput(attrs={"autofocus": True}),
    )
    password = forms.CharField(
        label="Пароль",
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    def clean(self):
        data = self.cleaned_data
        username = data.get("username")
        password = data.get("password")

        if not username:
            raise ValidationError("Введите логин.")

        if not password:
            raise ValidationError("Введите пароль.")

        try:
            user = User.objects.get(username=username)
            if not user.is_active:
                raise ValidationError("Аккаунт требует активации.")

            if not user.check_password(password):
                raise ValidationError(
                    "Логин или пароль введен неправильно."
                )
        except User.DoesNotExist:
            raise ValidationError(
                "Логин или пароль введен неправильно."
            )
        return data


class CustomPasswordResetForm(PasswordResetForm):
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        message = render_to_string(email_template_name, context)
        send_email_password_reset(to_email, message)


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                'autofocus'] = True

