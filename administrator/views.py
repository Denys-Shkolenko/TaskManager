from django.http import HttpResponse


def user_list(request):
    return HttpResponse('<h3>User list</h3>')


def task_statistics(request):
    return HttpResponse('<h3>Task statistics</h3>')
