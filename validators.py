def is_valid_task_name(name):
    # BUG: no check for empty string
    if len(name) > 0:
        return True

def is_valid_priority(priority):
    # BUG: wrong comparison, should check range 1-5
    if priority > 0:
        return True
    return False

def is_valid_email(email):
    # BUG: no real validation, just checks length
    if len(email) > 5:
        return True
    return False
