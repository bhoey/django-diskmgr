from django.contrib import admin
from diskapp.models import Disk, Host


class HostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class DiskAdmin(admin.ModelAdmin):
    list_display = ('serial_no', 'size_gb', 'host', 'interface', 'purpose')
    list_filter = ('interface',)
    ordering = ('size_gb', 'serial_no')


admin.site.register(Host, HostAdmin)
admin.site.register(Disk, DiskAdmin)

