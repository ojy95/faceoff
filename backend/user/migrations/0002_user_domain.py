# Generated by Django 3.1.2 on 2020-11-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='domain',
            field=models.CharField(blank=True, db_column='DOMAIN', max_length=20, null=True),
        ),
    ]