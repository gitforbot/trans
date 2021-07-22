import discord
from async_google_trans_new import AsyncTranslator

TOKEN = 'YOUR_TOKEN'

client = discord.Client()
translator = AsyncTranslator()


@client.event
async def on_ready():
    print('--------------')
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('--------------')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('!trans'):
        say = message.content
        say = say[7:]
        if say.find('-') == -1:
            str = say
            detact = await translator.detect(str)
            befor_lang = detact[0]
            if befor_lang == 'ja':
                convert_string = await translator.translate(str, lang_src=befor_lang, lang_tgt='en')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Befor', value=str)
                embed.add_field(
                    name='After', value=convert_string, inline=False)
                await message.channel.send(embed=embed)
            else:
                convert_string = await translator.translate(str, lang_src=befor_lang, lang_tgt='ja')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Befor', value=str)
                embed.add_field(
                    name='After', value=convert_string, inline=False)
                await message.channel.send(embed=embed)
        else:
            trans, str = list(say.split('='))
            befor_lang, after_lang = list(trans.split('-'))
            convert_string = await translator.translate(str, lang_src=befor_lang, lang_tgt=after_lang)
            embed = discord.Embed(title='変換結果', color=0xff0000)
            embed.add_field(name='Befor', value=str)
            embed.add_field(
                name='After', value=convert_string, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('!detect'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語はたぶん ' + detect.lang + ' です。'
        await message.channel.send(m)

client.run(TOKEN)
