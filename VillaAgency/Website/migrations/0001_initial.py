# Generated by Django 4.2.6 on 2023-10-31 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imoveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=200)),
                ('status', models.CharField(choices=[('DISPONÍVEL', 'Disponível'), ('VENDIDO', 'Vendido')], default='', max_length=100)),
                ('area', models.IntegerField(default=0, max_length=4)),
                ('bedrooms', models.IntegerField(default=0, max_length=4)),
                ('bathrooms', models.IntegerField(default=0, max_length=4)),
                ('floor', models.IntegerField(default=0, max_length=4)),
                ('parking', models.IntegerField(default=0, max_length=4)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo', models.CharField(choices=[('APARTMENT', 'Apartment'), ('VILLA HOUSE', 'Villa House'), ('PENTHOUSE', 'Penthouse')], default='', max_length=100)),
                ('path', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(default='', max_length=255)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
