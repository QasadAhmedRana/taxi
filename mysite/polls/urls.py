from django.urls import path
from . import views
from .views import ContactSuccessView, ContactView


app_name = 'polls'
urlpatterns = [
    #ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('inner-page/', views.InnerPageView.as_view(), name="inner-page"),
    #path('datenschutz/', DatenschutzView.as_view(), name='datenschutz'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),


]