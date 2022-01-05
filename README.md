# Slackcord
## An app to communicate between Slack workspaces and Discord servers
### Purpose:
My robotics team mainly uses Slack for team-wide communication, but the programming subteam also uses Discord as it provides a space to coordinate more specific plans.

Because announcements are placed in both Slack and Discord, I wanted to make an app that allows for the programming captains to announce in Slack and have the message sent to Discord, or vice-versa.

### Software Used:
Discord.py

Slack's Bolt API for Python

Text files

### Current Issues/State of the Project
This project is certainly a work in progress. As of right now, I have both bots running concurrently, but I am unable to find a way for the two bots to communicate. 

As of right now, in the beginning stages, I simply want one bot to receive a message with a certain condition, take that message and create a text file with it, then have the other bot search for text files at a certain interval, and when it sees that one has been created, take the message and post it before deleting the file.

The main obstacle here is each API runs on these sort of event things, so I am unable to run a while loop in one of the bots.

A potential solution is to check for text files whenever any new message is sent, but there isn't a guarantee that a message will be sent on time.

I am new to the Slack API, so bear with me as I try to find a solution.

### Plans for the distant future
1. Migrate from Discord.py to a fork, as it is currently outdated.
2. Have a more sophisticated data system (ex: PostgreSQL)