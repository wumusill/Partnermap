from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import *


# 총학생회
class PartnerAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Partner, PartnerAdmin)


# 인문대학 학생회
class PartnerHumanityAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(PartnerHumanity, PartnerHumanityAdmin)


# 경영대학 학생회
class PartnerBusinessAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(PartnerBusiness, PartnerBusinessAdmin)


admin.site.register(PartnerSociety)
admin.site.register(PartnerScience)
admin.site.register(PartnerEngine)
admin.site.register(PartnerElec)
admin.site.register(PartnerFarm)
admin.site.register(PartnerTeacher)
admin.site.register(PartnerLife)
admin.site.register(PartnerVet)
admin.site.register(PartnerMedicine)
admin.site.register(PartnerDoctor)
admin.site.register(PartnerMixed)
