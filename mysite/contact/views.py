from django.core.mail import EmailMessage
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
#from .forms import SendMailForm
# contact/views.py
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from .models import  Anfrage
from django.urls import reverse_lazy

# contact/views.py

class ContactView(FormView):
    template_name = 'contact/contact.html'
   # template_name = 'contact/send_mail.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


# contact/views.py
class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'



