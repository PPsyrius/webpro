# Generated by Django 3.1.4 on 2020-12-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('m_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('m_name', models.CharField(max_length=50, unique=True)),
                ('m_health', models.PositiveIntegerField()),
                ('m_image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WordBank',
            fields=[
                ('wb_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('wb_list', models.CharField(max_length=10000)),
            ],
        ),
    ]
