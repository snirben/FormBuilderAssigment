from django.db import models

# Create your models here.



class Form(models.Model):
    formname = models.CharField(verbose_name="FormName:", max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

class Field(models.Model):

       form= models.ForeignKey(Form, verbose_name="Form",
                                   null=True, on_delete=models.CASCADE)
       label=models.CharField(verbose_name="Label",max_length=255,null=True)
       name = models.CharField(max_length=255,null=True)
       data_type= models.CharField(max_length=255, null=True)


class FormAnswer(models.Model):
    formanswer = models.ForeignKey(Form, on_delete=models.CASCADE)


class FormAnswerFieldData(models.Model):
    name = models.CharField(max_length=255, null=True)
    formanswer = models.ForeignKey(FormAnswer, on_delete=models.CASCADE)
    type=models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=4000, null=True)
