from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Group(models.Model):
    group_name = models.CharField(max_length=50, verbose_name='group_names')

    def __str__(self):
        return self.group_name


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True)
    login = models.EmailField()
    password = models.CharField(max_length=100)
    score = models.IntegerField(null=True, blank=True, default=0)
    rating = models.IntegerField(null=True, blank=True, default=0)
    countOfFinishTest = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-group_name']

    def __str__(self):
        return self.user_name + ' ' + self.user_surname


class Test(models.Model):
    test_name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    count_questions = models.IntegerField(default=0)
    count_partisipant = models.IntegerField(default=0)

    def __str__(self):
        return self.test_name

class Question(models.Model):
    question = models.CharField(max_length=255)
    test_name = models.ForeignKey(Test, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотки для вопросов', null=True, blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    timer = models.IntegerField(default=20)
    is_right = models.BooleanField(default=False)
    score = models.IntegerField(default=100)

    def __str__(self):
        return self.answer

    def clean(self, *args, **kwargs):
        b = Answer.objects.all().filter(question=self.question).count()
        c = Answer.objects.all().filter(is_right = True).count()
        if c > 0 and self.is_right == True:
            raise ValidationError('Уже есть правильный ответ')
        if b >= 4:
            raise ValidationError('Вопросов больше чем 4')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class UserAnswer(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.ForeignKey(Test, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    second = models.IntegerField()

    def __str__(self):
        return 'Имя пользователя; ' + str(self.user_name) + ' Тест: ' + str(self.test_name)
