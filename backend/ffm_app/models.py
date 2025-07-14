from django.db import models
from django.conf import settings
from django.utils import timezone

class Property(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class CheckbookTransaction(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=[('debit','Debit'),('credit','Credit')])
    source = models.CharField(max_length=50, default='Manual')
    date = models.DateField(default=timezone.now)

class ClientKPISettings(models.Model):
    client = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_wo_stats = models.BooleanField(default=True)
    show_budget = models.BooleanField(default=True)
    show_pm_compliance = models.BooleanField(default=True)
    show_vendor_scores = models.BooleanField(default=True)

class CapitalExpenditureForecast(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2)
    projected_year = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class VendorPerformance(models.Model):
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    total_work_orders = models.PositiveIntegerField(default=0)
    on_time_completions = models.PositiveIntegerField(default=0)
    average_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    preferred = models.BooleanField(default=False)

class TenantTicket(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant_name = models.CharField(max_length=100)
    unit_number = models.CharField(max_length=50)
    issue_description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Open')
