from django.http import HttpResponse


def login_user(request):
    return HttpResponse('<h3>Login</h3>')


def logout_user(request):
    return HttpResponse('<h3>Logout</h3>')


def register_user(request):
    return HttpResponse('<h3>Register</h3>')


def profile_user(request):
    return HttpResponse('<h3>Profile</h3>')
