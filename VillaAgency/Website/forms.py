from django import forms

class LoginForms(forms.Form):
    email=forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: daviv01@gmail.com',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class MessageForms(forms.Form):
    name = forms.CharField(
        label='Full Name:',
        max_length=100
    )
    email= forms.EmailField(
        label='Email Address:', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'name': 'email',
                'id': 'email',
                'autocomplete': 'on',
                'pattern':'[^ @]*@[^ @]*',
                'required':'',
                'placeholder': 'Your E-mail...',
            }
        )
    )
    subject = forms.CharField(
        label='Subject:',
        max_length=100
    )
    message = forms.CharField(
        label='Subject:',
        max_length=100
    )