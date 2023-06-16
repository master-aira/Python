class Dad:
    basketball = 1
class Son(Dad):
    dance = 1
    basketball = 11
    def is_dance(self):
        return f"Yes I do dance {self.dance} no of times"
class Grandson(Son):
        dance = 6
        def is_dance(self):
            return f"Yes I do dance Very Awesomely! {self.dance} no of times"
darry = Dad()
larry = Son()
harry = Grandson()
print(harry.basketball)