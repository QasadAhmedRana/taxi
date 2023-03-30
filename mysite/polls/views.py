from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Anfrage
from django.views import generic
from django.utils import timezone
from django.views import generic

#start pyrebase

#end pyrebase


from django.template import loader

# Create your views here.
#index has been replaced with homepage
"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
         """
    Return the last five published questions (not including those set to be
    published in the future).
    """
         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
   #this is causing errors when we click questions
    #queryset function causes problems
    #cannot find filter in function
    """def get_queryset(self):
    # Excludes any questions that aren't published yet.

        return Question.objects.all.filter(pub_date__lte=timezone.now())"""


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

# contact/views.py

class ContactView(FormView):
    template_name = 'polls/contact.html'
   # template_name = 'contact/send_mail.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


# contact/views.py
class ContactSuccessView(TemplateView):
    template_name = 'polls/success.html'

class InnerPageView(TemplateView):
    template_name = 'inner-page.html'

#Datenschutz view
def datenschutz(request):
    return render(request, 'polls/datenschutz.html')

def impressum(request):
    return render(request, 'polls/impressum.html')
