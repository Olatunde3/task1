# Generated by Django 4.2.4 on 2023-09-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=50)),
                ('day_week', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('track', models.CharField(max_length=50)),
                ('github_url', models.CharField(max_length=150)),
                ('source_code', models.CharField(max_length=150)),
            ],
        ),
    ]
