class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        print("{0},{1}".format(self.draft,self.crew))
        if(self.draft<=0 | self.crew<=0):
            return False
        elif(self.draft-self.crew*1.5>20):
            return True
        else:
            return False
