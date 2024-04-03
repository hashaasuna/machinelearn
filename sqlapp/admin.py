from typing import Any
from django.contrib import admin
from django.db.models.fields.related import RelatedField
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . models import Psterminalinfo
from . import models
# Register your models here.

@admin.register(Psterminalinfo)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('cpnyid','perioddate','terminalid')
    list_filter = ('terminalid', 'perioddate')
    
admin.site.register(models.Pssales)
admin.site.register(models.Pssalesitem)
