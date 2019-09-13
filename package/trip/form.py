from django import forms



class Reg(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=200)
    contact = forms.CharField(label="Enter Your Contact", max_length=200)
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    password = forms.CharField(label="Enter Your Password", max_length=200,widget=forms.PasswordInput)


class login(forms.Form):
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    password = forms.CharField(label="Enter Your password", max_length=200)