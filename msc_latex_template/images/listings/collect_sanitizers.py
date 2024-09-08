def collect_sanitizers(cls):
    cls.required_params = {}
    cls.validators = {}
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        if hasattr(method, '_required_params') and hasattr(method, '_validators'):
            cls.required_params[name] = method._required_params
            cls.validators[name] = method._validators
    return cls