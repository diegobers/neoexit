# Generated by Django 4.0.2 on 2022-02-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('data_criacao', models.DateField(auto_now_add=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('status', models.CharField(choices=[('Destaque', 'Destaque'), ('Aberta', 'Aberta'), ('Fechada', 'Fechada')], max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
    ]
