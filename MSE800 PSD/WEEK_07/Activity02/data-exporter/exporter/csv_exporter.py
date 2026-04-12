import csv
from exporter.exporter import DataExporter

class CSVExporter(DataExporter):
    def export(self, data, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print("✅ Data exported to CSV successfully")
