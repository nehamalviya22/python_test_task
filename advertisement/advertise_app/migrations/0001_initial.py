# Generated by Django 3.2.9 on 2021-12-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sdkversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdkversion', models.CharField(max_length=100)),
                ('ad_count', models.IntegerField(default=0)),
                ('impression_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('ad_count', models.IntegerField(default=0)),
                ('impression_count', models.IntegerField(default=0)),
            ],
        ),
    ]
