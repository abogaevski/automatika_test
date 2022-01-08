# Generated by Django 4.0.1 on 2022-01-08 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='employee.employee')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
                'db_table': 'stores',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата посещения')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='store.store')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещения',
                'db_table': 'visits',
            },
        ),
    ]