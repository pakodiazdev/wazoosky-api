from unittest.mock import patch

import pytest
from django.core.management import call_command


@pytest.mark.django_db
class TestSeedUsersCommand:

    def test_add_arguments(self):
        """Ensure the command adds the --total argument."""
        from users.management.commands.seed_users import Command

        parser = Command().create_parser("manage.py", "seed_users")
        options = parser.parse_args([])
        assert hasattr(options, "total")
        assert options.total == 100  # default value

    @patch("users.management.commands.seed_users.User.objects.bulk_create")
    def test_handle(self, mock_bulk_create):
        """Ensure the command calls bulk_create with the specified number of users."""
        call_command("seed_users", "--total", "2")
        mock_bulk_create.assert_called_once()
        # Check that it received exactly 2 users
        args, kwargs = mock_bulk_create.call_args
        users_created = args[0]
        assert len(users_created) == 2
