import discord
from discord.ext import commands, tasks
import openai



intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)
TOKEN = <DISCORD-TOKEN>

api_keys = {}
prompts = {}


@client.event
async def on_ready():
    print("We've logged in as {0.user}".format(client))
    print("------------------------------")

@client.command(help="Sets the user's OpenAI API key. Usage: !setapi <api_key>")
async def setapi(ctx, api_key: str):
    api_keys[ctx.message.author.id] = api_key
    await ctx.send("API key set!")

@client.command(help="Clears the user's prompts. Usage: !clearprompts")
async def clearprompts(ctx):
    prompts[ctx.message.author.id] = ""
    await ctx.send("Prompts cleared!")

@client.command(help="Sends a query to OpenAI's Completion API and returns the response. "
"Optional arguments: model=<model_name>, temp=<temperature>, tokens=<max tokens>")
async def q(ctx, *, prompt: str):
    openai.api_key = api_keys.get(ctx.message.author.id)
    if openai.api_key is None:
        await ctx.send("You must set your API key using the !setapi command.")
        return

    user_prompts = prompts.get(ctx.message.author.id)
    if user_prompts is None:
        user_prompts = ""
    user_prompts += prompt + "\n"
    prompts[ctx.message.author.id] = user_prompts

    model = "text-davinci-003"
    temperature = 1
    max_tokens = 1000

    # Check if the user has specified the model, temperature, or max_tokens
    # in the command
    for arg in ctx.message.content.split(" ")[2:]:
        if arg.startswith("model="):
            model = arg.split("=")[1]
        elif arg.startswith("temp="):
            temperature = float(arg.split("=")[1])
        elif arg.startswith("tokens="):
            max_tokens = int(arg.split("=")[1])

    response = openai.Completion.create(
        model=model,
        prompt=user_prompts,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )

    await ctx.send(response["choices"][0]["text"])

@client.command()
async def h(ctx):
    # Initialize the response message
    response = "Available commands:\n"

    # Iterate through all the commands
    for command in client.commands:
        # Get the documentation for the command
        documentation = command.help
        # Format the documentation and add it to the response message
        response += f"{command}: {documentation}\n"

    # Send the response message to the user
    await ctx.send(response)


client.run(TOKEN)
