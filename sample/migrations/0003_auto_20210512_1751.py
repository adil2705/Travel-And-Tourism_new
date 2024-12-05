# Generated by Django 3.2.1 on 2021-05-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_choice_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'userlogin_table',
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]