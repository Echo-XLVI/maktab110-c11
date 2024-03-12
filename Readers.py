class Reader:
    def __init__(self, name:str, email:str) -> None:
        self.name=name
        self.email=email
        self.comments={}
        self.points={}