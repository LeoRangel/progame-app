# Generated by Django 3.0.4 on 2020-06-02 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ausers', '0005_professor_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'professores'},
        ),
    ]
