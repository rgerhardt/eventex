from django.db import models


class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


class PeriodQuerySet(models.QuerySet):
    NOON = '12:00'

    def at_morning(self):
        return self.filter(start__lt=self.NOON)

    def at_afternoon(self):
        return self.filter(start__gte=self.NOON)


PeriodManager = models.Manager.from_queryset(PeriodQuerySet)