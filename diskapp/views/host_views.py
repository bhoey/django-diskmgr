from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from diskapp.forms import HostForm
from diskapp.models import Host, Disk

# Function-based Views Example

def host_add(request: HttpResponse):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, "diskapp/host_form.html", {'host_form': form})
    else:
        form = HostForm()

    context = {
        'form': form,
    }

    return render(request, "diskapp/host_form.html", context)


def host_delete(request: HttpResponse, pk: int):

    host = get_object_or_404(Host, pk=pk)
    delete_disks = request.POST.get('delete_disks', '') == 'yes'

    if request.method == 'POST':
        disks = Disk.objects.filter(host=host.pk)
        for disk in disks:
            if delete_disks:
                disk.delete()
            else:
                disk.host = None
                disk.save()
        host.delete()
        return redirect('index')

    else:
        form = HostForm(instance=host)

    return render(request, 'diskapp/host_confirm_delete.html', {'host': host, 'form': form})


def host_update(request: HttpResponse, pk: int):

    host = get_object_or_404(Host, pk=pk)

    if request.method == 'POST':
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'diskapp/host_form.html', {'form': form})

    else:
        form = HostForm(instance=host)

    return render(request, 'diskapp/host_form.html', {'form': form})
