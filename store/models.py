from django.db import models

from employee.models import Employee


class Store(models.Model):
    title = models.CharField('Название', max_length=255)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='store')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
        db_table = 'stores'


class Visit(models.Model):
    date = models.DateField('Дата посещения', auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='visits')
    latitude = models.DecimalField('Широта', max_digits=9, decimal_places=6)
    longitude = models.DecimalField('Долгота', max_digits=9, decimal_places=6)

    def __str__(self):
        return '{}: {} - {}'.format(self.date, self.latitude, self.longitude)

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
        db_table = 'visits'
