from django.http import HttpResponse


def notification_list(request):
    return HttpResponse('<h3>Notification list</h3>')
