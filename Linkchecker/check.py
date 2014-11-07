#!/usr/bin/python
import os
import re
import subprocess
import sys
import time

# Gather our code in a main() function
def main():
  # print 'Number of arguments: ', len(sys.argv)
  if(len(sys.argv) == 1):
    print "No site specified"
    sys.exit(1)

  url = sys.argv[1]
  time_stamp = time.strftime("%Y%m%d%H%M%S")
  scan_target = url.replace("http://", "")
  dir_name = "%s_%s" % (scan_target, time_stamp)
  dir_name = re.sub(r'[^A-Za-z0-9\.]', '', dir_name)

  bin_path = "linkchecker"
  command = "%s --file-output=csv --file-output=html %s" % (bin_path, url)
  command = [bin_path, "--complete", "--file-output=csv", "--file-output=html", url]
  os.mkdir(dir_name)
  os.chdir(dir_name)
  result = subprocess.call(command)
  print result

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()