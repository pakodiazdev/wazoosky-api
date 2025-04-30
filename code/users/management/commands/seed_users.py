from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with test users"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=10)

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for _ in range(total):
            email = fake.unique.email()
            username = fake.user_name()
            password = "secret123"

            if not User.objects.filter(email=email).exists():
                User.objects.create_user(
                    email=email, username=username, password=password
                )
                self.stdout.write(self.style.SUCCESS(f"✅ Created user: {email}"))
