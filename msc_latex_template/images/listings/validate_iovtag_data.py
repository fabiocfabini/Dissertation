def validate_iovdata(iovdata):
    for entry in iovdata:
        for run, data in entry.items():
            func_name = data["func"]
            payload = data["payload"]
            try:
                validate_required_arguments(payload, func_name)
            except ValueError as err:
                raise ValueError(f"Invalid config at run {run}.") from err