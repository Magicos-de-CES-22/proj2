# Generated by Django 3.2.4 on 2021-06-13 18:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0003_auto_20210613_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.CharField(max_length=6)),
                ('nota', models.DecimalField(decimal_places=1, default=1.0, max_digits=2, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)])),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='avaliacao.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='avaliacao.professor')),
            ],
        ),
    ]
