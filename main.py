from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 13356656
api_hash = "304ec89622dc2ede528971d19f14087b"
phone = "+994707909291"

# List of source channels that you want to get messages from
source_channel_names = ['main bitches']

# The channel/Group that you want to send messages to
destination_channel_link = -1001874052676

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code:'))


@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title in source_channel_names:
            message = event.message

            # Check if the message contains specific strings
            if "- Binance Killers®" in message.text and "BK® Crypto Fear and Greed Index" in message.text:
                # Replace the strings
                modified_text = message.text.replace("- Binance Killers®", "- Crypto Moon®").replace("BK®", "CM®")

                # Send the modified message with attached media (if any)
                await client.send_message(entity=destination_channel_link, message=modified_text, file=message.media)
            elif "- Binance Killers®" in message.text and "VIP Crypto Market RSI Heatmap" in message.text and "Timeframe: Daily" in message.text:
                # Replace the strings
                modified_text = message.text.replace("- Binance Killers®", "- Crypto Moon®").replace("VIP", "CM®")

                # Send the modified message with attached media (if any)
                await client.send_message(entity=destination_channel_link, message=modified_text, file=message.media)

            elif "- Binance Killers®" in message.text and "1) Open Interest" in message.text:
                # Replace the strings
                modified_text = message.text.replace("- Binance Killers®", "- Crypto Moon®").replace("VIP", "CM®")
                # Send the modified message with attached media (if any)
                await client.send_message(entity=destination_channel_link, message=modified_text, file=message.media)


            elif "- Binance Killers®" in message.text and "MARKET ANALYSIS:" in message.text and "Market Cap:" in message.text:
                # Split the message into lines
                lines = message.text.split('\n')
                # Join the first 32 lines and replace the required string
                modified_text = '\n'.join(lines[:32]).replace("- Binance Killers®", "- Crypto Moon®").replace("BK®",
                                                                                                              "CM®")
                # Add the desired line at the end of the message
                modified_text += "\n➖➖➖➖➖➖➖\n- Crypto Moon"
                # Send the modified message with attached media (if any)
                await client.send_message(entity=destination_channel_link, message=modified_text, file=message.media)

    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit


client.start()
client.run_until_disconnected()
