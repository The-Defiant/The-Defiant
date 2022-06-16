class DataBase():
    def __init__(self):
        self.tables = {}
        self.connect = None
        
        
        
    def connect(self):
        self.connect = True
        return self
    
    def disconnect(self):
        self.connect = False
        return self
    
    def create_table(self, name: str):
        self.tables[name] = {}
        return self    
        
    def add_element_to_table(self, table, element):
        self.tables[table][]
    
        