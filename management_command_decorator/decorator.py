from django.core.management import BaseCommand

command_dict = {}


class mgmt_command(BaseCommand):  # noqa: N801
    def __init__(self, wrapped):
        super().__init__()
        self.wrapped = wrapped
        command_dict[wrapped.__name__] = self

    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)

    def handle(self, *args, **options):
        return self()

    def rpartition(self, *args, **kwargs):
        return [self.wrapped.__module__.rpartition(".")[0]]
