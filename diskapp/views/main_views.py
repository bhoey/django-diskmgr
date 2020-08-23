from django.http import HttpResponse
from diskapp.models import Disk, Host
from django.shortcuts import render


def index(request: HttpResponse):
    hosts = Host.objects.all()
    no_host_disks = Disk.objects.filter(host_id__isnull=True)

    context = {
        'hosts': hosts,
        'no_host_disks': no_host_disks,
    }

    return render(request, 'diskapp/index.html', context)


