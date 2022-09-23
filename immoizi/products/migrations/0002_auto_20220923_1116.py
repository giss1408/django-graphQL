# Generated by Django 3.2.15 on 2022-09-23 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='bailleur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.tenant'),
        ),
        migrations.AlterField(
            model_name='description',
            name='tenant',
            field=models.CharField(default='Anonyme', max_length=100),
        ),
    ]
