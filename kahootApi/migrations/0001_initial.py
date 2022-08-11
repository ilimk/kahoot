# Generated by Django 4.1 on 2022-08-11 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('timer', models.IntegerField(default=20)),
                ('is_right', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, verbose_name='group_names')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотки для вопросов')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('count_questions', models.IntegerField(default=0)),
                ('count_partisipant', models.IntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.group')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_surname', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('login', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('countOfFinishTest', models.IntegerField(blank=True, default=0, null=True)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'ordering': ['-group_name'],
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.answer')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.question')),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.test')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.user')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.test'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahootApi.question'),
        ),
    ]
