from django import forms

class PosterForm(forms.Form):
    company_name = forms.CharField(max_length=100, label="Company Name")
    price = forms.FloatField(label="Price")
    slogan = forms.CharField(max_length=200, label="Slogan")
    property_image = forms.ImageField(label="Property Image")
    feature1 = forms.CharField(max_length=50, label="Feature 1")
    feature1_image = forms.ImageField(label="Feature 1 Image")
    feature2 = forms.CharField(max_length=50, label="Feature 2")
    feature2_image = forms.ImageField(label="Feature 2 Image")
    feature3 = forms.CharField(max_length=50, label="Feature 3")
    feature3_image = forms.ImageField(label="Feature 3 Image")
    facilities = forms.CharField(widget=forms.Textarea, label="Facilities (comma-separated)")
    realtor_name = forms.CharField(max_length=100, label="Realtor Name")
    realtor_role = forms.CharField(max_length=50, label="Realtor Role")
    realtor_image = forms.ImageField(label="Realtor Image")
    contact_number = forms.CharField(max_length=15, label="Contact Number")
    contact_email = forms.EmailField(label="Contact Email")
    website = forms.URLField(label="Website")
