
import json
import os

def generate_report():
    report = []
    with open("logs/shark_attack_log.txt", "r") as log_file:
        for line in log_file:
            report.append(line.strip())
    
    with open("logs/report.json", "w") as json_file:
        json.dump(report, json_file, indent=4)
    
    print("Report generated: logs/report.json")
