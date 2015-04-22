#!/usr/bin/env python3
from networks import VRR
from models import Stop, Trip
from datetime import datetime
from output import PrettyPrint
import json

vrr = VRR()
du = Stop(city='essen', name='hbf')
bs = Stop(city='essen', name='borbeck süd bf')

trip = Trip()
trip.origin = du
trip.destination = bs

vrr.get_trips()
#result = vrr.get_stop_rides(du)
#p = PrettyPrint()
#print(p.formatted(result))
# print(json.dumps(result.serialize(), indent=2))
