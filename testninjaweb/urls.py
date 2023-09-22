from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suite/',views.suite, name='suite'),
    path('runtest/',views.runTest,name="run test"),
    path('savetest/',views.saveTest,name='Save Test'),
    path('deletetest/',views.deleteTest,name="Delete workflow"),
    path('loadworkflow/',views.loadWorkflow,name='Load workflow'),
    path('loadsuiteslist/',views.loadAllSuitesAndTest,name="Load all suites and its tests")
]