from dataclasses import dataclass,field
@dataclass
class DeviceProject:
    device_name:str
    requirements:list[dict]=field(default_factory=list)
