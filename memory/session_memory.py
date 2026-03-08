session = {}

def set_state(key, value):
    session[key] = value

def get_state(key):
    return session.get(key)