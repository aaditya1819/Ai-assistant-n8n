import requests


user_message = "Use the Calendar tool to create a event.Title: Test Date: Tomorrow Start Time: 10:00 AM End Time: 11:00 AM After creating the event, confirm the event details."

request_message = {"message": user_message}

url = "https://aaditya1819k.app.n8n.cloud/webhook-test/5cf15705-3cc7-47fc-b5db-c829151b435d"

print(f"Sending request to: {url}")
try:
    response = requests.post(url, json=request_message)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0 and "output" in data[0]:
            print("Response output:")
            print(data[0]["output"])
        else:
            print("Received unexpected JSON format:")
            print(data)
    elif response.status_code == 404:
        print("Error: Webhook not found (404).")
        print("This usually means the n8n test webhook is not 'listening' or the URL is incorrect.")
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")