class SELFBOT():
    __linecount__ = 1955
    __version__ = 1.1
    
    # Dont just skid it, gimme some credits, thank you - xanthe.#1337
    # Edit/Fixed By https://github.com/Wh7sk
	
import discord, sys, time, os, colorama, io, random, numpy, datetime, smtplib, string, ctypes, json, re, requests
from discord.colour import Colour

from discord.ext import (
    commands,
    tasks
)

from colorama import Fore, Style
import pyPrivnote as pn

colorama.init()

ctypes.windll.kernel32.SetConsoleTitleW(f'[HWG Sniper v{SELFBOT.__version__} | Loading...')
print(f'''{Style.BRIGHT}{Fore.YELLOW}



                            ██▓     ▒█████   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████ 
                            ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
                            ▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
                            ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
                            ░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
                            ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
                            ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
                              ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
                                ░  ░    ░ ░        ░  ░   ░     ░           ░       ░ 
                                                        ░                             

                                    WARNING: DISCORD.PY VERSION MUST BE 1.4.2
                                            Discord.py Ver: {discord.__version__}

'''+Fore.RESET)

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

def Clear():
    os.system('cls')

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Whisk.run(token, bot=False, reconnect=True)
            os.system(f'title (Whisk Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

Whisk = discord.Client()
Whisk = commands.Bot(
    description='Whisk Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Whisk.remove_command('help')

@Whisk.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Whisk.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    
    if "discord.gift/" in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search(r'discord.gift/(\w+)', message.content).group(1)
            '''sep = '...'
            code = Xcode.split(sep, 1)[0]'''
            token = config.get('token')
            headers = {'Authorization': token}
            r = requests.post(
                f'https://canary.discord.com/api/v9/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
            
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'
            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.RED}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.MAGENTA}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
            elif '405' in r:
                print(""
                f"\n{Fore.MAGENTA}[{time} - 405 ERROR]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.MAGENTA}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.MAGENTA}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.MAGENTA}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.MAGENTA}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Whisk.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.MAGENTA}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.MAGENTA}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Whisk.process_commands(message)

@Whisk.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Enabled" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Enabled"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Enabled"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Enabled"
    else:
        privnote = "Disabled"    

    print(f'''{Style.BRIGHT}{Fore.MAGENTA}

                  ██░ ██  █     █░ ▄████      ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  
                  ▓██░ ██▒▓█░ █ ░█░██▒ ▀█▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
                  ▒██▀▀██░▒█░ █ ░█▒██░▄▄▄░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
                  ░▓█ ░██ ░█░ █ ░█░▓█  ██▓     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
                  ░▓█▒░██▓░░██▒██▓░▒▓███▀▒   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
                   ▒ ░░▒░▒░ ▓░▒ ▒  ░▒   ▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                   ▒ ░▒░ ░  ▒ ░ ░   ░   ░    ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
                   ░  ░░ ░  ░   ░ ░ ░   ░    ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
                   ░  ░  ░    ░         ░          ░           ░  ░              ░  ░   ░     
                                                                            
                        
                                        {Fore.MAGENTA}╭—————————————————————————————————╮
                                        {Fore.MAGENTA}│         HWG Sniper {SELFBOT.__version__}          │
                                        {Fore.MAGENTA}│        {Fore.YELLOW}github.com/wh7sk         {Fore.MAGENTA}│
                                        {Fore.MAGENTA}╰————————————————┬————————————————╯
                                        {Fore.MAGENTA}            User │ {Fore.YELLOW}{Whisk.user.name}#{Whisk.user.discriminator} 
                                        {Fore.MAGENTA}              ID │ {Fore.YELLOW}{Whisk.user.id}
                                        {Fore.MAGENTA}    Nitro Sniper │ {Fore.YELLOW}{nitro}
                                        {Fore.MAGENTA}  SlotBot Sniper │ {Fore.YELLOW}{slotbot}
                                        {Fore.MAGENTA} Privnote Sniper │ {Fore.YELLOW}{privnote}
                                        {Fore.MAGENTA} Giveaway Sniper │ {Fore.YELLOW}{giveaway}
                                        {Fore.MAGENTA}       ┈┈┈┈┈┈┈┄╌╶┴╴╌┄┈┈┈┈┈┈
    '''+Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW(f'[HWG Sniper v{SELFBOT.__version__} | {Whisk.user.name}#{Whisk.user.discriminator}')
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }


@Whisk.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

if __name__ == '__main__':
	Init()
