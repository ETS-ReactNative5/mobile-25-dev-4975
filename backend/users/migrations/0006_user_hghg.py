# Generated by Django 2.2.12 on 2020-05-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_hghg'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hghg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
