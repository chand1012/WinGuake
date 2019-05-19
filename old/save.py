from windowLib import write_to_log
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()
write_to_log(current_dir, script_dir)

print "Path successfully saved."
