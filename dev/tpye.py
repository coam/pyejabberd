from pyejabberd import EjabberdAPIClient
from pyejabberd.muc.enums import MUCRoomOption
from pyejabberd.muc.enums import Affiliation


# Create a client and authenticate with elevated user 'bob@example.com'
client = EjabberdAPIClient(host='47.90.15.40', port=4560, username='zyf', password='123456', user_domain='coopens.com',
                           protocol='http')

# Test the connection by sending an echo request to the server
sentence = 'some random data'
result = client.echo(sentence)
assert result == sentence

# Get a list of users that are on the server
registered_users = client.registered_users('coopens.com')
# result is in the format [{'username': 'bob', ...}]

print registered_users


# Get Bob's contacts
user_roster = client.get_roster(user='zyf', host='coopens.com')

print user_roster

# Register a new user
# client.register(user='alice', host='coopens.com', password='@l1cepwd')

# Change a password
#client.change_password(user='alice', host='coopens.com', newpass='newpwdd')

# Unregister a user
# client.unregister(user='alice', host='coopens.com')


# Create a muc room
# client.create_room(name='room7', service='conference.coopens.com', host='coopens.com')


# Set room option
# client.change_room_option(name='room2', service='conference.coopens.com', option=MUCRoomOption.persistent, value=True)


# Get muc rooms
# muc_online_rooms = client.muc_online_rooms()
# result is in the format ['room1@conference', ...] where 'conference' is the muc service name


# print muc_online_rooms



# Set room affiliation
# client.set_room_affiliation(name='room1', service='conference', jid='alice@example.com', affiliation=Affiliation.member)

# Get room affiliations
# affiliations = client.get_room_affiliations(name='room1', service='conference')

# Destroy a muc room
# client.destroy_room(name='room6', service='conference.coopens.com', host='coopens.com')
