# Discord-OpenAI-Companion
# Project Documentation
This is a Discord bot that uses the OpenAI Completion API to generate responses to prompts given by users. It allows users to set their own OpenAI API key, clear their prompts, and generate responses to prompts with optional arguments for the model, temperature, and maximum number of tokens. It also includes a command to display a list of available commands and their documentation.

# Product Documentation
The bot is written in Python and uses the Discord and OpenAI libraries. It connects to the Discord API with a bot token and listens for commands prefixed with "!". It then uses the OpenAI API to generate responses to prompts and sends them back to the Discord channel. The user can specify optional arguments when generating a response, including the model to use, the temperature for the response, and the maximum number of tokens to generate.

# Process Documentation
To use the bot, the user must first set their OpenAI API key using the !setapi command. They can then use the !q command to send a prompt to the OpenAI Completion API and receive a response. If the user wants to clear their previous prompts, they can use the !clearprompts command. To see a list of available commands and their documentation, the user can use the !h command.

# Technical Documentation
<h2> API Documentation </h2> <br>
To use the OpenAI Completion API, the user must first set their API key using the !setapi command. This key is stored in the api_keys dictionary, which maps user IDs to API keys. The !q command sends a request to the OpenAI Completion API using the openai.Completion.create() method, which takes a number of optional arguments including the model to use, the temperature for the response, and the maximum number of tokens to generate.

<h2> Data Model Documentation </h2> <br>
The prompts dictionary stores the prompts for each user, mapping user IDs to a string of prompts separated by newline characters. The api_keys dictionary stores the API keys for each user, mapping user IDs to API keys.

<h2> Architecture Documentation </h2> <br>
The bot connects to the Discord API using the discord.Client class and listens for commands using the commands.Bot class. It processes commands using the @client.command decorator and sends responses using the client.send() method. To generate responses, it uses the openai.Completion.create() method from the OpenAI library.

# User Guide
To use the bot, the user must first invite it to a Discord server and set their OpenAI API key using the !setapi command. They can then use the !q command to send a prompt and receive a response from the OpenAI Completion API. To clear their prompts, they can use the !clearprompts command. To see a list of available commands and their documentation, they can use the !h command.

# Release Notes
Initial release: Includes !setapi, !clearprompts, !q, and !h commands.
