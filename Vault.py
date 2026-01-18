class Vault:
    def __init__(self, galleons=0, knuts=0, sickles=0):
        self.galleons = galleons
        self.sickles = sickles
        self. knuts = knuts

    def __str__(self):
        return f"{self.knuts} Knuts,{self.sickles} Sickles,{self.galleons} Galleons"
    
# http://docs.python.org/3/reference/datamodel.html#special-method-names
# for more methods

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        knuts = self.knuts + other.knuts
        sickles = self.sickles + other.sickles
        return Vault(galleons , sickles , knuts)
        
potter = Vault(100,30,70)  
goosy = Vault(200,40,70)
total = potter + goosy
print (total)   