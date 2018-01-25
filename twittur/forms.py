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

    count = forms.CharField(
        max_length=200,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Count',
                'class':'form-control',
            }
        )
    )
