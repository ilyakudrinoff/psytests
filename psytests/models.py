from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


GENDER = (
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
)

ADULT = (
    ('after 18', 'after 18'),
    ('before 18', 'before 18'),
)


class Psyhologes(TimeStampedModel):
    name = models.CharField('Имя', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    gender = models.CharField('Пол', choices=GENDER, max_length=10)
    old = models.IntegerField('Возраст')
    instagram = models.CharField('Инстаграм', max_length=50)
    telegram = models.CharField('Телеграм', max_length=50)
    email = models.CharField('Почта', max_length=100)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Психолог'
        verbose_name_plural = 'Психологи'

    def __str__(self):
        return f'{self.name}'


class Tests(TimeStampedModel):
    name = models.CharField('Название анкеты', max_length=200)
    question = models.TextField('Вопрос')
    answer = models.CharField('Ответ', max_length=100)
    adult = models.CharField('Старше 18?', choices=ADULT, max_length=10)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'{self.name}'


class Results(TimeStampedModel):
    psyholog = models.ForeignKey(Psyhologes, on_delete=models.CASCADE, related_name='psyhologes', blank=True, null=True,
                                 verbose_name='Психолог')
    test = models.ForeignKey(Psyhologes, on_delete=models.CASCADE, related_name='tests', blank=True, null=True,
                                 verbose_name='Тест')
    question = models.TextField('Вопрос')
    answer = models.CharField('Выбранный ответ', max_length=100)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'{self.psyholog}'
