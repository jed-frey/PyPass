from pypass import generate

def test_uuid():
    import uuid
    test_uuid=uuid.uuid4()
    print(test_uuid)
    return test_uuid
    
def test_password0():
     # "Password" to remember to salt the password generation.
    salt = "12345"
    # String to separate parts parts of the hash string.
    separator = ""
    hash_type = "sha256"
    known_password="5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
    # echo -n 12345 | sha256sum
    assert known_password == generate(salt=salt,
                                  separator=separator,
                                  hash_type=hash_type)
                                  
def test_password1():
    # "Password" to remember to salt the password generation.
    salt = "12345"
    # String to separate parts parts of the hash string.
    separator = "&"
    # Email login.
    email = "skroob@spaceball.gov"
    # https://en.wikipedia.org/wiki/Secure_Hash_Algorithm
    hash_type = "sha256"
    known_password = "d9c9f2f4469fac0870ef4d798e962f18590a19276962ab52e854b0fc756990a2"
    #  echo -n "12345&skroob@spaceball.gov" | sha256sum
    assert known_password == generate(salt=salt,
                                      separator=separator,
                                      hash_type=hash_type,
                                      email=email)