# Generated by Django 4.1.7 on 2023-03-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_application', '0004_alter_book_pic_url_alter_hold_book_author_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pic_url',
            field=models.CharField(max_length=255),
        ),
    ]
