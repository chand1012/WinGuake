from windowLib import write_to_log
import os

current_dir = os.getcwd()
temp_dir = os.getenv("TEMP")
write_to_log(current_dir, temp_dir)

print "Path successfully saved."
