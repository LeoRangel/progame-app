# Generated by Django 3.0.4 on 2020-04-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='imagem',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='turmas'),
        ),
    ]
