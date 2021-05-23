try:
    import importlib.resources as importlib_resources
except ImportError:
    # In PY<3.7 fall-back to backported `importlib_resources`.
    import importlib_resources


def get_db_path():
    db_path_gen = importlib_resources.path(__name__, 'db.json')
    db_path_list = list(db_path_gen.gen)
    return str(db_path_list[0])

