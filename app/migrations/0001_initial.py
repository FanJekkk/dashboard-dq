# Generated by Django 2.1.15 on 2020-10-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('err', models.IntegerField()),
            ],
            options={
                'db_table': 'subscribers',
            },
        ),
    ]
