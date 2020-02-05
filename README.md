# Matrix Mod Scripts

A collection of scripts to help moderate a matrix server.

## move-aliases.py

Move aliases from one room to another. You must use an admin access_token for
the server that owns the aliases.

Fill in the aliases you want to move. Fill in the room that the aliases will be
moved to. Fill in the access token.

NOTE: This will remove the aliases on the server without sending events into
the room, thus clients will not know about the change and thus clicking a link
in a client that's already mapped this alias will still be taken to the old
room.

```
python ./move-aliases.py
```
