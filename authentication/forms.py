from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        required=True, widget=forms.PasswordInput())


class StageOneForm(forms.Form):
    about_me = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Tell Us About Your Self', 'class': 'form-control'}
    ))


class StageTwoForm(forms.Form):
    activation_code = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Activation Code', 'class': 'form-control'}
    ))


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter email address', 'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': '******', 'class': 'form-control'}))


