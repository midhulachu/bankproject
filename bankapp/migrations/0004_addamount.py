# Generated by Django 4.2.2 on 2023-07-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_regmodel_accountnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='addamount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
