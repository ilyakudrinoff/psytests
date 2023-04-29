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
    adult = models.CharField('Старше 18?', choices=ADULT, max_length=10)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'{self.name}'


class Questions(TimeStampedModel):
    question = models.TextField('Вопрос')
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='test', blank=True, null=True,
                             verbose_name='Тест')

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.question}'


class Answers(TimeStampedModel):
    answer = models.CharField('Ответ', max_length=100)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='a_test', blank=True, null=True,
                             verbose_name='Тест')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='a_question', blank=True, null=True,
                                 verbose_name='Вопросы')

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.answer}'


class Results(TimeStampedModel):
    psyholog = models.ForeignKey(Psyhologes, on_delete=models.CASCADE, related_name='psyholog', blank=True, null=True,
                                 verbose_name='Психолог')
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='r_test', blank=True, null=True,
                                 verbose_name='Тест')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='r_question', blank=True, null=True,
                                 verbose_name='Вопросы')
    answer = models.CharField('Выбранный ответ', max_length=100)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'{self.psyholog}'
