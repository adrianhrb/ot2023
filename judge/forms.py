from django import forms


class JudgeIdentification(forms.Form):
    first_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
