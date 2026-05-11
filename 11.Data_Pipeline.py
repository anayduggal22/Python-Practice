class DataPipeline:
    pipeline_count = 0
    
    def __init__(self, source_url, table_name):
        self.source_url = source_url
        self.table_name = table_name
        DataPipeline.pipeline_count += 1
        
    def fetch(self):
        print(f"Fetching form: {self.source_url}")
        
    def store(self):
        print(f"Storing into: {self.table_name}")
        
    def __str__(self):
        print(f"Pipeline({self.source_url} -> {self.table_name})")
        
    @classmethod
    def get_count(cls):
        return f"Total piplines create: {cls.pipeline_count}"
    

class  GovernmentDataPipeline(DataPipeline):
    
    def __init__(self, source_url, table_name, ministry):
        super().__init__(source_url, table_name)
        self.ministry = ministry
        
    def clean(self):
        print(f"Cleaning data from {self.ministry} ministry")
        
    def __str__(self):
        return f"GovPipeline({self.ministry} | {self.source_url} -> {self.table_name})"
    
    
#Test
p1 = GovernmentDataPipeline("data.gov.in/api/crops", "crops_table", "Agriculture")
p2 = GovernmentDataPipeline("data.gov.in/api/weather", "weather_table", "IMD")

p1.fetch()
p1.clean()
p1.store()

print(p1)
print(p2)
print(DataPipeline.get_count())
