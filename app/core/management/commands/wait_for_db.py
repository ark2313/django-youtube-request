from django.core.management.base import BaseCommand
from django.db import connections 
import time
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Wating for DB Connection ...')

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except:
                self.stdout.write("Retry DB Connection")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Success to PostgreSQL connection'))

       # return super().handle(*args, **options)