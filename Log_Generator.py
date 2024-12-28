import time
import random
import string
import logging

# setting up logging for error handling
logging.basicConfig(filename="log_errors.log", level=logging.ERROR)

# list the level of logs
LOG_LEVEL = ["INFO", "DEBUG", "ERROR", "WARNING"]

# list of possible actions
ACTIONS = ["Login", "Logout", "Data Request", "file Upload", "Download", "Error"];

# function to generate random strings for logs
def generate_random_string(length=10):
    """
        function generate randome strigns referred as user name
    """
    try:
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))
    except Exception as e:
        logging.error(f"Error in generate_random_string: {e}")
        return "ERROR"

# function to generate a random log entry
def generate_log_entry():
    """
        function generates random log entries
    """
    try:
        log_level = random.choice(LOG_LEVEL)
        timestamp = time.strftime("%Y-%m-%D %H:%M:%S", time.gmtime())
        action = random.choice(ACTIONS)
        user = generate_random_string(8)
        log_entry = f"{timestamp} - {log_level} - {action} - user: {user}"
        return log_entry
    except Exception as e:
        logging.error(f"Error iin generate_log_entry {e}")
        return "ERROR"

# function to write logs to a text file
def write_logs_to_a_file(log_filename, num_entries=100):
    """
        function writes logs to file
    """
    try:
        with open(log_filename, 'w') as file:
            for _ in range(num_entries):
                log = generate_log_entry()
                if log != "ERROR":
                    file.write(log + "\n")
        print(f"logs have been successfully writen to {log_filename}")
    except Exception as e:
        logging.error(f"Error while writing to a file {e}")
        print("Error occured while writing to a file");

# Execute file
write_logs_to_a_file(log_filename="log_generator_errors.txt", num_entries=1000);