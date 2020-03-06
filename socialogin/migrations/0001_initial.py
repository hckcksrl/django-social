# Generated by Django 3.0.3 on 2020-03-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default=None, max_length=255)),
                ('username', models.CharField(default=None, max_length=255)),
                ('access_token', models.CharField(default=None, max_length=255)),
                ('refresh_token', models.CharField(default=None, max_length=255)),
                ('social_id', models.IntegerField()),
                ('social_site', models.CharField(blank=True, choices=[('kakao', 'kakao'), ('facebook', 'facebook')], max_length=255, null=True)),
            ],
        ),
    ]
