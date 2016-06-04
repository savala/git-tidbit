import sys
sys.path.append('Snapple')
sys.path.append('Email')

from termcolor import colored
from snapple_service import *
from fetchEmail import *
from setup import *
from datetime import *


service = SnappleFactService()
tidbit = service.get_tidbit()
mailService = setup.get_credentials()
email = fetchEmail.getEmails(mailService, datetime.now())

print ""
print colored(tidbit, 'green')
print colored(email, 'red')
