from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    LEASEDLINE = 1
    IBW = 2
    FXL = 3
    SERVICE_TYPES = (
        (LEASEDLINE, 'Leased Line'),
        (IBW, 'IBW'),
        (FXL, 'Fixed Line'),
    )
    name = models.CharField(max_length=50)
    installation_date = models.DateField(blank=True, null=True)
    account_manager = models.CharField(max_length=30, blank=True)
    monthly_charge = models.DecimalField(max_digits=7, decimal_places=2)
    capacity = models.IntegerField(blank=True, null=True)
    service_type = models.PositiveSmallIntegerField(choices=SERVICE_TYPES, blank=True, null=True)
