from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=128)
    sex = forms.ChoiceField(label='sex', choices=Student.SEX_ITEMS)
    profession = forms.CharField(label='profession', max_length=128)
    email = forms.CharField(label='e-mail', max_length=128)
    qq = forms.CharField(label='QQ', max_length=128)
    phone = forms.CharField(label='telephone', max_length=128)

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('must be digit')
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )