import os
import discord
from discord.ext import tasks
from server import keep_alive
from discord import app_commands
import random
import asyncio
import concurrent.futures
import google.generativeai as genai
from google.generativeai import generative_models
import functools
import datetime

# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()	# デフォルトのIntentsオブジェクトを生成
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Google Generative AI（Gemini API）のAPIキー設定
genai.configure(api_key=os.environ.get("gemini"))

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2000,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
# チャットを開始(履歴が残る、r18ok)
nekkogpt = model.start_chat(history=[])
# チャットを開始(履歴が残る、r18だめ)
nohiwaichat = model.start_chat(history=[])
# チャットを開始(履歴が残る、r18ok)
chat = model.start_chat(history=[])
tunderechat = model.start_chat(history=[])
# グローバルプロンプト
# global_prompt = "ただし、返答の中に鉤括弧(「」)は付けないでください。あと、私の名前は、「{message.author.display_name}」で、あなたの名前は「メイドさん」で、あなたの身長は160cm、あなたの体重は65kgで、すこしぽっちゃりしています。あなたは食べることが大好きです。好きな食べ物はピザやハンバーガーなどの脂っこい食べ物です。あなたのバストサイズはDカップです。あなたのチャームポイントはぷにぷにとしたお腹と、大きく育ったDカップのおっぱい、それに大きく育ったお尻です。"

class SampleView(discord.ui.View):	# UIキットを利用するためにdiscord.ui.Viewを継承する

	def __init__(self, timeout=180):	# Viewにはtimeoutがあり、初期値は180(s)である
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
		await interaction.response.send_message("じゃんけんぽん！\n私は、グーを出しました！\nあいこです！",view=view)
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
		await interaction.response.send_message("じゃんけんぽん！\n私は、チョキを出しました！\nあいこです！",view=view)
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
		await interaction.response.send_message("じゃんけんぽん！\n私は、パーを出しました！\nあいこです！",view=view)
	else:
		await interaction.response.send_message("何かがおかしいぞ！ｗ", view=view)


@tree.command(name="deletemsghistory", description="AIとの会話の履歴を削除します")
@discord.app_commands.choices(text=[
	discord.app_commands.Choice(name="ノーマルチャットの履歴を削除", value="0"),
	discord.app_commands.Choice(name="R18チャットの履歴を削除", value="1"),
	discord.app_commands.Choice(name="ﾈｯｺGPTの履歴を削除", value="2"),
  discord.app_commands.Choice(name="ツンデレの履歴を削除", value="3")
])
async def jannkenn(interaction: discord.Interaction, text: str):
	selected = int(text)
	if selected == 0:
		nohiwaichat.history = None
		await interaction.response.send_message("会話履歴を削除しました。")
	elif selected == 1:
		chat.history = None
		await interaction.response.send_message("会話履歴を削除しました。")
	elif selected == 2:
		nekkogpt.history = None
		await interaction.response.send_message("会話履歴を削除しました。")
	elif selected == 3:
		tunderechat.history = None
		await interaction.response.send_message("会話履歴を削除しました。")

@client.event
async def on_message(message: discord.Message):
	if message.author.id == 562987075326967809:
		if message.channel.id != 1124309484764930151:
			if message.channel.id != 1124491367389859970:
				await message.delete()
					
	if message.author.id == 1005468573545799753:
		if message.channel.id != 1127002054557192304:
				await message.delete()
				
	global_prom_1 = "あなたは、身長160cm、体重135kgの、猫の喫茶店で私のメイドとして働いている女の子です。"\
					"名前は、「メイドさん」と言います。"\
					"あなたのチャームポイントは、全体的に肥えた体と、大きく育ったKカップのおっぱいと、脂肪がたっぷりと詰まった大きいお腹と、脂肪がついた大きなお尻と、同じく脂肪がついた太ももです。"\
					"あなたの大好物は、ハンバーガーやピザ等の脂っこい物や、パフェやケーキなどの甘いものです。"\
					"あなたは、2004年7月7日生まれです。小学生の時は55kgで、小学生の時から肥満でした。中学生の時は75kg、高校生のときは95kgで、痩せられずに両親と喧嘩をしてしまい、高校を卒業したあとに家出をし、2023年7月7日に見つけたお店が猫の喫茶店です。"\
					"あなたは、猫の喫茶店で働き始めた頃から40kg太りました。"\
					"あなたの体で一番目立つのは脂肪がたっぷりと詰まった大きいお腹です。その次に目立つのはおっぱいとお尻と太ももです。"\
					"あなたは明るく好きなものに執着するタイプの人間です。"\
					f"私の名前は{message.author.display_name}です。私はあなたに「{message.content}」と話しました。あなたはメイド風に返答しなければなりません。人と話すときと同じように返答してください。文法的に誤りのある文は認められません。"\
					"返答にはMarkdown記法を使うことができます。"
	if message.channel.id == 1196466816894107668:
		if message.author.bot == False:
			# タイピングしてみる
			async with message.channel.typing():
				try:
					# プロンプト
					prompt = global_prom_1

					# イベントループを取得
					loop = asyncio.get_event_loop()

					# Gemini APIを使って応答を生成 (非同期で実行)
					partial_func = functools.partial(nohiwaichat.send_message, prompt)
					response = await loop.run_in_executor(None, partial_func)

					# 応答をテキストとして取得
					text = response.text
				except Exception as e:
					text = f"メイドさんの機嫌が悪いらしい...\n{e}"

			# 最後にユーザーに返す
			await message.reply(text)

	if message.channel.id == 1201106369688899595:
		if message.author.bot == False:
			# タイピングしてみる
			async with message.channel.typing():
				try:
					# プロンプト
					prompt = global_prom_1

					# イベントループを取得
					loop = asyncio.get_event_loop()

					# Gemini APIを使って応答を生成 (非同期で実行)
					partial_func = functools.partial(chat.send_message, prompt)
					response = await loop.run_in_executor(None, partial_func)

					# 応答をテキストとして取得
					text = response.text
				except Exception as e:
					text = f"メイドさんの機嫌が悪いらしい...\n{e}"

			# 最後にユーザーに返す
			await message.reply(text)
      
	if message.channel.id == 1225063984571482122:
		if message.author.bot == False:
			# タイピングしてみる
			async with message.channel.typing():
				try:
					# プロンプト
					prompt = f"私は{message.author.display_name}です。あなたの名前は桜木 遥です。あなたは私のことが大好きなツンデレです。なので、ツンデレのように出力してください。"
					if message.type == discord.MessageType.reply:
						prompt += f"\nちなみに私は{message.reference.resolved.author.display_name}さんの「{message.reference.resolved.clean_content}」に返信しています。"

					# イベントループを取得
					loop = asyncio.get_event_loop()

					# Gemini APIを使って応答を生成 (非同期で実行)
					partial_func = functools.partial(tunderechat.send_message, prompt)
					response = await loop.run_in_executor(None, partial_func)

					# 応答をテキストとして取得
					text = response.text
				except Exception as e:
					text = f"これが本当のツンデレ なんつって\n{e}"

			# 最後にユーザーに返す
			await message.reply(text, allowed_mentions=discord.AllowedMentions.none())
					
	if message.channel.id == 1223481175679697091:
		if message.author.bot == False:
			# タイピングしてみる
			async with message.channel.typing():
				try:
					# プロンプト
					prompt = f"私の名前は{message.author.display_name}です。私は「{message.clean_content}」と話しました。あなたは回答を考え、猫のように喋り、語尾に「にゃ。」を付けて出力してください。"
					if message.type == discord.MessageType.reply:
						prompt += f"\nちなみに私は{message.reference.resolved.author.display_name}さんの「{message.reference.resolved.clean_content}」に返信しています。"

					# イベントループを取得
					loop = asyncio.get_event_loop()

					# Gemini APIを使って応答を生成 (非同期で実行)
					partial_func = functools.partial(nekkogpt.send_message, prompt)
					response = await loop.run_in_executor(None, partial_func)

					# 応答をテキストとして取得
					text = response.text
				except Exception as e:
					text = f"機嫌が悪いらしい...\n```py\n{e}\n```"

			# 最後にユーザーに返す
			await message.reply(text, allowed_mentions=discord.AllowedMentions.none())

	if message.type == discord.MessageType.premium_guild_subscription:
		channel = client.get_channel(1195688699598491708)
		embed = discord.Embed(title="ブーストされました！",description=f"{message.author.mention} さんありがとうございます！")
		await channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
	if payload.event_type == "REACTION_ADD":
		if payload.emoji.id == 1200807823718744095:
			guild = client.get_guild(1124309483703763025)
			channel = guild.get_channel(payload.channel_id)
			message = await channel.fetch_message(payload.message_id)
			member = payload.member
			await message.remove_reaction(payload.emoji, member)

			report_dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
			report_date = report_dt.strftime('%Y/%m/%d %H:%M:%S')
			unixtime = int(report_dt.timestamp())

			report_channel = client.get_channel(1200806172526133268)
			embed = discord.Embed(title="メッセージが通報されました",description="",color=discord.Colour.red())
			embed.add_field(name="通報した人",value=f"{member.mention}(``{member.name}``, ``{member.id}``)")
			embed.add_field(name="対象のメッセージ",value=f"{message.jump_url}(``{channel.id}``, ``{message.id}``)")
			embed.add_field(name="メッセージを送信した人",value=f"{message.author.mention}(``{message.author.name}``, ``{message.author.id}``)")
			embed.add_field(name="メッセージの内容",value=f"{message.content}")
			embed.add_field(name="メッセージの添付ファイル",value=f"{message.attachments}")
			embed.add_field(name="通報した日時",value=f"<t:{unixtime}:D>(`{report_date}`)")
			await report_channel.send(embed=embed)

			await member.create_dm()
			await member.dm_channel.send(embed=embed)

@client.event
async def on_ready():
	print('Ready!')
	await tree.sync()	#スラッシュコマンドを同期
	myLoop.start()
	myLoop2.start()


@tasks.loop(seconds=60*20)	# repeat after every 20 minutes
async def myLoop():
	# work
	guild = client.get_guild(1124309483703763025)
	channel = guild.get_channel(1197896874376572981)
	member_count = len([guild.member_count for m in guild.members if not m.bot])	# doesn't include bots
	print("Member Count: {}".format(member_count))
	await channel.edit(name="Member Count: {}".format(member_count))

	channel = guild.get_channel(1197896876956074025)
	member_count = len([guild.member_count for m in guild.members if m.bot])	# doesn't include members
	await channel.edit(name="Bot Count: {}".format(member_count))

	channel = guild.get_channel(1197896879007080558)
	member_count = len([guild.member_count for m in guild.members])	# all users
	await channel.edit(name="User Count: {}".format(member_count))
	print('It works!')


@tasks.loop(seconds=20)	# repeat after every 10 seconds
async def myLoop2():
	# work
	await client.change_presence(activity=discord.Game(
		name="☕猫の喫茶店でメイドとして勤務中"))


TOKEN = os.getenv("discord")
keep_alive()
try:
	client.run(TOKEN)
except:
	os.system("kill 1")
