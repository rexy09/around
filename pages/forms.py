from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Your email'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message','rows':'4'}), required=True)