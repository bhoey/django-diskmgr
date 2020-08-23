from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.forms import ModelForm
from django.urls import reverse
from diskapp.models import Host


class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = ['name',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.add_input(Button('cancel',
                                     'Cancel',
                                     css_class='btn-primary',
                                     onclick=f"window.location.href='{reverse('index')}';"))
