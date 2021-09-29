# Generated by Django 3.0.4 on 2020-04-04 18:06

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    Turma = apps.get_model('progame', 'Turma')
    Modulo = apps.get_model('progame', 'Modulo')
    Questao = apps.get_model('progame', 'Questao')

    for turma in Turma.objects.all():
        turma.uuid = uuid.uuid4()
        turma.save()

    for modulo in Modulo.objects.all():
        modulo.uuid = uuid.uuid4()
        modulo.save()

    for questao in Questao.objects.all():
        questao.uuid = uuid.uuid4()
        questao.save()


class Migration(migrations.Migration):

    dependencies = [
        ('progame', '0002_auto_20200402_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='questao',
            name='uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='uuid',
            field=models.UUIDField(editable=False, null=True),
        ),

        migrations.RunPython(create_uuid),

        migrations.AlterField(
            model_name='modulo',
            name='uuid',
            field=models.UUIDField(unique=True, default=uuid.uuid4, null=False),
        ),
        migrations.AlterField(
            model_name='questao',
            name='uuid',
            field=models.UUIDField(unique=True, default=uuid.uuid4, null=False),
        ),
        migrations.AlterField(
            model_name='turma',
            name='uuid',
            field=models.UUIDField(unique=True, default=uuid.uuid4, null=False),
        ),
    ]
