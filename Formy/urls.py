from django.urls import path

from Formy import views

urlpatterns = [

    path('', views.home, name='home'),
    path('createform/', views.newFormPage, name='createform'),
    path('ajax/form_create/', views.newForm, name='createformajax'),
    path('ajax/form_submit/', views.submitForm, name='submitformajax'),
    path('form/<str:pk>', views.submitFormPage, name='form'),
    path('viewform/<str:pk>', views.submissionsForm, name='viewform'),
]
