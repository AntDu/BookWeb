from django.db import models


class Authors(models.Model):
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=256)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name + + self.surname


class Books(models.Model):
    name = models.CharField(db_column='Name', max_length=256)
    description = models.CharField(db_column='Description', max_length=256, null=True)
    publishyear = models.DateTimeField (db_column='PublishYear')
    books_to_authors = models.ManyToManyField(Authors)  # , through='Bookstoauthors')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(db_column='Name', max_length=128)
    country = models.CharField(db_column='Country', max_length=128)
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=128, null=True)
    licens = models.CharField(db_column='Licens', max_length=256, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)
    books_to_publisher = models.ManyToManyField(Books)  # , through='Bookstopublisher')

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(db_column='Name', max_length=256, null=True)
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)
    books_to_genres = models.ManyToManyField(Books)  # , through='Bookstogenres')

    def __str__(self):
        return self.name


class Users(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=128, null=True)
    lastname = models.CharField(db_column='LastName', max_length=128, null=True)
    nickname = models.CharField(db_column='NickName', max_length=128, blank=True, null=True)
    birthday = models.DateTimeField(db_column='BirthDay')
    dateregistration = models.DateTimeField(db_column='DateRegistration')
    email = models.EmailField(db_column='Email', unique=True, max_length=64)
    books_to_users = models.ManyToManyField(Books)  # , through=

    def __str__(self):
        return self.firstname + + self.lastname


class Review(models.Model):
    title = models.CharField(db_column='Title', max_length=512, blank=True, null=True)
    content = models.CharField(db_column='Content', max_length=512)
    notes = models.CharField(db_column='Notes', max_length=512, null=True)
    # booksreview = models.ForeignKey(Books, db_column='booksreview')
    # booksreview = models.OneToOneField(Books, primary_key=True)
    review_to_books = models.ManyToManyField(Books)

    def __str__(self):
        return self.title


class Reviewcomments(models.Model):
    comment = models.CharField(db_column='Comment', max_length=512)
    likes = models.IntegerField(db_column='Likes', blank=True, null=True)
    dislikes = models.IntegerField(db_column='Dislikes', blank=True, null=True)
    comments_to_users = models.ManyToManyField(Users)  # , through='Userstocomments')

    def __str__(self):
        return self.comment








