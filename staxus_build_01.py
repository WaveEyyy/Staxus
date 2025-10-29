import discord
from discord.ext import commands
from discord import app_commands
import aiosqlite
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.presences = True  # Track game activity
intents.members = True    # Identify users
intents.guilds = True
intents.message_content = True  # Required for commands

bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree  # For slash commands
DB_PATH = "plays.db"
YOUR_ID = 1234545846024694  # Insert Your Discord ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS plays (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                game_name TEXT,
                timestamp DATETIME
            )
        ''')
        await db.commit()
    await tree.sync()  # Sync slash commands
    print("Database initialized and slash commands synced.")

@bot.event
async def on_presence_update(before, after):
    if after.id != YOUR_ID:
        return

    before_game = before.activity.name if before.activity and before.activity.type == discord.ActivityType.playing else None
    after_game = after.activity.name if after.activity and after.activity.type == discord.ActivityType.playing else None

    if after_game and after_game != before_game:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO plays (user_id, game_name, timestamp) VALUES (?, ?, ?)",
                (after.id, after_game, datetime.utcnow())
            )
            await db.commit()
        print(f"Logged game: {after_game} at {datetime.utcnow()}")

@tree.command(name="weekly", description="Shows how many times you've played each game this week")
async def weekly(interaction: discord.Interaction):
    one_week_ago = datetime.utcnow() - timedelta(days=7)
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('''
            SELECT game_name, COUNT(*) 
            FROM plays 
            WHERE user_id = ? AND timestamp >= ? 
            GROUP BY game_name
        ''', (interaction.user.id, one_week_ago)) as cursor:
            rows = await cursor.fetchall()

    if not rows:
        await interaction.response.send_message("No game activity found this week.", ephemeral=True)
        return

    msg = "**🎮 Weekly Game Tracker:**\n"
    for game, count in rows:
        msg += f"• {game}: {count} times\n"

    await interaction.response.send_message(msg)

bot.run("INSERT_YOUR_BOT_TOKEN_HERE")