class MyRouter(object):
    "this is a class that describes the characteristics of a router."
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
        
    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router name is: ", self.model)
        print("The router name is: ", self.serialno)
        print("The router name is: ", self.ios)
        print("The router name is: ", self.model + manuf_date)
