import os
import discord
from discord.ext import tasks
from server import keep_alive
from discord import app_commands
import asyncio
import random
import re
import aiohttp
import asyncio
import io

# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()  # デフォルトのIntentsオブジェクトを生成
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class SampleView(discord.ui.View):  # UIキットを利用するためにdiscord.ui.Viewを継承する

  def __init__(self, timeout=180):  # Viewにはtimeoutがあり、初期値は180(s)である
    super().__init__(timeout=timeout)

    @discord.ui.button(label="グー", style=discord.ButtonStyle.success)
    async def guu(self, button: discord.ui.Button,
                  interaction: discord.Interaction):
      jite = random.randint(0, 2)
      view = SampleView(timeout=None)
      if jite == 0:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、グーを出しました！\nあいこです！", view=view)
      elif jite == 1:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、チョキを出しました！\nあなたの勝ちです！", view=view)
      elif jite == 2:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、パーを出しました！\nあなたの負けです！", view=view)

    @discord.ui.button(label="チョキ", style=discord.ButtonStyle.success)
    async def tyoki(self, button: discord.ui.Button,
                    interaction: discord.Interaction):
      jite = random.randint(0, 2)
      view = SampleView(timeout=None)
      if jite == 0:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、グーを出しました！\nあなたの負けです！", view=view)
      elif jite == 1:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、チョキを出しました！\nあいこです！", view=view)
      elif jite == 2:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、パーを出しました！\nあなたの勝ちです！", view=view)

    @discord.ui.button(label="パー", style=discord.ButtonStyle.success)
    async def paa(self, button: discord.ui.Button,
                  interaction: discord.Interaction):
      jite = random.randint(0, 2)
      view = SampleView(timeout=None)
      if jite == 0:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、グーを出しました！\nあなたの勝ちです！", view=view)
      elif jite == 1:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、チョキを出しました！\nあなたの負けです！", view=view)
      elif jite == 2:
        await interaction.response.send_message(
          "じゃんけんぽん！\n私は、パーを出しました！\nあいこです！", view=view)


@tree.command(name="ott", description="rock paper scissors one two three")
@discord.app_commands.choices(text=[
  discord.app_commands.Choice(name="グー", value="0"),
  discord.app_commands.Choice(name="チョキ", value="1"),
  discord.app_commands.Choice(name="パー", value="2")
])
async def jannkenn(interaction: discord.Interaction, text: str):
  te = int(text)
  jite = random.randint(0, 2)
  view = SampleView(timeout=None)
  if (te == 0) and (jite == 0):
    await interaction.response.send_message("じゃんけんぽん！\n私は、グーを出しました！\nあいこです！",
                                            view=view)
  elif (te == 0) and (jite == 1):
    await interaction.response.send_message(
      "じゃんけんぽん！\n私は、チョキを出しました！\nあなたの勝ちです！", view=view)
  elif (te == 0) and (jite == 2):
    await interaction.response.send_message(
      "じゃんけんぽん！\n私は、パーを出しました！\nあなたの負けです！", view=view)
  elif (te == 1) and (jite == 0):
    await interaction.response.send_message(
      "じゃんけんぽん！\n私は、グーを出しました！\nあなたの負けです！", view=view)
  elif (te == 1) and (jite == 1):
    await interaction.response.send_message("じゃんけんぽん！\n私は、チョキを出しました！\nあいこです！",
                                            view=view)
  elif (te == 1) and (jite == 2):
    await interaction.response.send_message(
      "じゃんけんぽん！\n私は、パーを出しました！\nあなたの勝ちです！", view=view)
  elif (te == 2) and (jite == 0):
    await interaction.response.send_message(
      "じゃんけんぽん！\n私は、グーを出しました！\nあなたの勝ちです！", view=view)
  elif (te == 2) and (jite == 1):
    await interaction.response.send_message(
      "じゃんけんぽん！\n私は、チョキを出しました！\nあなたの負けです！", view=view)
  elif (te == 2) and (jite == 2):
    await interaction.response.send_message("じゃんけんぽん！\n私は、パーを出しました！\nあいこです！",
                                            view=view)
  else:
    await interaction.response.send_message("何かがおかしいぞ！ｗ", view=view)


@client.event
async def on_message(message):
  if message.author.id == 562987075326967809:
      if message.channel.id != 1124309484764930151:
          await message.delete()
          
  if message.author.id == 1005468573545799753:
      if message.channel.id != 1127002054557192304:
          await message.delete()

@client.event
async def on_ready():
  print('Ready!')
  await tree.sync()  #スラッシュコマンドを同期
  myLoop.start()
  myLoop2.start()


@tasks.loop(seconds=60)  # repeat after every 10 seconds
async def myLoop():
  # work
  guild = client.get_guild(1124309483703763025)
  channel = guild.get_channel(1126754189331148841)
  member_count = len([guild.member_count for m in guild.members
                      if not m.bot])  # doesn't include bots
  print("Member Count: {}".format(member_count))
  await channel.edit(name="Member Count: {}".format(member_count))

  channel = guild.get_channel(1126754191986151444)
  member_count = len([guild.member_count for m in guild.members
                      if m.bot])  # Include bots
  await channel.edit(name="Bot Count: {}".format(member_count))

  channel = guild.get_channel(1142373728525746207)
  count = 0  #put these at the beginning of your command so it will reset every time, otherwise, your starting number would be the sum of all earlier commands
  for member in guild.members:  #you forgot to get members
    if member.status != discord.Status.offline:
      count += 1  #you can't use "= +1" - "+= 1" is correct
  await channel.edit(name="Online Member Count: {}".format(count))
  print('It works!')


@tasks.loop(seconds=20)  # repeat after every 10 seconds
async def myLoop2():
  # work
  await client.change_presence(activity=discord.Game(
    name="☕猫の喫茶店でメイドとして勤務中 / https://discord.gg/aEEt8FgYBb"))


TOKEN = os.getenv("discord")
keep_alive()
try:
  client.run(TOKEN)
except:
  os.system("kill 1")
