import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from Formy.models import Form, Field, FormAnswer, FormAnswerFieldData


def home(request):
    forms = Form.objects.all()
    return render(request, "Formy/FormList.html", {"forms": forms})


def newFormPage(request):
    return render(request, "Formy/NewForm.html", {})


def newForm(request):
    try:
     data = json.loads(request.GET.get('data'))

     form = Form(formname=data["form_name"])
     form.save()

     for field_ in data["fields"]:
        field = Field(form=form, label=field_["fieldlabel"], name=field_["inputname"], data_type=field_["type"])
        field.save()
    except :
     return JsonResponse({'hogback': "fail"}, status=200, content_type="application/json")
    return JsonResponse({'hogback': "ok"}, status=200, content_type="application/json")


def submitFormPage(request, pk):
    form = Form.objects.get(id=pk)
    fields = Field.objects.filter(form=form)
    return render(request, "formy/SubmitForm.html", {"fields": fields, "form": form})


def submitForm(request):
  try:
    data = json.loads(request.POST.get('data'))

    form = Form.objects.get(id=data['formid'])
    formanswer = FormAnswer(formanswer=form)
    formanswer.save()
    del data["input"][0] ##delete the CSRF Token
    for answer_ in data["input"]:
        answer = FormAnswerFieldData(formanswer=formanswer,name=answer_['name'], type=answer_['type'], value=answer_["input"])
        answer.save()
  except:
    return JsonResponse({'hogback': "fail"}, status=200, content_type="application/json")
  return JsonResponse({'hogback': "ok"}, status=200, content_type="application/json")


def submissionsForm(request, pk):
    form = Form.objects.get(id=pk)
    titles=Field.objects.filter(form=form)
    answerslug = FormAnswer.objects.filter(formanswer=form)
    answers=[]
    for answer in answerslug:
        answers.append([FormAnswerFieldData.objects.filter(formanswer=answer)])
    print(answers)
    return render(request, "formy/ViewForm.html", {"answers": answers,"titles":titles, "form": form})
