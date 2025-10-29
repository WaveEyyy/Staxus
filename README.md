🎮 Staxus — Game Activity Tracker Bot
Staxus is a personal Discord bot that automatically tracks what games you play each week and shows your stats using simple commands.
It’s designed for gamers who want to keep an eye on their gaming habits without any setup hassle.


⚙️ Features
🧠 Automatic tracking — logs your game activity whenever you start playing.
📅 Weekly stats — use /weekly to see how many times you’ve played each game in the past 7 days.
💾 SQLite database — lightweight local data storage (no external servers).
🔒 Private setup — perfect for your own server or a small group of friends.


🚀 Getting Started (Very Easy)
1. Clone or download this repository

git clone https://github.com/WaveEyyy/staxus.git
cd staxus

2. Open "staxus_build_01.py" file with an IDE (Visual Studio Code or similar)

Replace INSERT_YOUR_BOT_TOKEN with your actual bot token. (Generated from Discord's developer portal after you've created an application)

Replace INSERT_YOUR_ID with your Discord user ID. (Turn on Developer Mode in Advanced Settings on Discord to get your ID)

3. Save the python file and run it in CMD or Terminal
python staxus_build_01.py


4. Invite it to your server
Go to the Discord Developer Portal
Open your application/bot → OAuth2 → OAuth2 URL Generator
Under Scopes, select "bot" and "applications.commands"

Under Bot Permissions, enable the following permissions:
View Channels
Send Messages
Manage Messages
Embed Links
Read Message History
Use Slash Commands

Copy the generated URL from below and paste it in your browser and invite Staxus to your server.

🧩 Commands
/weekly	Shows how many times you played each game in the last 7 days

📁 Database
The bot uses a local SQLite database (plays.db) that stores:
Your Discord user ID
Game Name
Timestamp of each play session

🛠 Requirements
Python 3.8 or higher
Libraries:
pip install discord.py aiosqlite

📜 License
This project is licensed under the MIT License
.

💡 Credits
Developed with 💙 by WAVEEYYY at (Nexus Labs)
Discord bot concept and code logic inspired by love for gaming and automation.
