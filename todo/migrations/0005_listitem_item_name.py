# Generated by Django 4.1 on 2022-10-03 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_list_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='item_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
