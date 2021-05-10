from django import forms


class forms1(forms.Form):
    Name = forms.CharField(max_length=100)
    Email1 = forms.EmailField()
    suggestions = forms.CharField(widget=forms.Textarea)
