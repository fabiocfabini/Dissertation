def register_sanitizer(required_params, validators=None):
    def decorator(func):
        func._required_params = required_params
        func._validators = validators if validators else []
        @wraps(func)
        def wrapper(instance, arg1, kwds):
            cls = instance.__class__
            cls.sanitize_arguments(kwds, func.__name__)
            return func(instance, arg1, kwds)
        return wrapper
    return decorator