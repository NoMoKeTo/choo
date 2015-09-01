#!/usr/bin/env python3
from .base import Serializable, TripPart
from .locations import AbstractLocation, Coordinates
from . import fields


class Way(TripPart):
    waytype = fields.Model('WayType', none=False)
    origin = fields.Model(AbstractLocation, none=False)
    destination = fields.Model(AbstractLocation, none=False)
    distance = fields.Field(float)
    duration = fields.Timedelta()
    events = fields.List(fields.Model('WayEvent', none=False))
    path = fields.List(fields.Model(Coordinates, none=False))

    def __init__(self, waytype=None, origin=None, destination=None, distance=None, **kwargs):
        super().__init__(waytype=(WayType('walk') if waytype is None else waytype),
                         origin=origin, destination=destination, distance=distance, **kwargs)

    def __eq__(self, other):
        return (isinstance(other, Way) and self.waytype == other.waytype and
                self.origin == other.origin and self.destination == other.destination)

    def __repr__(self):
        distance = ''
        if self.distance:
            distance = ' %dm' % self.distance
        return '<Way %s %dmin%s %s %s>' % (
            str(self.waytype), self.duration.total_seconds() / 60,
            distance, repr(self.origin), repr(self.destination))


class WayType(Serializable):
    _known = ('walk', 'bike', 'car', 'taxi')
    _created = {}

    def __new__(cls, value=''):
        if isinstance(value, cls):
            return value
        elif value not in cls._known:
            raise AttributeError('invalid waytype: %s' % repr(value))
        if value in cls._created:
            return cls._created[value]
        else:
            self = super().__new__(cls)
            self._value = value
            cls._created[value] = self
            return self

    def _serialize_instance(self):
        return self._value

    @classmethod
    def unserialize(cls, data):
        return cls(data)

    def __repr__(self):
        return 'WayType(%s)' % repr(self._value)

    def __str__(self):
        return self._value

    def __eq__(self, other):
        return other._value == self._value


class WayEvent(Serializable):
    _created = {}

    def __new__(cls, name='', direction=''):
        if isinstance(name, cls):
            return name
        assert name in ('stairs', 'elevator', 'escalator')
        assert direction in ('up', 'down')
        value = (name, direction)
        if value in cls._created:
            return cls._created[value]
        else:
            self = super().__new__(cls)
            self._value = value
            cls._created[value] = self
            return self

    def _serialize_instance(self):
        return self._value

    @classmethod
    def unserialize(cls, data):
        return cls(*data)

    def __repr__(self):
        return 'WayEvent%s' % repr(self._value)

    def __iter__(self):
        return self._value

    def __eq__(self, other):
        return isinstance(other, WayEvent) and self._value == other._value

    @property
    def name(self):
        return self._value[0]

    @property
    def direction(self):
        return self._value[1]