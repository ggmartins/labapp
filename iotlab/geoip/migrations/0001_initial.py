# Generated by Django 3.0.2 on 2020-01-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=46, unique=True)),
                ('is_ipv4', models.BooleanField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('datecached', models.DateTimeField()),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('org', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('ASorg', models.CharField(max_length=100)),
                ('hits', models.IntegerField()),
            ],
        ),
    ]
