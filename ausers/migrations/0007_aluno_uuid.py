# Generated by Django 3.0.4 on 2020-07-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausers', '0006_auto_20200601_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='uuid',
            field=models.UUIDField(editable=False, null=True, unique=True),
        ),
    ]
