import xml.etree.ElementTree as ET
from exporter.exporter import DataExporter

class XMLExporter(DataExporter):
    def export(self, data, filename):
        root = ET.Element("dataset")

        for item in data:
            record = ET.SubElement(root, "record")
            for key, value in item.items():
                element = ET.SubElement(record, key)
                element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)

        print("✅ Data exported to XML successfully")
