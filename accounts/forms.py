from allauth.account.forms import SignupForm
from django import forms


class MyCustomSignupForm(SignupForm):
    name = forms.CharField()
    last_name = forms.CharField()

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
