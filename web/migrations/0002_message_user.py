# Generated by Django 4.1.1 on 2022-09-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.TextField()),
                ('payee', models.TextField()),
                ('sigma', models.TextField()),
                ('msg', models.TextField()),
            ],
            options={
                'db_table': 'Message',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('money', models.TextField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
