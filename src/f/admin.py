from sharer.f.models import File
from django.contrib import admin

class FileAdmin(admin.ModelAdmin):
	pass
admin.site.register(File, FileAdmin)
