"""help command functionality"""
import os
import discord
from discord import Embed

Test_bot_application_ID = int(os.getenv('TEST_BOT_APP_ID'))


###########################
# Function: helper
# Description: Directs the help functions when called
# and is executes !help command
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help
###########################
async def helper(ctx):
    embed = Embed(title='help',
                  description="Use !help <command> for extended support",
                  colour=discord.Colour.red())
    embed.add_field(name='answer',
                    value='Answer specific question. Please put question ext in quotes')
    embed.add_field(name='ask',
                    value='Ask question. Please put question text in quotes')
    embed.add_field(name='attendance',
                    value='Gets the attendance of channel')
    embed.add_field(name='begin-tests',
                    value='start test command')
    embed.add_field(name='create',
                    value='Create a new event')
    embed.add_field(name='end-tests',
                    value='end tests command')
    embed.add_field(name='oh',
                    value='Operations relevant for office hours')
    embed.add_field(name='ping',
                    value='Returns Latency')
    embed.add_field(name='poll',
                    value='Set Poll for a specified time and topic')
    embed.add_field(name='setInstructor',
                    value='Set member to Instructor')
    embed.add_field(name='stats',
                    value='Shows bot stats')
    embed.add_field(name='test',
                    value='Simple sanity check')
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('help')


###########################
# Function: answer
# Description: Help for command answer
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help answer
###########################
async def answer(ctx):
    embed = Embed(title='answer',
                  description='Answer specific question. Please put question ext in quotes',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*',
                    value='!answer <Question Number> ["Answer"]',
                    inline=False)
    embed.add_field(name='*Channel*',
                    value='q-and-a',
                    inline=False)
    embed.add_field(name='*Authorization*',
                    value='Anyone',
                    inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('answer')


###########################
# Function: ask
# Description: Help for command ask
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help ask
###########################
async def ask(ctx):
    embed = Embed(title='ask',
                  description='Answer specific question. Please put question ext in quotes',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*',
                    value='!ask ["Question?"]',
                    inline=False)
    embed.add_field(name='*Channel*',
                    value='q-and-a',
                    inline=False)
    embed.add_field(name='*Authorization*',
                    value='Anyone',
                    inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('ask')


###########################
# Function: attendance
# Description: Help for command attendance
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help attendance
###########################
async def attendance(ctx):
    embed = Embed(title='attendance',
                  description='Gets the attendance of voice channel',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*',
                    value='!attendance',
                    inline=False)
    embed.add_field(name='*Channel*',
                    value='instructor-commands',
                    inline=False)
    embed.add_field(name='*Authorization*',
                    value='Instructor',
                    inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('attendance')


###########################
# Function: begin_tests
# Description: Help for command begin-tests
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help begin-tests
###########################
async def begin_tests(ctx):
    embed = Embed(title='begin-tests', description='start test command',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!begin-tests', inline=False)
    embed.add_field(name='*Channel*', value='Any', inline=False)
    embed.add_field(name='*Authorization*', value='Bot', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('begin-tests')


###########################
# Function: create
# Description: Help for command create
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help create
###########################
async def create(ctx):
    embed = Embed(title='create', description='Create a new event',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!create', inline=False)
    embed.add_field(name='*Channel*', value='instructor-commands', inline=False)
    embed.add_field(name='*Authorization*', value='Instructor', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('create')


###########################
# Function: end_tests
# Description: Help for command end-tests
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help end-tests
###########################
async def end_tests(ctx):
    embed = Embed(title='end-tests', description='end tests command',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!end-tests', inline=False)
    embed.add_field(name='*Channel*', value='Any', inline=False)
    embed.add_field(name='*Authorization*', value='Bot', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('end-tests')


###########################
# Function: oh
# Description: Help for command oh
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help oh
###########################
async def oh(ctx):
    embed = Embed(title='oh', description='Operations relevant for office hours',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!oh <enter>', inline=True)
    embed.add_field(name='*Channel*', value='office-hour', inline=True)
    embed.add_field(name='*Authorization*', value='Anyone', inline=True)

    embed.add_field(name='*Syntax*', value='!oh <exit>', inline=True)
    embed.add_field(name='*Channel*', value='office-hour', inline=True)
    embed.add_field(name='*Authorization*', value='Anyone', inline=True)

    embed.add_field(name='*Syntax*', value='!oh <next>', inline=True)
    embed.add_field(name='*Channel*', value='office-hour', inline=True)
    embed.add_field(name='*Authorization*', value='Instructor', inline=True)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('oh')


###########################
# Function: ping
# Description: Help for command ping
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help ping
###########################
async def ping(ctx):
    embed = Embed(title='ping', description='Returns Latency',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!ping', inline=False)
    embed.add_field(name='*Channel*', value='Any', inline=False)
    embed.add_field(name='*Authorization*', value='Anyone', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('ping')


###########################
# Function: poll
# Description: Help for command poll
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help poll
###########################
async def poll(ctx):
    embed = Embed(title='poll', description='Set Poll for a specified time and topic',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!poll', inline=False)
    embed.add_field(name='*Channel*', value='Any', inline=False)
    embed.add_field(name='*Authorization*', value='Instructor', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('poll')


###########################
# Function: setInstructor
# Description: Help for command setInstructor
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help setInstructor
###########################
async def setInstructor(ctx):
    embed = Embed(title='setInstructor',
                  description='Set Poll for a specified time and topic',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!poll', inline=False)
    embed.add_field(name='*Channel*', value='instructor-commands', inline=False)
    embed.add_field(name='*Authorization*', value='Instructor', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('setInstructor')


###########################
# Function: stats
# Description: Help for command stats
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help stats
###########################
async def stats(ctx):
    embed = Embed(title='stats', description='Shows bot stats',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!stats', inline=False)
    embed.add_field(name='*Channel*', value='Any', inline=False)
    embed.add_field(name='*Authorization*', value='Anyone', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('stats')


###########################
# Function: test
# Description: Help for command test
# Inputs:
#      - ctx: Context of the function activation
# Outputs: Result of !help test
###########################
async def test(ctx):
    embed = Embed(title='test', description='Simple sanity check',
                  colour=discord.Colour.orange())
    embed.add_field(name='*Syntax*', value='!test', inline=False)
    embed.add_field(name='*Channel*', value='Any', inline=False)
    embed.add_field(name='*Authorization*', value='Anyone', inline=False)
    await ctx.send(embed=embed)
    if ctx.author.id == Test_bot_application_ID:
        await ctx.send('test')
