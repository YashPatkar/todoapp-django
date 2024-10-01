from django.shortcuts import render, redirect
from .models import Note
# Create your views here.
def home(request):
    notes = None
    if request.method == "POST":
        name = request.POST.get('name')
        note = request.POST.get('note')
        add_note = Note(name=name, note=note)
        add_note.save()
    notes = Note.objects.all()
    return render(request, "app1/home.html", {"notes": notes})


def delete_user(request, id):
    user = Note.objects.filter(id = id)
    user.delete()
    return redirect('home')
