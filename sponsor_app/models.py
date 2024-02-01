from django.db.models import *
from django.contrib.auth import get_user_model


User = get_user_model()


class Sponsor(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    full_name = CharField(max_length=256)
    phone = CharField(max_length=13)
    pay_fund = FloatField()

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


class PhysicalSponsor(Sponsor):

    class Meta:
        verbose_name = "Physical Sponsor"
        verbose_name_plural = "Physical Sponsors"
        db_table = "sponsors"


class LegalSponsor(Sponsor):
    organization_name = CharField(max_length=256)

    def __str__(self):
        return f"{self.organization_name} | {self.full_name}"

    class Meta:
        verbose_name = "Legal Sponsor"
        verbose_name_plural = "Legal Sponsors"
        db_table = "legal_sponsors"
