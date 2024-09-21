#This script reads logs, filters threats, then displays the results.

def read_log(file_path):
    # open the log file with read access.  read and return content.
    with open(file_path,'r') as file:
        return file.readlines()

def filter_threats(log_lines):
    #create empty list to store suspicious entries
    suspicious_entries = []
    #iterate over lines in log searching for evidence of Failed root login, Suspicious Activity, or Failed login attempts.
    for line in log_lines:
        if "Failed root login" in line or "Suspicious activity" in line or "Failed login attempt" in line:
            #add suspicious entries to the list.
            suspicious_entries.append(line) #adding line to suspicious entries
    return suspicious_entries
def display_results(threats):
    #display each threat identified
    for threat in threats:
        print(threat)


#main loop
if __name__ == "__main__":
    log_file = 'access.log'
    log_data = read_log(log_file)
    threats = filter_threats(log_data)
    display_results(threats)

