from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from diskapp.models import Disk

# Class-based Views Example

class DiskCreate(CreateView):
    model = Disk
    fields = ['serial_no', 'size_gb', 'interface', 'purpose', 'host']
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Add', css_class='btn-primary'))
        form.helper.add_input(Button('cancel',
                                     'Cancel',
                                     css_class='btn-secondary',
                                     onclick=f"window.location.href='{reverse('index')}';"))
        return form


class DiskDelete(DeleteView):
    model = Disk
    success_url = reverse_lazy('index')


class DiskUpdate(UpdateView):
    model = Disk
    fields = ['serial_no', 'size_gb', 'interface', 'purpose', 'host']
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Update', css_class='btn-primary'))
        form.helper.add_input(Button('cancel',
                                     'Cancel',
                                     css_class='btn-secondary',
                                     onclick=f"window.location.href='{reverse('index')}';"))
        return form

