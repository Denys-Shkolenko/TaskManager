from django.http import HttpResponse


def task_list(request):
    return HttpResponse('<h3>Task list</h3>')


def create_task(request):
    return HttpResponse('<h3>Create task</h3>')


def detail_task(request, task_id: int):
    return HttpResponse(f'<h3>Detail task #{task_id}</h3>')


def update_task(request, task_id: int):
    return HttpResponse(f'<h3>Update task #{task_id}</h3>')


def delete_task(request, task_id: int):
    return HttpResponse(f'<h3>Delete task #{task_id}</h3>')


def assign_task(request, task_id: int):
    return HttpResponse(f'<h3>Assign task #{task_id}</h3>')
