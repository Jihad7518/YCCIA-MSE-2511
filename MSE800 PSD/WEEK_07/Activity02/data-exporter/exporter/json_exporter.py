import json
from exporter.exporter import DataExporter

class JSONExporter(DataExporter):
    def export(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Data exported to JSON successfully")
