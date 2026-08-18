

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def root_view(request):
    """
    Root URL:
    Logged-in user -> Home
    Anonymous user -> Login
    """

    if request.user.is_authenticated:
        return redirect('home')

    return redirect('login')


def login_view(request):

    # Already logged in
    if request.user.is_authenticated:
        return redirect('home')

    next_url = request.GET.get('next') or request.POST.get('next')

    form = LoginForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                if next_url:
                    return redirect(next_url)

                return redirect('home')

            form.add_error(
                None,
                'Invalid username or password.'
            )

    return render(
        request,
        'authentication/login.html',
        {
            'form': form,
            'next': next_url,
        }
    )


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = form.save()

            messages.success(
                request,
                'Account created successfully. Please login.'
            )

            return redirect('login')

    return render(
        request,
        'authentication/register.html',
        {
            'form': form,
        }
    )


@login_required
def logout_view(request):

    if request.method == 'POST':

        logout(request)

        return redirect('login')

    return render(
        request,
        'authentication/logout_confirm.html'
    )