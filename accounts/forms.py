from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    fullname = forms.CharField(max_length=255, label='Full Name')

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        user.fullname = self.cleaned_data['fullname']
        user.save()

        # You must return the original result.
        return user


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'fullname')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'fullname')
