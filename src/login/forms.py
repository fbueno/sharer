from django import forms

class LoginForm(forms.Form):
        username = forms.CharField(label='Email', max_length=30, required=True)
        password = forms.CharField(label='Password',max_length=30,widget=forms.PasswordInput(),required=True)

