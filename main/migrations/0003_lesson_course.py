# Generated by Django 4.2.3 on 2023-07-18 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_lesson_url_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='Курс'),
        ),
    ]
