from django import forms
from .models import Addblog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2',)

    def __init__(self, *args, **kwargs):
        super(register_form,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
     
        self.fields['username'].widget.label =''






class Blog_Form(forms.ModelForm):
    class Meta:
        model = Addblog
        fields = ('author','image','body')
        widgets = {
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'body' :  forms.Textarea(attrs={'class':'form-control'})
        }
