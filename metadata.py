NEXT_PERSON = 'next:person'
NEXT_EVENT = 'next:event'
NEXT_LOCATION = 'next:location'
NEXT_DATE = 'next:date'

EVENT_URI = 'event:%s:uri'
LOCATION_URI = 'location:%s:uri'
DATE_URI = 'date:%s:uri'

class Person(object):
    def __init__(self):
        pass

    def save(self):
        return 1

class Event(object):
    def __init__(self):
        pass

    def save(self):
        return 1

class Location(object):
    def __init__(self):
        pass

    def save(self):
        return 1

class Date(object):
    def __init__(self):
        pass

    def save(self):
        return 1

class Persons(object):
    def __init__(self, redis):
        self._redis = redis

class Events(object):
    def __init__(self, redis):
        self._redis = redis

class Locations(object):
    def __init__(self, redis):
        self._redis = redis

class Dates(object):
    def __init__(self, redis):
        self._redis = redis

