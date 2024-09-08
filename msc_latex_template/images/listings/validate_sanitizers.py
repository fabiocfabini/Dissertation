def validate_sanitizers(params, func_name):
    if not hasattr(LuminosityCorrector, func_name):
        raise ValueError(f"Function '{func_name}' does not exist in class '{LuminosityCorrector.__name__}'.")
    if func_name not in LuminosityCorrector.required_params:
        raise ValueError(f"Function '{func_name}' cannot be used for corrections.")

    # At this stage params will only be None if The iovtag
    # provided no arguments under 'payload' This may be intended,
    # if the func_name actually does not receive arguments.
    # Otherwise it will be an improper iovtag.
    if params is None:
        params = {}

    param_desc_list = LuminosityCorrector.required_params[func_name]
    missing_params = []
    for param, desc in param_desc_list:
        if param not in params:
            missing_params.append(f"- {param}: {desc}")
    if missing_params:
        err_str = (
            f"The configuration for '{func_name}' is missing required arguments:\n"
            + "\n".join(missing_params)
        )
        raise ValueError(err_str)

    validators_list = LuminosityCorrector.validators[func_name]
    validator_errs = []
    for validator, err_msg in validators_list:
        if not validator(params):
            validator_errs.append(f"- {err_msg}")
    if validator_errs:
        err_str = (
            f"The configuration for '{func_name}' has invalid parameters:\n"
            + "\n".join(validator_errs)
        )
        raise ValueError(err_str)