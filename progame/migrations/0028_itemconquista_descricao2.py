# Generated by Django 3.0.4 on 2020-07-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progame', '0027_auto_20200718_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemconquista',
            name='descricao2',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
