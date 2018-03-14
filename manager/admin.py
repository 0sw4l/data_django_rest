# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'datos', 'creado']


admin.site.index_title = 'Data'
admin.site.site_title = 'Data'
admin.site.site_header = 'Data'
admin.site.name = 'Data'
