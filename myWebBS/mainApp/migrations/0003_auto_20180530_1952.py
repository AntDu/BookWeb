# Generated by Django 2.0.5 on 2018-05-30 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_review_review_to_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='books_ta_authors',
            new_name='books_to_authors',
        ),
    ]
