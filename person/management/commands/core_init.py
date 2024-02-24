from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import connection
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            # Temporarily disable foreign key checks for SQLite
            if connection.vendor == "sqlite":
                cursor.execute("PRAGMA foreign_keys=OFF;")

            try:
                # Drop all tables for SQLite excluding sqlite_sequence
                if connection.vendor == "sqlite":
                    cursor.execute(
                        "SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';"
                    )
                    tables = cursor.fetchall()
                    for table in tables:
                        cursor.execute(f"DROP TABLE {table[0]};")
                else:
                    # Drop schema for other databases
                    cursor.execute("DROP SCHEMA public CASCADE;")

                # Apply migrations to create new tables
                self.stdout.write(self.style.SUCCESS("Dropped all tables."))
                self.stdout.write(self.style.SUCCESS("Applying migrations..."))
                call_command("migrate")

                self.stdout.write(self.style.SUCCESS("Database reset successfully."))

            finally:
                # Re-enable foreign key checks for SQLite
                if connection.vendor == "sqlite":
                    cursor.execute("PRAGMA foreign_keys=ON;")

        User.objects.create_superuser(
            username="moshihud",
            password="123456",
        )
        User.objects.create_superuser(
            username="admin",
            password="123456",
        )
        self.stdout.write("Successfully created super user")
