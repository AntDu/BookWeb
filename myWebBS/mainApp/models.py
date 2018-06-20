from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    surname = models.CharField(max_length=256, blank=True, null=True)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    publish_year = models.DateTimeField()
    book_to_author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128, null=True)
    licens = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    book_to_publisher = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    book_to_genre = models.ManyToManyField(Book)  # , through='Booktogenres')

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    nickname = models.CharField(max_length=128, blank=True, null=True)
    birthday = models.DateTimeField(auto_now_add=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, max_length=64)
    book_to_user = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True)
    content = models.CharField(max_length=512, blank=True, null=True)
    notes = models.CharField(max_length=512, blank=True, null=True)
    review_to_book = models.ManyToManyField(Book)

    def __str__(self):
        return self.title


class ReviewComments(models.Model):
    comment = models.CharField(max_length=512, blank=True, null=True)
    like = models.PositiveIntegerField()
    dislike = models.PositiveIntegerField()
    comment_to_user = models.ManyToManyField(User)

    def __str__(self):
        return self.comment
