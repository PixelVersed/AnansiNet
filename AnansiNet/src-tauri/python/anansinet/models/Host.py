from pydantic import BaseModel

class Host(BaseModel):
    ip: str
    mac: str
    spoofed: bool = False
    limited: bool = False
    blocked: bool = False

    def __init__(self, ip: str, mac: str) -> None:
        super().__init__(ip=ip, mac=mac)
        self.ip = ip
        self.mac = mac

    
    # @override
    # def __eq__(self, other) -> bool:
    #     return self.ip == other.ip

    # @override
    # def __hash__(self):
    #     return hash((self.mac, self.ip))