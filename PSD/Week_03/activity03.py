# Week 3 - Activity 1: File Processing (OOP Version)
# Reads a file, prints its content, and counts '*' characters.

class FileProcessor:

    def __init__(self, filepath):
        # store the file path so the other methods can use it
        self.filepath = filepath

    def read_file(self):
        try:
            # open the file safely (utf-8 so Windows won't complain)
            with open(self.filepath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()  # read everything at once
            return content
        except FileNotFoundError:
            return "Error: File not found."

    def count_stars(self, text):
        # count how many "*" appear in the file
        return text.count('*')

    def process(self):
        content = self.read_file()

        if content.startswith("Error"):
            print(content)
            return

        print("\n File Content")
        print(content)  # print the actual text from the file

        star_count = self.count_stars(content)
        print("\nNumber of '*' characters in the file:", star_count)


if __name__ == "__main__":

    filepath = r".\Week_03\demo_file.txt"

    processor = FileProcessor(filepath)  # create object
    processor.process()                  # run the whole workflow