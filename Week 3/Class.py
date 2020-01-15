class FileReader():
    def __init__(self,way):
        self.way=way
    def reader(self):
        try:
            with open(self.way,"r") as file:
                return file.read()
        except FileNotFoundError:
            print("Файл не найден")
f=FileReader("storage5.data")
f.reader()