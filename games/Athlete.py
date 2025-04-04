class Athlete:
    '''
    Athlete class, with only name attribute.
    '''
    def __init__(self, name:str):
        self.name = name
        
    def __str__(self):
        return f"Athlete: {self.name}"
    
    def __repr__(self):
        return f"Athlete('{self.name}')"
    
    def to_json(self) -> dict:
        return {"name": self.name}
    
    def display(self):
        print(f"{self.name}")
        
if __name__ == '__main__':
    a = Athlete("Ana G.")
    a.display()
    print(a)
    print(repr(a))
    print (f"a: {id(a)}")
    b = eval(repr(a))
    print(b)
    print(f"b: {id(b)}")