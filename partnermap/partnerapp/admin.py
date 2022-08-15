from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)