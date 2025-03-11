from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define groups and their permissions
        groups_permissions = {
            'Admin': ['add_user', 'change_user', 'delete_user', 'view_user'],
            'Editor': ['change_user', 'view_user'],
            'Viewer': ['view_user'],
        }

        # Create groups and assign permissions
        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.get(codename=perm)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully.'))

