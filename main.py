import discord
import asyncio
from discord.ext import commands
import urllib.request as req
import re
from time import sleep
from math import trunc
#--------------------------------------------
class Cotacao:

    def __get_cotacao(self, url, regex='^.*nacional" value="([0-9,]+)"'):   #pegar o valor das moedas
        pagina = req.urlopen(url)
        s = pagina.read().decode('utf-8')
        m = re.match(regex, s, re.DOTALL)
        if m:
            return float(m.group(1).replace(',', '.'))
        else:
            return 0

    def dolar(self):
        return (self.__get_cotacao('http://dolarhoje.com/'))

    def euro(self):
        return self.__get_cotacao('http://eurohoje.com/')

    def libra(self):
        return self.__get_cotacao('http://librahoje.com/')

    def rublo(self):
        return self.__get_cotacao('https://dolarhoje.com/rublo-russo-hoje/')

    def peso(self):
        return self.__get_cotacao('https://dolarhoje.com/peso-argentino/')

    def bitcoin(self):
        return self.__get_cotacao('https://dolarhoje.com/bitcoin-hoje/')

cotacao = Cotacao()
dolar_float = float(cotacao.dolar())
#-----------------------------------------------------------------------------------------------------------------------
client = commands.Bot(command_prefix = ".")   #prefix
client.remove_command('help')
mensagem_bonitinha = ('Analisando minha bolsa de valores:chart_with_upwards_trend:...Por favor aguarde.') #mensagem antes dos valores

print('software online')

@client.event
async def on_ready():
    print('bot online')

#-----------------------------------------    #comandos
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='Stonks. Bem vindo.')
    embed.add_field(name=".dolar", value='Informa a cotação do Dolar.', inline = False)
    embed.add_field(name=".euro", value='Informa a cotação do Euro.', inline = False)
    embed.add_field(name=".rublo", value='Informa a cotação do Rublo.', inline = False)
    embed.add_field(name=".bitcoin", value='Informa a cotação do Bitcoin.', inline = False)          #help
    embed.add_field(name=".peso", value='Informa a cotação do Peso Argentino.', inline = False)
    embed.add_field(name=".libra", value='Informa a cotação da Libra.', inline = False)
    embed.add_field(name=".converter", value='Converte um valor em Dolar para Real.', inline = False)
    embed.add_field(name=".vbuck", value='Informa o preço do Vbuck.', inline = False)
    embed.add_field(name=".imposto", value='Fala umas verdades.', inline = False)
    embed.add_field(name=".repita", value='Repete algo que foi falado pelo autor do comando.', inline = False)
    await ctx.send(author, embed=embed)
    
@client.command()
async def dolar(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Dolar está custando {cotacao.dolar()} Reais. :money_with_wings: '))    #dolar


@client.command()
async def euro(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Euro está custando {cotacao.euro()} Reais. :money_with_wings: '))      #euro

@client.command()
async def libra(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Libra está custando {cotacao.libra()} Reais. :money_with_wings: '))     #libra

@client.command()
async def rublo(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Rublo Russo está custando {cotacao.rublo()} Reais. :money_with_wings: '))   #rublo

@client.command()
async def peso(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Peso Argentino está custando {cotacao.peso()} Reais. :money_with_wings: '))    #peso

@client.command()
async def bitcoin(ctx):
    msg = await ctx.send(mensagem_bonitinha)
    sleep(1)
    await msg.edit(content=(f'1 Bitcoin está custando {cotacao.bitcoin()} Reais. :money_with_wings: '))     #bitcoin

@client.command()
async def vbuck(ctx):
    await ctx.send(mensagem_bonitinha)
    sleep(1)
    await ctx.send('KKKKKKKKK VBUCK TA CARO DEMAIS MANO. VAI DAR NAO.')                                         #vbuck

@client.command()
async def imposto(ctx):
    msg = await ctx.send('IMPOSTO')
    sleep(1)
    await msg.edit(content=('É'))
    sleep(1)
    await msg.edit(content=("ROBÔ :robot:"))

@client.command()
async def stonks(ctx):
    await ctx.send('Estou aqui para te ajudar com conversão de moedas.')
    sleep(1)
    await ctx.send('Digite ".help" para ver o que posso fazer!')

@client.command()
async def converter(ctx, arg):
    try:
        multiplicacao = (float("{}".format(dolar_float))*float("{}".format(arg)))        #convert
        await ctx.send (f'{arg} Dolares valem mais ou menos {trunc(multiplicacao)} Reais.')
    except:
        await ctx.send("Formato não suportado. Tente usar ponto ao invés de vírgula.")

@client.event
async def on_message(message):
    if 'imposto' in message.content:
        await message.channel.send('EU OUVI IMPOSTO?')

#------------------------------------------------------------------------------------------------------

# client.run(token)