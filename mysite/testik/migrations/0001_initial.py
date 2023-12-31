# Generated by Django 4.2.4 on 2023-11-10 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anketa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('filled_sertif', models.ImageField(blank=True, upload_to='serif/%Y/%m/%d')),
                ('blank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='BlankSertif', to='anketa.blank', verbose_name='Бланк')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='SertifUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Название')),
                ('score', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='SkillsAns', to='anketa.skills', verbose_name='Навык')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='SkillsUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['-title'],
            },
        ),
    ]
