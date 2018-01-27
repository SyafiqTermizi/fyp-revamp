from django import forms


class KeywordForm(forms.Form):

    keyword = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Keyword',
                'class':'form-control',
            }
        )
    )

    count = forms.IntegerField(
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Count',
                'class':'form-control',
            }
        )
    )


class UserForm(forms.Form):

    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Screen Name',
                'class':'form-control',
            }
        )
    )

    count = forms.IntegerField(
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Count',
                'class':'form-control',
            }
        )
    )
