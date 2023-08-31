from django import forms
class regform(forms.Form):
    firstname=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
    confirmpassword=forms.CharField(max_length=30)
    email=forms.EmailField()
    number=forms.IntegerField()
    image=forms.FileField()
class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
class regformm(forms.Form):
    balance=forms.IntegerField()
    password=forms.CharField(max_length=30)
class newsform(forms.Form):
    topic=forms.CharField(max_length=300)
    content=forms.CharField(max_length=3000)
class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
class moneyform(forms.Form):
    acname=forms.CharField(max_length=30)
    accountnumber=forms.IntegerField()
    amount=forms.IntegerField()