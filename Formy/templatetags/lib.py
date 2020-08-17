from django import template

from Formy.models import FormAnswer

register = template.Library()
@register.filter
def form_sumbitcount(id):
    arg=FormAnswer.objects.all().filter(formanswer=id)
    return arg.count()