from data import data
from exporter.factory import ExporterFactory

def main():
    format_type = input("Choose export format (csv/json/xml): ").lower()
    exporter = ExporterFactory.get_exporter(format_type)

    filename = f"output.{format_type}"
    exporter.export(data, filename)

if __name__ == "__main__":
    main()
