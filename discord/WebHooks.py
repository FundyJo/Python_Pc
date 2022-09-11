import requests

WebHookUrl = "https://canary.discord.com/api/webhooks/1007322006183760064/jKHVgWqAFNKvRCf4MXcEIeeuB0yOkaFDhgO0WNmYN3q4ayI54MqNxEltKu5Ju2Mhr5kz"

Json = {
  "embeds": [
    {
      "color": 3092790,
      "fields": [
        {
          "name": "CredeBot",
          "value": "--TOKEN--"
        },
        {
          "name": "CredeBot Canary",
          "value": "--TOKEN--"
        },
        {
          "name": "CredeBot Development",
          "value": "--TOKEN--"
        }
      ],
      "footer": {
        "text": "Powered by CredeBot"
      }
    }
  ]
}

try:
  requests.post(WebHookUrl, json=Json)
except:
  print("ERROR")
