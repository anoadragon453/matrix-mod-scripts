#!/usr/bin/env python3
import requests
import json
from urllib.parse import quote as encode_as_url

holding_room = "!holding:example.com"

aliases = [
    "#something:example.com",
]

hs_url = "https://matrix.example.com"

removal_failures = []
adding_failures = []

# Authorization header
access_token = ""
auth_headers = {"Authorization": "Bearer %s" % access_token}

for alias in aliases:
    encoded_alias = encode_as_url(alias)

    url = "%s/_matrix/client/r0/directory/room/%s" % (hs_url, encoded_alias)

    # Remove the alias from the room
    r = requests.delete(url, headers=auth_headers)

    if r.status_code != 200:
        print("Error removing alias", alias, r.content)
        print("Continuing...")
        removal_failures.append(alias)
        continue

    # Add the alias to the holding room
    r = requests.put(
        url,
        data=json.dumps({"room_id": holding_room}),
        headers=auth_headers,
    )

    if r.status_code != 200:
        print("Error adding alias", alias, r.content)
        adding_failures.append(alias)
        continue

    print("Transferred", alias)

if removal_failures:
    print("Aliases still attached to the room:", removal_failures)

if adding_failures:
    print(
        "Aliases that are currently unassigned(!) (removed but not added to holding "
        "room):", adding_failures
    )

if not removal_failures and not adding_failures:
    print("Successfully transferred all aliases")
