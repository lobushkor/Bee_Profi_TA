from django import forms
from . import models


class TourRequestForm(forms.ModelForm):
    class Meta:
        model = models.TourRequest
        fields = ['country', 'hotel', 'nights', 'pax', 'child', 'client_text']
        labels = {
            'country': 'Країна',
            'hotel': 'Готель',
            'nights': 'Кількісьть ночей',
            'pax': 'Кількість дорослих',
            'child': 'Кількість дітей',
            'client_text': 'Додаткова інформація',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TourRequestForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(TourRequestForm, self).save(commit=False)
        instance.user = self.request.user
        if commit:
            instance.save()
        return instance



