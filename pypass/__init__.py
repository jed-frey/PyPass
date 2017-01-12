"""Naval Fate.

Usage:
  pypass  [--site=<site>] init
  pypass [--config=<config>] [--site=<site>] [--length=<len>] (<username> <website> | <email>)
  pypass --list
  pypass (-h | --help)
  pypass --version

Options:
  -h --help     Show this screen.  
  --version     Show version.
  --list        List supported hashlib algorithms
  -s <site>, --site=<site> Site category. [default: DEFAULT]
  -l <len>, --length=<len> Password lengths [default: 5,10,20,None].
  --verbose     Print 
"""
from __future__ import print_function
__VERSION__="0.1.0"

import hashlib
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
except:
    raise
    
import os
import stat
import sys

def generate(salt, separator, hash_type, *args):
    # Start the hash array.
    hash_array = [salt]
    # Add on any extra values from the input
    for value in args:
        hash_array.append(value)
    # Get the hashing function.
    hash_func = getattr(hashlib, hash_type)()
    # Generate hash string.
    hash_string = separator.join(hash_array)
    # Encode the string to a byte string.
    hash_string=hash_string.encode(encoding="utf-8")
    # Update the hash function with the hash string.
    hash_func.update(hash_string)
    # Generate the hex digest to be used as the password.
    password = hash_func.hexdigest()
    # Return the password
    return password

def init(config_file = None, site = None):
    if config_file is None:
        config_file = os.path.join(os.path.expanduser("~"), ".config", "pypass.ini")
    if site is None:
        site = "DEFAULT"

    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        config.read(config_file)

    config[site] = {"salt": "12345", # The same as my luggage
                    "separator": "|",
                    "hash": "sha256"}
            
    with open(config_file, 'w') as fid:
        config.write(fid)

    os.chmod(config_file, stat.S_IRUSR | stat.S_IWUSR)
    
def read_config(config_file = None, site=None):
    if config_file is None:
        config_file = os.path.join(os.path.expanduser("~"), ".config", "pypass.ini")

    if site is None:
        site = "DEFAULT"

    config = configparser.ConfigParser()
    config.read(config_file)
    return config[site]["salt"], config[site]["separator"], config[site]["hash"]
    
def main():
    from docopt import docopt
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    if arguments["--list"]:
        print("Available Hashing Algorithms:")
        for algorithms in hashlib.algorithms_guaranteed:
            print("\t"+algorithms)
        sys.exit(0)
    
    if arguments["init"]:
        init(arguments["--config"], arguments["--site"])
        sys.exit(0)

    if arguments["<email>"] is not None:
        salt, sep, hash = read_config(arguments["--config"], arguments["--site"])
        passwd = generate(salt, sep, hash, arguments["<email>"])
        # Print out various password lengths.
        print("Passwords:")
        for cut in [10, 20, len(passwd)]:
            print("Len{}: {}".format(cut, passwd[0:cut]))
        sys.exit(0)

    if (arguments["<username>"] is not None and arguments["<website>"] is not None):
        salt, sep, hash = read_config(arguments["--config"], arguments["--site"])
        passwd = generate(salt, sep, hash, arguments["<username>"], arguments["<website>"])
        # Print out various password lengths.
        print("Passwords:")
        for cut in [10, 20, len(passwd)]:
            print("Len{}: {}".format(cut, passwd[0:cut]))
        sys.exit(0)
    print(arguments)

def pong():
    print("Pong")

if __name__ == '__main__':
    main()
