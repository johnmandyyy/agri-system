from app.constants import app_constants as CONSTANTS
import random
from app.models import Dataset

class Datagen:
    
    def __init__(self):
        pass

    def insert_random_dataset(self):
        Datasets = self.generate_random_dataset()
        for data in Datasets:
            Dataset.objects.create(**data)

        print('Data was inserted.')

    def generate_random_dataset(self):

        data = []

        for _ in range(100):
            anemometer = random.randint(1, 999)
            rainfall = random.randint(1, 999)
            humidity = random.randint(1, 999)

            # Simple storm logic: if at least two values are "high", it's a storm
            high_count = sum([
                anemometer > 333,
                rainfall > 333,
                humidity > 333
            ])

            is_storm_present = high_count >= 2

            entry = {
                "anemometer": anemometer,
                "rainfall": rainfall,
                "humidity": humidity,
                "is_storm_present": is_storm_present
            }

            data.append(entry)

        return data
