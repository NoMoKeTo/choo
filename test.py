#!/usr/bin/env python3
from networks import VRR
from models import Stop
from datetime import datetime
import json

vrr = VRR()
du = Stop(city='essen', name='borbeck süd bf')

result = vrr.get_stop_rides(du)
print(json.dumps(result.serialize(), indent=2))
