class Human:
    def __init__(
            self, 
            firstname: str, 
            lastname: str, 
            age: int
    ) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
def generate_human():
    return Human(firstname="Mark", lastname="Markov", age=20)

human = generate_human()
