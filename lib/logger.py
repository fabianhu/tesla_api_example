# implement a logger, so that tesla_api can log messages
# this does direct file logging

import datetime
import sys

class Logger:
    def __init__(self, depth, log_file):
        self.depth = depth
        self.log_file = log_file
        self.log_file_handle = None
        self.log_file_handle = open(self.log_file, "a")
        self.log_file_handle.write("########### Logging started at " + str(datetime.datetime.now()) + "\n")

    def log(self, message):
        self.log_file_handle.write(str(datetime.datetime.now()) + " " + message + "\n")
        self.log_file_handle.flush()
        print("log" , message)
        sys.stdout.flush()

    def error(self, message):
        self.log("Error " + message)

    def info(self, message):
        self.log("Info " + message)

    def debug(self, message):
        self.log("Debug " + message)


    def __del__(self):
        if self.log_file_handle is not None:
            self.log_file_handle.close()



