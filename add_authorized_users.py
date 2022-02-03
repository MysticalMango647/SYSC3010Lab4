from backend import Backend
from mydbconfig import *
backend = Backend(config, email, firstname, lastname)

backend.add_authorized_users('yunasmagsi@cmail.carleton.ca')
backend.add_authorized_users('flynngraham@cmail.carleton.ca')
