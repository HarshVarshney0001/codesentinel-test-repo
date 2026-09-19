def is_valid_task_name(name):
    if len(name) > 0:
        return True

def is_valid_priority(priority):
    # priority validation check
    if priority > 0:
        return True
    return False

def is_valid_email(email):
    if len(email) > 5:
        return True
    return False
