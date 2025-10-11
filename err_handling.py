def transform_err(error):
    error = (str(error))
    if "takes 0 positional arguments" in error:
        return "This command doesn't take a target"
    elif "missing" and  "required positional arguments" in error:
        return "Please specify a target"
    else:
        return error

