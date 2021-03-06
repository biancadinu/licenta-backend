# Generated by Django 3.0.6 on 2020-06-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20200602_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calcium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='cholesterol',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fiber',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='saturated_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='sodium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='sugars',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='total_carbs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='total_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='trans_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vitamin_a',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='vitamin_c',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
