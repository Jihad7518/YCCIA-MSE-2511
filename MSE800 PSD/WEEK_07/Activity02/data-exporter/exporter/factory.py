from exporter.csv_exporter import CSVExporter
from exporter.json_exporter import JSONExporter
from exporter.xml_exporter import XMLExporter

class ExporterFactory:
    @staticmethod
    def get_exporter(format_type: str):
        if format_type == "csv":
            return CSVExporter()
        elif format_type == "json":
            return JSONExporter()
        elif format_type == "xml":
            return XMLExporter()
        else:
            raise ValueError("Unsupported export format")
