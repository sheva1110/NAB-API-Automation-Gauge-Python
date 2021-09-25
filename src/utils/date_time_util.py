import calendar
import datetime
import time
from datetime import datetime as dt


class DateTimeUtil:

    @staticmethod
    def get_current_daytime_by_format(date_time_format):
        date_time_obj = calendar.timegm(time.gmtime())
        try:
            return dt.fromtimestamp(date_time_obj).strftime(date_time_format)
        except Exception as err:
            print(f'\n\tCurrent datetime can\'t be created due to error: {err}')
            return ''

    @staticmethod
    def get_list_daytime_in_current_week():
        today = datetime.date.today()
        list_day_time = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
        return list_day_time

    @staticmethod
    def pretty_time(seconds):
        sign_string = '-' if seconds < 0 else ''
        seconds = abs(int(seconds))
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        if days > 0:
            return '%s%dd%dh%dm%ds' % (sign_string, days, hours, minutes, seconds)
        elif hours > 0:
            return '%s%dh%dm%ds' % (sign_string, hours, minutes, seconds)
        elif minutes > 0:
            return '%s%dm%ds' % (sign_string, minutes, seconds)
        else:
            return '%s%ds' % (sign_string, seconds)
