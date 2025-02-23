from django.shortcuts import render
from .forms import RatingForm


def index(request):
    if request.method == "POST":
        form = RatingForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            return render(request, "index.html", {"form": form})
    form = RatingForm()
    context = {"form": form}
    return render(request, "index.html", context)
