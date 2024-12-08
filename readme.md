# Discord Gallery Bot

A Discord bot that allows users to upload images from a URL or as an attachment and automatically shares them in a designated gallery channel. Each uploaded image is displayed with a custom description, the uploader’s username, and the timestamp of the upload.

## Features
- **Upload images** via a URL or as an attachment.
- **Embed generation** with metadata (uploader, description, upload date).
- **Automatic image sharing** to a specified gallery channel.
- **Customizable description** for each image upload.
- Easy setup and straightforward usage.

## Prerequisites
Before running this bot, ensure you have the following installed on your system:
- **Python 3.8+**: The latest Python 3.x version is recommended.
- **`discord.py` library**: For interacting with Discord’s API. Install with:
  ```bash
  pip install discord.py
  ```
- **`aiohttp` library**: For making asynchronous HTTP requests. Install with:
  ```bash
  pip install aiohttp
  ```

## Installation
Follow these steps to set up and run the bot:

### 1. Clone the repository
```bash
git clone https://github.com/creepcomp/discord-gallery-bot.git
```

### 2. Navigate to the project directory
```bash
cd discord-gallery-bot
```

### 3. Install the required Python packages
```bash
pip install -r requirements.txt
```

### 4. Configure the bot
- Open the `bot.py` file and replace:
  - `YOUR_BOT_TOKEN` with your actual Discord bot token.
  - `GALLERY_CHANNEL_ID` with the ID of the Discord channel where images will be posted.

### 5. Run the bot
```bash
python bot.py
```

## Usage
Once the bot is running, you can use the `!upload` command to upload an image to the gallery channel.

### Command Syntax
```
!upload <image_url> [description]
```
- **`image_url`**: The URL of the image to upload (optional if attaching).
- **`description`**: A custom description for the image (optional).

### Example Commands
- Upload an image from a URL:
  ```
  !upload https://example.com/image.jpg A beautiful sunset over the mountains.
  ```

- Attach an image directly and add a description:
  ```
  (Attach an image) !upload A scenic view of the beach.
  ```

## How It Works
1. **Upload Command**: The bot listens for the `!upload` command.
2. **Image Download**: If a URL is provided, the bot downloads the image.
3. **Temporary File Creation**: The image is stored temporarily before uploading to Discord.
4. **Embed Creation**: An embed is generated containing the image, the uploader's information, and a timestamp.
5. **Channel Posting**: The embed is sent to the designated gallery channel.

## Customization
- You can customize the bot's command prefix by changing `command_prefix="!"` in the `commands.Bot()` constructor.
- Modify the `GALLERY_CHANNEL_ID` in `bot.py` to point to the desired channel.

## Troubleshooting
- **"Failed to download the image" error**: Ensure the URL is valid and accessible.
- **Bot not posting to the gallery channel**: Check that the `GALLERY_CHANNEL_ID` is correct and that the bot has permissions to post messages in that channel.

## Security Note
Do not share your bot token in public repositories or with others. Keep your token secure to prevent unauthorized access to your bot.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [discord.py documentation](https://discordpy.readthedocs.io/)
- [aiohttp documentation](https://docs.aiohttp.org/en/stable/)

## Author
- **Parsa Rostamzadeh (Creepcomp)**
- **GitHub**: [creepcomp](https://github.com/creepcomp)

## Support
If you encounter any issues or have questions, feel free to create an issue in the [Issues](https://github.com/creepcomp/discord-gallery-bot/issues) section of the repository.
