class Logger:
    def log(self, message):
        pass
class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, 'a') as f:
            f.write(text + '\n')

class LogFileWriter(Logger, FileWriter):
    def __init__(self, filename):
        FileWriter.__init__(self, filename)

    def log(self, message):
        log_entry = f"[LOG FILE] {message}"
        self.write(log_entry)
        print(f"Logged to file: {message}")

logger = LogFileWriter("log.txt")
logger.log("System started successfully.")
logger.log("Error: cannot connect to database.")
