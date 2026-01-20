import json
import argparse

class LogAnalyzer:

    def __init__(self, input_log_file, output_json_file):
        self.input_log_file = input_log_file
        self.output_json_file = output_json_file
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "UNKNOWN": 0}

    def read_logs(self):
        with open(self.input_log_file,"r") as input_file:
            return input_file.readlines()
    
    def write_logs(self,counts):
        with open(self.output_json_file,"w+") as output_file:
            json.dump(counts,output_file,indent=4)

    def log_analyze(self, lines):
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
            else:
                self.counts["UNKNOWN"] += 1
        return self.counts                          #Here Returing the final counts of avaialble logs to self.counts
    

def main():
   #Creating parser
   parser = argparse.ArgumentParser(description="Process the log file and generate the summary to output file and terminal.")

   #Adding Arguments
   parser.add_argument("--file", type=str, required=True, help="Path of the input log file (e.g app.log)")
   parser.add_argument("--out", type=str, required=True, help="Path of the output summary file (e.g summary.txt)")

   # Parse the arguments
   args = parser.parse_args()

   # Access the arguments
   input_file = args.file
   output_file = args.out

   analyzer = LogAnalyzer(input_file,output_file)
   lines = analyzer.read_logs()

   if not lines:
        print("No logs to analyze.")
        return

   result = analyzer.log_analyze(lines)        #Analyzing the logs and put into reult

   print("Log Analysis Summary:")
   for level, count in result.items():
        print(f"{level}: {count}")
    
   analyzer.write_logs(result)  #Writing the JSON file for logs


if __name__ == "__main__":
    main()