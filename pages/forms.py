from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder':'Your name'}))
    from_email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))   
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Message','rows':'4'}), required=True)