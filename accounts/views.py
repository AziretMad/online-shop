from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    PasswordResetView, PasswordContextMixin, PasswordResetConfirmView
)
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView, TemplateView

from .forms import SignupForm, SignInForm, CustomPasswordResetForm
from .tasks import send_email_account_activation
from .tokens import account_activation_token


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Активируйте ваш аккаунт'
        message = render_to_string(
            'accounts/active_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
        )
        to_email = form.cleaned_data.get('email')
        send_email_account_activation(to_email, message)
        return HttpResponseRedirect(reverse('accounts:activation_info'))


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('accounts:activation_done'))
    else:
        return HttpResponse('Сылка для подтверждения не рабочая!')


class SignInView(FormView):
    form_class = SignInForm
    template_name = 'accounts/signin.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(reverse('/:index'))
            else:
                return HttpResponseRedirect(
                    reverse('accounts:activation_info')
                )
        return HttpResponseRedirect(reverse('accounts:activation_info'))


def _logout(request):
    logout(request)
    return redirect("/:index")


class ActivationInfoView(TemplateView):
    template_name = 'accounts/activation_info.html'


class ActivationDoneView(TemplateView):
    template_name = 'accounts/activation_done.html'


class InvalidLinkView(TemplateView):
    template_name = 'accounts/invalid_link.html'
