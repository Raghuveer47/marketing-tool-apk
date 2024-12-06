from django.db import models

class Poster(models.Model):
    company_name = models.CharField(max_length=100)
    price = models.FloatField()
    slogan = models.CharField(max_length=200)
    property_image = models.ImageField(upload_to='property_images/')
    feature1 = models.CharField(max_length=50)
    feature1_image = models.ImageField(upload_to='feature_images/')
    feature2 = models.CharField(max_length=50)
    feature2_image = models.ImageField(upload_to='feature_images/')
    feature3 = models.CharField(max_length=50)
    feature3_image = models.ImageField(upload_to='feature_images/')
    facilities = models.TextField()  # Store facilities as a comma-separated string
    realtor_name = models.CharField(max_length=100)
    realtor_role = models.CharField(max_length=50)
    realtor_image = models.ImageField(upload_to='realtor_images/')
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField()
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
