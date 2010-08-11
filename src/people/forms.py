from django import forms

class RegForm(forms.Form):
        password = forms.CharField(label='Sua nova senha', max_length=30,widget=forms.PasswordInput(),required=True)

class EmailForm(forms.Form):
        email = forms.EmailField()
