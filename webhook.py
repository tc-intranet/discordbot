from discord_webhook import DiscordWebhook
import sys
a_input = sys.argv[1]
print(a_input)
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/543009863291371520/mlEevJu_fWBeLwcK1xoqX68R7WTXAU-RJfYQ9xVdl-VqQpK3FXCoOf_rj4w-NsfXvRW-', content=a_input)
webhook.execute()