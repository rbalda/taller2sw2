class Card:
    def __init__(self):
        self.name=""
        self.last_name=""
        self.code=""
        self.credit=0.00

    # def name(self,value):
    #     if value:
    #         self.name=value
    #         return
    #     return self.name
    #
    # def last_name(self,value):
    #     if value:
    #         self.last_name=value
    #         return
    #     return self.last_name
    #
    # def code(self, value):
    #     if value:
    #         self.code=value
    #         return
    #     return self.code

    def credit(self, value):
        if value:
            self.credit=value
            return
        return self.credit