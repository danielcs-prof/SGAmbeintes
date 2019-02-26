from .models import *
from django import forms


class FormEmbedded(forms.ModelForm):

    class Meta:

        model = Embedded
        fields = ['hardware', 'firmware', 'location', 'state', 'mode', 'essid', 'ip', 'mac', 'mask', 'gateway']
        widget={
            'firmware': forms.FileInput(attrs={'class': 'custom-file-input'})
        }


class FormSensor(forms.ModelForm):

    class Meta:

        model = Sensor
        fields = ['description', 'rate', 'data']


class FormActuator(forms.ModelForm):

    class Meta:

        model = Actuator
        fields = ['description', 'command']