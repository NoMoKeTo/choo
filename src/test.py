#!/usr/bin/env python3
import code
import json
from pprint import pprint  # noqa

from choo.apis.de import vrr
from choo.models import City, Stop
from choo.queries import PlatformQuery  # noqa
from choo.types import Coordinates, Serializable

# collection = Collection('test')

bs = Stop(city=City('essen'), name='borbeck süd bf')
results = vrr.platforms.where(coords=Coordinates(51.462983, 6.956251)).max_distance(5000).execute()
pprint(list(results)[0].serialize())
print(json.dumps(list(results)[0].serialize(), indent=2))
code.interact(local=locals())


# bo = Stop(city='essen', name='hbf')
# bo = Stop(city='heidelberg', name='hbf')

# trip = Trip.Request()
# trip.origin = bs
# trip.destination = bo

# location = Location.Request()
# location.name = 'Borbeck'

# vrr.dump_raw = True
# result = vrr.query(trip)

# import pprint
# pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(result.serialize())
# print(result.results)
# serialized = json.dumps(result.serialize(no_duplicates=[]), indent=2)
# print(serialized)
