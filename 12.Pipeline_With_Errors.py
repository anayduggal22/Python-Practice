import requests

class PipelinedError(Exception):
    pass

class DataPiplined:
    
    def __init__(self, url, table_name):
        self.url = url;
        self.table_name = table_name
    
    def fetch(self):
        try:
            response = requests.get(self.url, timeout= 10)
            response.raise_for_status() #Which can cause exception
            data = response.json()
            print(f"Fetched {len(data)} records")
            return data
        
        except requests.exceptions.Timeout:
            raise PipelinedError(f"Timeout fetching from {self.url}")
        
        except requests.exceptions.HTTPError as e:
            raise PipelinedError(f"HTTP Error: {e}")
        
        except requests.exceptions.ConnectionError:
            raise PipelinedError("No Internet Connection")
        
        
    def store(self, data):
        if not data:
            raise PipelinedError("No data to store")
        print(f"Storing {len(data)} records into {self.table_name}")
        
    def run(self):
        print(f"Running pipline for {self.table_name}...")
        try:
            data = self.fetch()
            self.store(data)
            print("Pipeline complete \n")
            
        except PipelinedError as e:
            print(f"Pipeline failed: {e} \n")
            


good = DataPiplined("https://jsonplaceholder.typicode.com/users", "users_table")
bad = DataPiplined("https://jsonplaceholder.typicode.com/nonexistent", "bad_table")

good.run()
bad.run()