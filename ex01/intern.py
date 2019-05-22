class Intern:
    def __init__(self,Name="My name? I'm nobody, an intern, I have no name"):
        self.Name = Name

    def __str__(self):
        return(self.Name)

    class Coffee:
        def __str__(self):
            return("This is the worst coffee you ever tasted")

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        coffee = Intern.Coffee()
        return(coffee)

#--------------------------------
if __name__ == '__main__':
    nobody = Intern()
    mark = Intern("Mark")
    # afficher le nom des instances
    print(nobody)
    print(mark)
    #demqder a mark un cafe et afficher le resultat
    #mark.make_coffee()
    print(mark.make_coffee())
    #Demandez à l’autre stagiaire de travailler 
    try:
        nobody.work()
    except Exception as e:
        print(e)
    #pour supprimer l'instance
    