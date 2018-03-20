import datetime
from past.builtins import basestring
from six import iteritems
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def round_to_day(date):
    return datetime.date(*date.timetuple()[:3])


def to_day(date_or_date_string, date_format=DATE_FORMAT):
    """Convert to a datetime.date instance, rounded down to day."""
    if isinstance(date_or_date_string, basestring):
        date = datetime.datetime.strptime(date_or_date_string, date_format)
    elif isinstance(date_or_date_string, datetime.datetime):
        date = date_or_date_string
    elif isinstance(date_or_date_string, datetime.date):
        date = datetime.datetime(
            year=date_or_date_string.year,
            month=date_or_date_string.month,
            day=date_or_date_string.day)
    else:
        raise ValueError('invalid argument: %r' % date_or_date_string)
    return round_to_day(date)


def list_to_str(thelist, joinstr='+'):
    if isinstance(thelist, list):
        thelist = joinstr.join(thelist)
    return thelist


def format_request_data(**kwargs):
    data = {k: v for k, v in iteritems(kwargs) if v is not None}
    if data.get('date'):
        data['date'] = str(to_day(data['date']))
    if data.get('start_date'):
        data['start_date'] = str(to_day(data['start_date']))
    if data.get('end_date'):
        data['end_date'] = str(to_day(data['end_date']))
    if data.get('countries'):
        data['countries'] = list_to_str(data['countries']).upper()
    if data.get('categories'):
        data['categories'] = list_to_str(data['categories'], joinstr='+')
    if data.get('category'):
        data['category'] = list_to_str(data['category'], joinstr='+')
    if data.get('device'):
        data['device'] = list_to_str(data['device'])
    if data.get('types'):
        data['types'] = list_to_str(data['types'])
    if data.get('keywords'):
        data['keywords'] = list_to_str(data['keywords'], ',')
    return data
