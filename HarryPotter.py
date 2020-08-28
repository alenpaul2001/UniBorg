# (c) AlenPaulVarghese
# .hph for random harry potter random_house
# .hps for random harry potter spells


import requests
import json
import random
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="hps ?(.*)"))
async def harrypotter(event):
    spells = requests.get('https://www.potterapi.com/v1/spells?key=$2a$10$hUcWvTPuzjKLhDdbOcpY/uRGuzwPE694t6e10xGElxxdHKbQGc5CS')
    r2json = json.loads(spells.text)
    random_number = random.randint(0, len(r2json))
    spell_to_print = r2json[random_number]['spell']
    await event.edit(text=spell_to_print)


@borg.on(admin_cmd(pattern="hph ?(.*)"))
async def harrypotterhouse(event):
        random_house = requests.get('https://www.potterapi.com/v1/sortingHat/')
        await event.edit(text=random_house.text)
