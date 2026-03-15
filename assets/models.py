from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = [
    ('open', 'Open'),
    ('progress', 'In Progress'),
    ('resolved', 'Resolved')
]

class Asset(models.Model):

    serial_number = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    computer_type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)
    opco_asset_tag = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)
    column1 = models.CharField(max_length=100, blank=True, null=True)
    column2 = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    def __str__(self):
        return self.opco_asset_tag


class Assignment(models.Model):

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    assigned_to = models.CharField(max_length=100, blank=True, null=True)

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    comments = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset} -> {self.assigned_to}"

class Comment(models.Model):

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)