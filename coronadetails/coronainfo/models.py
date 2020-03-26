from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

# Create your models here.
# WorldWide
class WorldWide(models.Model):
    total = models.CharField(max_length = 33)
    deaths = models.CharField(max_length=33)
    recovered = models.CharField(max_length=33)

    class Meta:
        verbose_name_plural = "WorldWide"
        db_table = "worldwide"

    def __str__(self):
        return self.total

    # def get_absolute_url(self):
    #     return reverse('schedule:edit', kwargs={'pk': self.pk})
    def __str__(self):
        return '{} - {}'.format(self.total, self.deaths)


#CaseswithDate
class CaseswithDate(models.Model):
    date = models.DateField()
    total = models.CharField(max_length=33)
    deaths = models.CharField(max_length=33)
    recovered = models.CharField(max_length=33)

    class Meta:
        verbose_name_plural = "Cases as a Date"
        db_table = "casesdate"

    def __str__(self):
        return self.total

    def get_absolute_url(self):
        return reverse('schedule:edit', kwargs={'pk': self.pk})

#Country Corona
class CasesCountry(models.Model):
    total = models.CharField(max_length=33)
    deaths = models.CharField(max_length=33)
    recovered = models.CharField(max_length=33)
    country = CountryField()

    class Meta:
        verbose_name_plural = "Total(Country)"
        db_table = "casescountry"

    def __str__(self):
        return self.total

    def get_absolute_url(self):
        return reverse('schedule:edit', kwargs={'pk': self.pk})