from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


class Payments(models.Model):
    user = models.OneToOneField(
        User, related_name='payment', on_delete=models.CASCADE)
    payment_created = models.DateTimeField(auto_now_add=True, null=True)
    payment_success = models.CharField(max_length=20)
    session_id = models.CharField(max_length=100)
    currency = models.CharField(max_length=20)
    amount_total = models.IntegerField()
    payment_status = models.CharField(max_length=20)
