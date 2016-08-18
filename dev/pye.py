#!/usr/bin/env python
# coding=utf-8
from pyejabberd import EjabberdAPIClient

# Create a client and authenticate with elevated user 'bob@coopens.com'
client = EjabberdAPIClient(host='47.90.15.40', port=4560, username='zyf', password='123456', user_domain='coopens.com',
                           protocol='http',verbose=1)

# Test the connection by sending an echo request to the server
sentence = 'some random data'
result = client.echo(sentence)
print result
assert result == sentence

# Get a list of users that are on the server
# registered_users = client.registered_users('coopens.com')
# result is in the format [{'username': 'bob', ...}]

# Register a new user
# client.register(user='zyfers', host='coopens.com', password='12345678')
# client.unregister(user='zyfers', host='coopens.com')

# # Change a password
# client.change_password(user='zyfer', host='coopens.com', newpass='123456')
#
# # Verify password
# assert client.check_password_hash(user='zlh', host='coopens.com', password='123456') is True
#
# # Set nickname
# client.set_nickname(user='zlh', host='coopens.com', nickname='Bob the builder')
#
# # Get Bob's contacts
client.get_roster(user='zyf', host='coopens.com')

#
# # Add Alice to Bob's contact group Friends
# client.add_rosteritem(localuser='zlh', localserver='coopens.com', user='zyf', server='coopens.com',
#                       nick='Alice from Wonderland', group='Friends', subs='both')
#
# # Delete Alice from Bob's contacts
# client.delete_rosteritem(localuser='zlh', localserver='coopens.com', user='zyf', server='coopens.com')
#
# # Get list of *all* connected users
# print client.connected_users()

#
# # Get list of *all* connected users and information about their sessions
# client.connected_users_info()
#
# # Get number of connected users
# print client.connected_users_number()
#
# # Get information for all sessions for a user
# print client.user_sessions_info(user="zyf", host="coopens.com")
#
# # Get muc rooms
# muc_online_rooms = client.muc_online_rooms()
# print(muc_online_rooms)
# # result is in the format ['room1@conference', ...] where 'conference' is the muc service name
#
# # Create a muc room
# client.create_room(name='room1', service='conference', host='coopens.com')
#
# # Get room options
# room_options = client.get_room_options(name='g', service='conference')
# print(room_options)
#
# # Set room option
# from pyejabberd.muc.enums import MUCRoomOption
#
# client.change_room_option(name='room1', service='conference', option=MUCRoomOption.public, value=False)
# client.change_room_option(name='room1', service='conference', option=MUCRoomOption.members_only, value=True)
#
# # Set room affiliation
# from pyejabberd.muc.enums import Affiliation
#
# client.set_room_affiliation(name='room1', service='conference', jid='zyf@coopens.com', affiliation=Affiliation.member)
#
# # Get room affiliations
# affiliations = client.get_room_affiliations(name='room1', service='conference')
#
# # Destroy a muc room
# client.destroy_room(name='room1', service='conference', host='coopens.com')
#
# # Unregister a user
# client.unregister(user='zyf', host='coopens.com')
