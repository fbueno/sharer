from django import forms

class UploadForm(forms.Form):
        f = forms.FileField('File')
