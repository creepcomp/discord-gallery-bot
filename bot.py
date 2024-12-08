import discord, aiohttp, os
from discord.ext import commands
from datetime import datetime

TOKEN = 'YOUR_BOT_TOKEN'
GALLERY_CHANNEL_ID = 123456789012345678  # Replace with your channel ID

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return None
            return await resp.read()

@bot.command(name='upload')
async def upload(ctx, image_url: str = None, *, description="No description provided"):
    if not image_url and not ctx.message.attachments:
        await ctx.send("Please provide an image URL or attach an image.")
        return

    if image_url:
        image_data = await download_image(image_url)
        if not image_data:
            await ctx.send("Failed to download the image. Please check the URL.")
            return
        
        with open("temp_image.jpg", "wb") as f:
            f.write(image_data)
        
        image_file = discord.File("temp_image.jpg", filename="image.jpg")
        uploaded_message = await ctx.send(file=image_file)
        os.remove("temp_image.jpg")
        image_url = uploaded_message.attachments[0].url
    else:
        image_url = ctx.message.attachments[0].url

    embed = discord.Embed(
        title="New Image Uploaded",
        description=f"**Uploaded by**: {ctx.author.mention}\n**Description**: {description}\n**Date**: {datetime.now():%Y-%m-%d %H:%M:%S}",
        color=discord.Color.blue()
    )
    embed.set_image(url=image_url)

    channel = bot.get_channel(GALLERY_CHANNEL_ID)
    if channel:
        await channel.send(embed=embed)
        await ctx.send(f"Image uploaded to {channel.mention}!")
    else:
        await ctx.send("The gallery channel does not exist.")

bot.run(TOKEN)
