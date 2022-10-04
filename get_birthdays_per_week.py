from datetime import datetime, timedelta


friends = {'Oleg': datetime(year=1990, month=10, day=1),
           'Olga': datetime(year=1989, month=10, day=3),
           'Sergij': datetime(year=2000, month=10, day=6),
           'Olja': datetime(year=1978, month=10, day=2),
           'Volodymyr': datetime(year=1994, month=10, day=4),
           'Olja_small': datetime(year=1985, month=10, day=3),
           'Vasyl': datetime(year=2002, month=10, day=7),
           'Georg': datetime(year=1995, month=10, day=9),
           'Petro': datetime(year=1988, month=10, day=12),
           'Pylyp': datetime(year=1999, month=10, day=8),
           'Svjatoslav': datetime(year=1989, month=10, day=4),
           'Gregor': datetime(year=2000, month=10, day=3)
           }


def get_birthdays_per_week(users):
    birthday_people = {'Monday': [], 'Tuesday': [],
                       'Wednesday': [], 'Thursday': [], 'Friday': []}
    date_all = datetime.now()
    date = date_all.replace(hour=0, minute=0, second=0, microsecond=0)
    # date = datetime(year=2022, month=10, day=4)

    if date.weekday() == 5:
        days_analiz = timedelta(days=7)
    elif date.weekday() == 6:
        days_analiz = timedelta(days=6)
    else:
        interval = 5 - date.weekday()
        days_analiz = timedelta(days=interval)

    date_fin = date + days_analiz

    for name in users:
        user_an = users[name].replace(year=date.year)
        if date <= user_an < date_fin:
            holiday = user_an.strftime('%A')
            if user_an.weekday() in (5, 6):
                holiday = 'Monday'
            birthday_people[holiday].append(name)

    for key in birthday_people:
        if len(birthday_people[key]) > 0:
            print(key, ':', ', '.join(birthday_people[key]))


if __name__ == '__main__':
    get_birthdays_per_week(friends)
