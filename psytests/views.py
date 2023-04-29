from django.shortcuts import render, get_object_or_404, redirect
from .forms import PsyhologesForm
from .models import Psyhologes, Tests, Questions, Answers, Results


def index(request):
    form = PsyhologesForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        f = form.save(commit=False)
        f.save()
        if f.old > 18:
            return redirect('psytests:adult_test')
        else:
            return redirect('psytests:child_test')
    return render(request, 'psytests/index.html', {'form': form})


def adult_test(request):
    tests = Tests.objects.filter(adult='after 18')
    context = {
        'tests': tests,
    }
    return render(request, 'psytests/adult_test.html', context)


def child_test(request):
    tests = Tests.objects.filter(adult='before 18')
    context = {
        'tests': tests,
    }
    return render(request, 'psytests/child_test.html', context)


def test(request, test_id):
    psyh = Psyhologes.objects.latest('name')
    tests = Tests.objects.get(pk=test_id)
    answers = Answers.objects.filter(test=test_id)
    questions = Questions.objects.filter(test=test_id)
    context = {
        'tests': tests,
        'answers': answers,
        'questions': questions,
    }
    print('1')
    if request.method == 'POST':
        print('2')
        for i in range(0, len(questions)):
            print('3')
            answer = request.POST.get[f'answer{i}']
            question = Questions.objects.get(pk=i)
            print(answer, question)
            Results.objects.create(psyholog=psyh, test=tests, question=question, answer=answer).save()
        return redirect('psytests:the_end')
    return render(request, 'psytests/test.html', context)


def the_end(request):
    return render(request, 'psytests/the_end.html')

