class DatabaseConnection:
    _instance = None 
    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise Exception("DatabaseConnection instance already exists! Use get_instance().")
        print("Database connection established.")
        DatabaseConnection._instance = self
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatabaseConnection()
        return cls._instance


db1 = DatabaseConnection.get_instance()
db2 = DatabaseConnection.get_instance()

print(db1 is db2) 

try:
    db3 = DatabaseConnection()
except Exception as e:
    print(f"Error: {e}")