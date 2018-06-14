
import names
import random

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from mainApp.models import Author, Book, Publisher, Genre
from datetime import datetime

from random import randrange
from datetime import timedelta

YES_COMMANDS = ('yes', 'y')
NO_COMMANDS = ('no', 'n')


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')


class Command(BaseCommand):
    help = 'Generates random data'

    def add_arguments(self, parser):

        parser.add_argument('num', nargs='*', type=int)

        parser.add_argument(
            '--clean',
            action='store_true',
            dest='clean',
        )

    def handle(self, *args, **options):

        if options['clean']:

            print("Are you sure you want to delete all data?: y/n\n")
            user_choice = input(">>> ").strip().lower()

            if user_choice.isalpha() and user_choice in NO_COMMANDS and user_choice not in YES_COMMANDS:
                print('Right choice')

            if user_choice.isalpha() and user_choice in YES_COMMANDS and user_choice not in NO_COMMANDS:
                print('You\'re the boss, already delete')
                Author.objects.all().delete()
                Book.objects.all().delete()
                Publisher.objects.all().delete()
                Genre.objects.all().delete()

        num = options['num'][0]

        for i in range(num):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            age = random.randint(1, 79)

            name = f"TITLE {i}"
            text = f"TEXT {i} "
            published_date = random_date(d1, d2)

            aut = Author.objects.create(
                name=first_name,
                surname=last_name,
                age=age
            )

            bo = Book.objects.create(
                name=name,
                description=text,
                publish_year=published_date,
            )

            bo.book_to_author = (aut,)
            bo.save()
