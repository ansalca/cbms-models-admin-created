from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Assign users to groups'

    def handle(self, *args, **kwargs):
        # Define users and their groups
        users_groups = {
            'admin_user': 'Admin',
            'editor_user': 'Editor',
            'viewer_user': 'Viewer',
        }

        # Assign users to groups
        for username, group_name in users_groups.items():
            user = User.objects.get(username=username)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

        self.stdout.write(self.style.SUCCESS('Users assigned to groups successfully.'))

