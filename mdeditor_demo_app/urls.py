from django.conf.urls import url
from django.views.generic import TemplateView
from .views import mdeditor_form_view, mdeditor_model_form_view

urlpatterns = [
    url(r'^$', mdeditor_form_view, name='mdeditor-form'),
    url(r'^model/$', mdeditor_model_form_view, name='mdeditor-model-form'),
]
