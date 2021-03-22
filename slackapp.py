from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
import time
import os

slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_client = WebClient(slack_bot_token)

channelPrimary = os.environ.get("CHANNEL_ID")
def post_announcement(confirmation, channel):
    slack_client.chat_postMessage(channel=channel, text=confirmation)
    announcement = confirmation.replace("Broadcasting:\n", "")
    while True:
        try:
            f = open("temp.txt", "x")
        except:
            time.sleep(30)
            continue
        f.write(announcement)
        f.close()
        break
    return 0

# Example responder to greetings
@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    message = event_data["event"]
    if message.get('type') == "app_mention":
        print("app has been mentioned")
        confirmation = message.get('text').replace("<@" + os.environ.get("BOT_USER_ID") + ">", "Broadcasting:\n")
        channel = message["channel"]
        post_announcement(confirmation, channel)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)