from django import forms

class CommentForm(forms.Form):
    your_name = forms.CharField(label='Ваше имя', max_length=100, required = True,widget = forms.TextInput(attrs = {
        'class': 'form-control',}))
    your_email = forms.EmailField(label='Ваш email', max_length=100, required = True,widget = forms.TextInput(attrs = {
        'class': 'form-control',}))
    your_message = forms.CharField(label='Ваше сообщение', max_length=300, required = True,widget = forms.Textarea(attrs = {
        'class': 'form-control',}))


