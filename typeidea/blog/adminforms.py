from django import forms


class PostAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=forms.Textarea, label='abstract', required=False)