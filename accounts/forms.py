from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
