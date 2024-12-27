from django.db import models


# Models
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_old_price = models.FloatField(null=True, blank=True)
    product_image = models.URLField()
    product_discount = models.FloatField()
    product_rating = models.FloatField()
    product_description = models.TextField()
    product_is_liked = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.product_name


class Offer(models.Model):
    hours = models.CharField(max_length=2)  # e.g., "01"
    minutes = models.CharField(max_length=2)  # e.g., "30"
    seconds = models.CharField(max_length=2)  # e.g., "45"
    description_text = models.TextField()  # Description of the offer
    image_name = models.CharField(max_length=255)  # Name of the image file
    percent = models.CharField(max_length=3)  # Discount percentage, e.g., "25%"
    countdown = models.IntegerField()  # Countdown in seconds

    def __str__(self):
        return self.description_text
