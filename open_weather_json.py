import datetime
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve(strict=True).parent


class DataSource:
    def read(self, **kwargs):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(kwargs['file_name']), 'r') as file:
            json_data = json.load(file)

            for row in json_data['hourly']:
                hour = datetime.datetime.fromtimestamp(row['dt']).isoformat()
                temperature = float(row['temp'])
                temperatures_by_hour[hour] = temperature
        return temperatures_by_hour



