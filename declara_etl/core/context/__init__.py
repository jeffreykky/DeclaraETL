from declara_etl.types.driver import DriverT

class Context:


    def __init__(self):
        self.setup()


    def setup(self):
        
        self.driver: DriverT = None
        self.task = None
        self.operators = []
        self.env_var:dict = dict()

        
context = Context()