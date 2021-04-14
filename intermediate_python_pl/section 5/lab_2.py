import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path, 'a')) as f:
                f.write(f'Action {logged_action} executed on {path} on {dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE CREATE', 'lab_2/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE DELETE', 'lab_2/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file('lab_2/dummy_file.txt')
delete_file('lab_2/dummy_file.txt')
create_file('lab_2/dummy_file.txt')
delete_file('lab_2/dummy_file.txt')
