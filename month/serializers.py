import datetime
from rest_framework import fields, serializers

from month import Month, models

class MonthField(fields.DateField):
  
    format = '%Y-%m'

    def to_internal_value(self, value):
        if isinstance(value, Month):
            month = value
        elif isinstance(value, datetime.date):
            month = Month.from_date(value)
        elif isinstance(value, str):
            try:
                month = Month.from_string(value)
            except ValueError:
                self.fail('invalid', format='YYYY-MM')
        else:
            month = None
        return month
