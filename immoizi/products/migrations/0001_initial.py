# Generated by Django 3.2.15 on 2022-09-23 10:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPrenoms', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=13)),
                ('quantity', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=13)),
                ('pieces', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_toEnter', models.DateField(default=datetime.date.today)),
                ('imageurl', models.URLField()),
                ('product_tag', models.CharField(max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='products.category')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='products.tenant')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]