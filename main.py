import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("앙꼬야 도움말")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("앙꼬야 도움말"):
        await message.channel.send("> 앙꼬야 안녕, 뽑기, 주사위, 투표 (제목)/(항목)/(항목).. 등")

    if message.content.startswith("앙꼬야 안녕"):
        await message.channel.send(random.choice(["> 안녕하세요!", "> 반가워요!"]))

    if message.content.startswith("앙꼬야 뽑기"):
        await message.channel.send(random.choice(["> 실패하셨습니다. 흐접ㅋ",  "> 성공하셨습니다. 축하드려요!"]))

    if message.content.startswith("앙꼬야 주사위"):
        await message.channel.send(random.choice(["> 1이 나왔습니다.", "> 2가 나왔습니다.", "> 3이 나왔습니다.", "> 4가 나왔습니다.", "> 5가 나왔습니다.", "> 6이 나왔습니다. 와!"]))

    if message.content.startswith("앙꼬야 투표"):
        vote = message.content[7:].split("/")
        await message.channel.send("투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("> " + vote[i])
            await choose.add_reaction('✅')















client.run("ODY1MTU4MzM1NjkwOTY1MDIy.YO_7fQ.NrmW8gCvbimh-CUgLh4VuuyiiqA")