class myclass():
    x = 10

    def new_class(self, new_x): #create function in class is called method
        self.x = new_x

object = myclass()
print(object.x)

object.new_class(50)
print(object.x)
