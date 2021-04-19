import discord
import requests
import os
import random
from alpha_vantage.timeseries import TimeSeries
from datetime import date, timedelta
import datetime
from discord.ext import commands, tasks
import asyncio

key = 'IQ1OME4G017P95NK'

ts = TimeSeries(key)

aapl, meta = ts.get_daily(symbol = 'AAPL')

today = str(date.today())

date = str(date.today() - timedelta(days = 1))

client = discord.Client()

now = datetime.datetime.now()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'pau' in message.content.lower():
        await message.add_reaction('<:rola:615238842999373825>')
    
    if message.content.startswith('$bov '):
        stock_name = message.content[5:]
        a = ts.get_daily(symbol = stock_name + '.sa')
        stock = a[0][date] #dia anterior
        await message.channel.send(stock)

    if message.content.startswith('$US '):
        stock_name = message.content[4:]
        a = ts.get_daily(symbol = stock_name)
        stock = a[0][date] #dia anterior
        await message.channel.send(stock)
        
    if message.content.startswith('$c '):
        currency = message.content[3:]
        URL = "https://www.bitstamp.net/api/v2/ticker/{currency_pair}/".format(currency_pair = currency)

        PARAMS = {}

        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        await message.channel.send(data)

with open("megatoken.json", "r") as json_file:
    secret = json.load(json_file)
client.run(secret["token"])
