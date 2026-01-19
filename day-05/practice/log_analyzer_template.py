import json

class LogAnalyzer:

    def __init__(self, input_file_name, output_file_name):
        self.input_file = input_file_name
        self.output_file = output_file_name


    def read_logs(self):
        with open(self.input_file,"r") as file:
            return file.readlines()
    
    def write_logs(self,counts):
        with open(self.output_file,"w+") as json_file:
            json.dump(counts,json_file,indent=4)
        
    def log_analyze(self):
        log_count = {
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }
        lines = self.read_logs()
        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"]+1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"]+1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"]+1})
            else:
                pass
        self.write_logs(log_count)



log1 = LogAnalyzer("app.log","output.json")
log_count = log1.log_analyze()