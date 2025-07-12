from django.contrib import admin
from .models import Provinsi, Kabupaten, Kecamatan, Desa, DomainDesa

admin.site.register(Provinsi)
admin.site.register(Kabupaten)
admin.site.register(Kecamatan)
admin.site.register(Desa)
admin.site.register(DomainDesa)
