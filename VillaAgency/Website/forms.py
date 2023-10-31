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

class MessageForm(forms.Form):
    name = forms.CharField(
        label='Full Name:',
        max_length=100,
        widget=forms.Input(
            attrs={
                'type': 'name',
                'name': 'name',
                'id': 'name',
                'autocomplete': 'on',
                'required':'',
                'placeholder': 'Your Name...',
            }
        )
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
        max_length=100,
        widget=forms.Input(
            attrs={
                'type': 'subject',
                'name': 'subject',
                'id': 'subject',
                'autocomplete': 'on',
                'placeholder': 'Subject...',
            }
        )
    )
    message = forms.TextField(
        label='Subject:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'name': 'message',
                'id': 'message',
                'placeholder': 'Your Message...',
            }
        )
    )