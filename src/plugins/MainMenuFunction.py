class MainFunctions:
    def __init__(self, master):
        self.master = master
    
    def closeWindow(self):
        self.master.destroy()
    
    def openSales(self):
        from templates.sales import salesWindow
        self.master.destroy()
        salesWindow()