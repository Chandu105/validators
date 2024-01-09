from django import forms

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')
def validate_len(data):
    if len(data)<4:
        raise forms.ValidationError('len is less than 4')


class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_a,validate_len])
    Slocation=forms.CharField(validators=[validate_for_a])
    Sprincipal=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['renteremail']

        if e!=r:
            raise forms.ValidationError('emails are not matched')
