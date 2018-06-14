

import names
import random
import argparse

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from mainApp.models import Author, Book, Publisher, Genre
from datetime import datetime

from random import randrange
from datetime import timedelta


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
            # choices=['y', 'n']
        )

    # python manage.py create_test_data

    def handle(self, *args, **options):
        # TODO move this to args (in terminal)
        # $ python manage.py create_test_data 1000

        # TODO add key
        # python manage.py create_test_data 1000 --clean=y/n

        # clean DB data

        if options['clean']:
            Author.objects.all().delete()
            Book.objects.all().delete()
            Publisher.objects.all().delete()
            Genre.objects.all().delete()


        # num = 10
        num = options['num'][0]

        # create author
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
