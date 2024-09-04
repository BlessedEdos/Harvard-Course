# from django import forms
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse


# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="New Task")
#     # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# # Create your views here.
# def index(request):
#     if "task" not in request.session:
#         request.session["tasks"] = []

#     return render(request, "tasks/index.html", {
#         "tasks": request.session["tasks"]
#     })

# def add(request):
#     if request.method == "POST":
#         form = NewTaskForm(request.POST)
#         if form.is_valid():
#             task = form.cleaned_data["task"]
#             # request.session["tasks"] += [task]
#             request.session["tasks"].append(task)
#             return HttpResponseRedirect(reverse("tasks:index"))
#         else:
#             return render(request, "tasks/add.html", {
#                 "form": form
#             })
#     return render(request, "tasks/add.html", {
#         "form": NewTaskForm()
#     })





from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    # Get the tasks from the session, or initialize an empty list if it doesn't exist
    tasks = request.session.get('tasks', [])
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # Get the current tasks from the session, or initialize an empty list
            tasks = request.session.get('tasks', [])
            # Append the new task
            tasks.append(task)
            # Save the updated tasks list back to the session
            request.session['tasks'] = tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
