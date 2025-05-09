from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with test users"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=100)

    def handle(self, *args, **options):
        total = options["total"]
        fake = Faker()

        users = []
        for _ in range(total):
            users.append(
                User(
                    username=fake.unique.user_name(),
                    email=fake.unique.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                )
            )

        User.objects.bulk_create(users, batch_size=500)
        self.stdout.write(
            self.style.SUCCESS(f"✅ {total} users created with bulk_create")
        )
