# Generated by Django 4.2 on 2023-04-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psyhologes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=10, verbose_name='Пол')),
                ('old', models.IntegerField(verbose_name='Возраст')),
                ('instagram', models.CharField(max_length=50, verbose_name='Инстаграм')),
                ('telegram', models.CharField(max_length=50, verbose_name='Телеграм')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Психолог',
                'verbose_name_plural': 'Психологи',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название анкеты')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=100, verbose_name='Ответ')),
                ('adult', models.CharField(choices=[('after 18', 'after 18'), ('before 18', 'before 18')], max_length=10, verbose_name='Старше 18?')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=100, verbose_name='Выбранный ответ')),
                ('psyholog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psyhologes', to='psytests.psyhologes', verbose_name='Психолог')),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='psytests.psyhologes', verbose_name='Тест')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
