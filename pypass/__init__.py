__VERSION__="0.1.0"

import hashlib
import os

def generate(salt, separator, hash_type, **kwargs):
    # Start the hash array.
    hash_array = [salt]
    # Add on any extra values from the input
    for key, value in kwargs.items():
        hash_array.append(value)
    # Get the hashing function.
    hash_func = getattr(hashlib, hash_type)()
    # Generate hash string.
    hash_string = separator.join(hash_array)
    
    hash_string=hash_string.encode(encoding="utf-8")
    # Update the hash function with the hash string.
    hash_func.update(hash_string)
    # Generate the hex digest to be used as the password.
    password = hash_func.hexdigest()
    # Return the password
    return password
    
def init(config_file = None):
    if config_file is None:
        config_file = os.path.join(os.path.expanduser("~"), ".config", "pypass.ini")
