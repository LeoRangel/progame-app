# Generated by Django 3.0.4 on 2020-05-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_tentativa_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='nivel',
            field=models.CharField(choices=[(0, 'Nenhum'), (1, '1 - Lembrar'), (2, '2 - Entender'), (3, '3 - Aplicar'), (4, '4 - Analisar'), (5, '5 - Avaliar'), (6, '6 - Criar')], default=0, max_length=1),
        ),
    ]
