import django
from django.apps import AppConfig

from management_command_decorator.decorator import command_dict


class ManagementCommandDecoratorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "management_command_decorator"

    def ready(self):
        from django.core.management import get_commands

        old_get_commands = get_commands

        def new_get_commands(*args, **kwargs):
            commands = old_get_commands(*args, **kwargs)
            for name, cmd in command_dict.items():
                commands[name] = cmd

            return commands

        django.core.management.get_commands = new_get_commands
