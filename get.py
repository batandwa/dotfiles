#!/usr/bin/python

# Run with:
#   python hello.py cameron
#   python hello.py


# import modules used here -- sys is a very standard one
import os
import shutil

# Gather our code in a main() function
def main():
  files = [line.rstrip() for line in open('files.txt')]
  for f in files:
    cwd = os.getcwd()
    src = os.path.abspath(cwd+'/../'+f)
    dest = os.path.abspath("%s/%s" % (cwd, f))
    print src + " ==> " + dest
    try:
      recursive_overwrite(src, dest)
    except IOError as e:
      print e

    # if(os.path.isdir(f)):
    #   # shutil.copytree(os.path.abspath('../'+f), "%s/%s" % (cwd, f))
    # else:
    #   shutil.copy(os.path.abspath('../'+f), "%s/%s" % (cwd, f))
    # # shutil.copy(os.path.abspath(f), "%s/%s" % (cwd, f))

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)
    else:
        if(not os.path.isdir(os.path.dirname(dest))):
            os.makedirs(os.path.dirname(dest))
        shutil.copyfile(src, dest)
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
