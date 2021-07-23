import json
from iiifprezi3 import Manifest
manifest = Manifest()
json.dumps(manifest.json(exclude_unset=True)) 