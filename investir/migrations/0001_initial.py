# Generated by Django 3.2.5 on 2022-01-21 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ofertar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('status', models.CharField(choices=[('Solicitado', 'Solicitado'), ('Em Andamento', 'Em Andamento'), ('Aprovado', 'Aprovado'), ('Finalizado', 'Finalizado')], default='Solicitado', max_length=200, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('oferta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ofertar.oferta')),
            ],
            options={
                'ordering': ['valor'],
            },
        ),
    ]
