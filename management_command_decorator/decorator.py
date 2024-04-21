import wrapt

command_dict = {}


def django_management_command(name=None):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        return wrapped(*args, **kwargs)

    command_dict[name if name else wrapper.__name__] = wrapper
    return wrapper
