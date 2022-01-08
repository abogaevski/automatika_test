from django.core.validators import RegexValidator
from django.db import models


class Employee(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='Phone number must be entered in the format: '
                                         '\'+999999999\'. Up to 15 digits allowed.')

    name = models.CharField('Имя', max_length=128)
    phone = models.CharField('Телефон', validators=[phone_regex], max_length=17)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        db_table = 'employees'
