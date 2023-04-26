from django.shortcuts import render, get_object_or_404, redirect
from .forms import PsyhologesForm
from .models import Psyhologes, Tests, Results


def index(request):
    form = PsyhologesForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        f = form.save(commit=False)
        f.save()
        if f.adult > 18:
            return redirect('psytests:adult_test')
        else:
            return redirect('psytests:child_test')
    return render(request, 'psytests/index.html', {'form': form})


def adult_test(request):
    return render(request, 'psytests/adult_test.html')


def child_test(request):
    return render(request, 'psytests/child_test.html')


def test():
    pass


def the_end(request):
    return render(request, 'psytests/the_end.html')

