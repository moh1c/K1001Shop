# Generated by Django 3.2.7 on 2021-09-20 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_auto_20210917_1534'),
        ('store', '0003_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='subregion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cities_light.subregion'),
        ),
    ]
