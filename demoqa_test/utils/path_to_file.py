import os


def get_path(file_name):
    picture_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', '..', 'tests', 'resources', file_name))
    return picture_path


print(get_path('photo_2016-08-25_20-45-23.jpg'))
