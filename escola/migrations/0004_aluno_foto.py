# Generated by Django 5.0.6 on 2024-06-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_aluno_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
