# Generated by Django 3.2.5 on 2021-07-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=120)),
                ('Author', models.CharField(max_length=130)),
                ('genre', models.CharField(max_length=123)),
                ('language', models.CharField(max_length=123)),
            ],
        ),
    ]
