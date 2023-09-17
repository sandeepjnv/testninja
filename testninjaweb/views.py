from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict
from django.forms.models import model_to_dict

import json

from .models import Workflow

from .TestingEngine.engine import executeWorkflow

# Create your views here.
def index(request):
    return render(request = request, template_name ='testninjaweb/index.html')

# suite view
def suite(request):
    initialValues = getSuiteInitialValues()
    initialValues = json.dumps(initialValues)
    return render(request = request, template_name ='testninjaweb/suite.html',context= {'initialValues': initialValues})

# get all initial values
def getSuiteInitialValues():
    try:
        workflows = Workflow.objects.all()
        suitname_dict = defaultdict(list)
        for workflow in workflows:
            suitname_dict[workflow.suitName].append({"name":workflow.name,"id":workflow.pk})

        suitname_dict = dict(suitname_dict)
        return suitname_dict
    except Exception as e:
        return None

# run test
def runTest(request):
    try :
        if request.method == 'POST':
            workflow = json.loads(request.body)
            testCasesResult = executeWorkflow(workflow)
        return JsonResponse({'status':1,'message': '','result':testCasesResult})
    except Exception as e:
        print(e)
        return JsonResponse({'status':0,'message': 'Something went wrong'})

def saveTest(request):
    try :
        if request.method == 'POST':
            testDetails = json.loads(request.body)

            workflow = Workflow()
            if testDetails["operation"] == "UPDATE":
                workflow = Workflow.objects.get(id=testDetails["id"])
            
            workflow.name = testDetails["name"]
            workflow.suitName = "TRAACS"
            workflow.workflowconfig = testDetails["workflowconfig"]
            workflow.save()
        
        return JsonResponse({'status':1,'message': 'Test Saved Successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'status':0,'message': 'Something went wrong'})
    
def loadWorkflow(request):
    try :
        if request.method == 'POST':
            test = json.loads(request.body)
            workFlowDetails = model_to_dict(Workflow.objects.get(id=test["id"]))

            return JsonResponse({'status':1,'workflow': workFlowDetails})
    except Exception as e:
        print(e)
        return JsonResponse({'status':0,'message': 'Something went wrong'})