from django import forms
from .models import Contact
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

class ContactForm(ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        return data
    def clean_email(self):
        data = self.cleaned_data['email']
        return data
    def clean_subject(self):
        data = self.cleaned_data['subject']
        return data
    def clean_message(self):
        data = self.cleaned_data['message']
        return data
    def clean_image(self):
        data = self.cleaned_data['image']
        return data
    def clean_send_email(self):
        data = self.cleaned_data['send_email']
        return data
    class Meta:
        model = Contact
        labels = {'image': _('Upload Image')}
        help_texts = {'image': _('Please upload only immage files')} 
        fields = '__all__'
    choice = [('Yes', 'Email Me A Copy of My Message')]
    #send_email = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, choices = choice, required= False)
    send_email = forms.BooleanField(required = False, label = 'Email Me A Copy of My Message')
