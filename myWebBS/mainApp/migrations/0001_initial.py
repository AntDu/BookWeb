# Generated by Django 2.0.5 on 2018-05-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('surname', models.CharField(db_column='Surname', max_length=256)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('description', models.CharField(db_column='Description', max_length=256, null=True)),
                ('publishyear', models.DateTimeField(db_column='PublishYear')),
                ('books_ta_authors', models.ManyToManyField(to='mainApp.Authors')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=256, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=256, null=True)),
                ('books_to_genres', models.ManyToManyField(to='mainApp.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=128)),
                ('country', models.CharField(db_column='Country', max_length=128)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=128, null=True)),
                ('licens', models.CharField(blank=True, db_column='Licens', max_length=256, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=512, null=True)),
                ('books_to_publisher', models.ManyToManyField(to='mainApp.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_column='Title', max_length=512, null=True)),
                ('content', models.CharField(db_column='Content', max_length=512)),
                ('notes', models.CharField(db_column='Notes', max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewcomments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(db_column='Comment', max_length=512)),
                ('likes', models.IntegerField(blank=True, db_column='Likes', null=True)),
                ('dislikes', models.IntegerField(blank=True, db_column='Dislikes', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_column='FirstName', max_length=128, null=True)),
                ('lastname', models.CharField(db_column='LastName', max_length=128, null=True)),
                ('nickname', models.CharField(blank=True, db_column='NickName', max_length=128, null=True)),
                ('birthday', models.DateTimeField(db_column='BirthDay')),
                ('dateregistration', models.DateTimeField(db_column='DateRegistration')),
                ('email', models.EmailField(db_column='Email', max_length=64, unique=True)),
                ('books_to_users', models.ManyToManyField(to='mainApp.Books')),
            ],
        ),
        migrations.AddField(
            model_name='reviewcomments',
            name='comments_to_users',
            field=models.ManyToManyField(to='mainApp.Users'),
        ),
    ]
