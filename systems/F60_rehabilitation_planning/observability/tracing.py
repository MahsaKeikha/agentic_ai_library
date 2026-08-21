class TraceLog:
    def __init__(self):self.events=[]
    def record(self,stage:str,detail:str):self.events.append({"stage":stage,"detail":detail})
