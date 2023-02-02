import json
import requests

def lambda_handler(event, context):
    # Slack API endpoint to send messages
    url = "https://hooks.slack.com/services/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"
    
    # Slack API token, can be found in your Slack App configuration
    token = "xapp-1-A04MJ0GT1U6-4735711038597-4c8a5705fc96a6866ebc9be0861cc7ca79e71ef44b48e08a67e4630ce75aa704"
    
    # The channel where you want to send the message
    channel = "#aws1"
    
    # The message you want to send
    message = "Hello from AWS Lambda!"
    
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    }
    
    payload = {
        "channel": channel,
        "text": message
    }
    
    # Send the message to Slack API
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Check if the message was sent successfully
    if response.status_code == 200:
        return {"statusCode": 200, "body": "Message sent successfully"}
    else:
        return {"statusCode": 400, "body": "Failed to send message"}
