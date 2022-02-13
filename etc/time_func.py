from datetime import date
from datetime import datetime, timedelta


def rtn_date(date_format):
    now = date.today()
    today_date = now.strftime(date_format)
    return today_date


def rtn_datetime(date_format, time_format):
    now = datetime.now()
    today_date = now.strftime(date_format)
    now_time = now.strftime(time_format)
    return today_date, now_time


def put_date_in_filename(file_type, file):  # 파일명에 날짜 추가
    today_date = rtn_date(date_format="%y%m%d")

    extension = '.' + file_type
    file_name = file.split(extension)[0]
    new_file_name = file_name + '_' + today_date + extension

    return new_file_name


def put_datetime_in_filename(file_type, file, include_seconds):  # 파일명에 날짜/시간 추가
    time_format = "%H%M"
    if include_seconds:
        time_format += "%S"
    today_date, now_time = rtn_datetime(date_format="%y%m%d", time_format=time_format)

    extension = '.' + file_type
    file_name = file.split(extension)[0]
    new_file_name = file_name + '_' + today_date + '_' + now_time + extension

    return new_file_name
