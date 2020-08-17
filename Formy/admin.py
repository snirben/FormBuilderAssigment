from django.contrib import admin

# Register your models here.
from Formy.models import Field, Form, FormAnswer, FormAnswerFieldData

admin.site.register(Form)
admin.site.register(Field)
admin.site.register(FormAnswer)
admin.site.register(FormAnswerFieldData)
