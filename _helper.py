


class FileReader:
    @staticmethod
    def read_line(path: str):
        lines = []
        with open(path, "r") as file:
            while (line := file.readline()):
                lines.append(line[:-1])
        return lines