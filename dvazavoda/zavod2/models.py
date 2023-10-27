
from django.db import models
from django.urls import reverse


# Create your models here.
class Confectionery(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    availability = models.BooleanField(default=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse("zavod2:product_detailed", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title} - {self.price}$"
