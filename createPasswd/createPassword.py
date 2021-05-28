import base64 ,os ,crypt, getpass;

print crypt.crypt(getpass.getpass(), "$6$"+base64.b64encode(os.urandom(16))+"$")
