
class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class MonthConverter:
    regex = r"\d{1,2}"

class DayConverter:
    regex = r"[0123]\d"