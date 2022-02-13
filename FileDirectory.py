from etc import dir_func
from etc import time_func
import sys


class FileDirectory:
    _base_directory = 'file/'

    def __init__(self, directory_type):
        if directory_type in ['html', 'report', 'log', 'screenshot']:
            self._directory = self._base_directory + directory_type + '/'
        else:
            sys.exit('Unknown Directory Type')

    @property
    def directory(self):
        return self._directory

    @property
    def today_directory(self):
        date_directory_name = time_func.rtn_date(date_format='%Y%m%d')
        dir_func.mkdir_if_not_exist(directory=self._directory + date_directory_name)
        return self._directory + date_directory_name + '/'
