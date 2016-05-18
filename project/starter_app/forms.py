from django import forms


class CreateNewPost(forms.Form):
	title = forms.CharField(max_length=50, required=True)
	slug = forms.SlugField(required=False)
	date_of_createion = forms.DateTimeField(required=False)
	content = forms.CharField(required=True, widget=forms.Textarea)
