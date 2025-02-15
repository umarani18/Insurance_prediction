from django import forms

class InsuranceForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=18, max_value=100)
    sex = forms.ChoiceField(label='Sex', choices=[('male', 'Male'), ('female', 'Female')])
    bmi = forms.FloatField(label='BMI', min_value=10.0, max_value=50.0)
    children = forms.IntegerField(label='Number of Children', min_value=0, max_value=10)
    smoker = forms.ChoiceField(label='Smoker', choices=[('yes', 'Yes'), ('no', 'No')])
    region = forms.ChoiceField(label='Region', choices=[('northwest', 'Northwest'), ('northeast', 'Northeast'), ('southwest', 'Southwest'), ('southeast', 'Southeast')])
