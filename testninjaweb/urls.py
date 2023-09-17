from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suite/',views.suite, name='suite'),
    path('runtest/',views.runTest,name="run test"),
    path('savetest/',views.saveTest,name='Save Test'),
    path('loadworkflow/',views.loadWorkflow,name='Load workflow')
]