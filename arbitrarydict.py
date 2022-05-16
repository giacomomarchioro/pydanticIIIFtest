from pydantic import BaseModel, parse_obj_as
from typing import Dict, Optional

from pydantic import parse

class Values(BaseModel):
    Value: str
    Type: str


class Mymodel(BaseModel):
    MessageAttributes: Optional[Dict[str, Values]]


data = {"MessageAttributes": {"ArbitraryKey": {"Type": "String", "Value": "TestString"}}}

parsed = Mymodel.parse_obj(data)

print(parsed)
print(parsed.MessageAttributes['ArbitraryKey'].Type)