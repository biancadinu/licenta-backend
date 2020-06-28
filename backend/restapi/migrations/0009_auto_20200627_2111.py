# Generated by Django 3.0.1 on 2020-06-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_auto_20200619_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=5048),
        ),
    ]
