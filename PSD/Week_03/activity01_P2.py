# Week 3 - Activity 2: File Processing with Append
# Reads a file, prints the content, counts '*' characters,
# and then appends an "End of File" message to the file.

class FileProcessor:

    def __init__(self, filepath):
        # keep the file path stored for all methods
        self.filepath = filepath

    def read_file(self):
        try:
            # open in read mode, ignore weird characters if any
            with open(self.filepath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            return content

        except FileNotFoundError:
            return "Error: File not found."

    def count_stars(self, text):
        # count '*' in the whole text
        return text.count('*')

    def append_end_message(self):
        # open file in append mode so it doesnt overwrite anything
        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write("\n End of File ")

    def process(self):
        content = self.read_file()

        if content.startswith("Error"):
            print(content)
            return

        print("\n File Content")
        print(content)

        star_count = self.count_stars(content)
        print("\nNumber of '*' characters in the file:", star_count)

        # now append EOF message (Part 2)
        self.append_end_message()
        print("\n'End of File' message added to the file.")


if __name__ == "__main__":

    filepath = r"D:\YCCIA-MSE-2511\YCCIA-MSE-2511\PSD\Week_03\demo_file.txt"
    

    processor = FileProcessor(filepath)
    processor.process()
