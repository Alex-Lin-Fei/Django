from django import forms
from .models import UserInfo, Commodity, Order
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('user', )


class CommodityForm(forms.ModelForm):
    # picture = forms.ImageField()
    tag = forms.CharField()
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    numberOfComments = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Commodity
        exclude = ('owner', )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('number', 'address')
