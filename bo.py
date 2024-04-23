import pyrogram
import asyncio
from pyrogram import Client, filters, idle
import re
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os
from pyrogram.types import Message
from pyromod import listen
import os
import pyrogram
import redis, re
import asyncio
from pyrogram import Client, idle
from pyrogram import Client as app
from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod import listen
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, ChatPrivileges
from pyrogram.enums import ChatType
import asyncio
import random

API_ID = int("23979725")
API_HASH = "7b0bdb3b9f40d8fb50e13fd8e565e620"
DEVS = ["ÙÙØ²Ø± Ø§ÙÙØ·ÙØ± ÙÙØºÙØ± @"] 
app = Client(
    "mbhfho",
    api_id=int("23979725"),
    api_hash="7b0bdb3b9f40d8fb50e13fd8e565e620",
    bot_token="5978744405:AAGyhwBe4BC3zbWDqs5dy4ZMH9Aw_p9goEs", 
    )

@app.on_message(filters.command("Ø¯Ø¹ÙØ© Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª ÙÙÙÙØ§Ø©", "") & filters.private, group=8272727727)
async def invite_accounts_to_group(client, message):
    if message.from_user.username not in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    name = await client.ask(message.chat.id, "Ø£Ø±Ø³Ù Ø§ÙØ¢Ù Ø§ÙØ±Ø§Ø¨Ø·")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    for session in sessions:
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.join_chat(name)
        except Exception as e:
            print(f"Error inviting user: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "ØªÙ Ø§ÙØ¶ÙØ§Ù {num_accounts} Ø¨ÙØ¬Ø§Ø­")    

@app.on_message(filters.command("Ø§ÙØ¶ÙØ§Ù Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª ÙÙÙÙØ§Ø© â", "") & filters.private, group=8272727727)
async def invite_accounts_to_group(client, message):
    if message.from_user.username not in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    name = await client.ask(message.chat.id, "Ø£Ø±Ø³Ù Ø§ÙØ¢Ù Ø§ÙØ±Ø§Ø¨Ø·")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    for session in sessions:
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.join_chat(name)
            await user.archive_chats(name)
        except Exception as e:
            print(f"Error inviting user: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "ØªÙ Ø§ÙØ¶ÙØ§Ù {num_accounts} Ø¨ÙØ¬Ø§Ø­")    
    
@app.on_message(filters.command("ÙØºØ§Ø¯Ø±Ù Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª ÙÙÙÙØ§Ø©", "") & filters.private, group=827272772772626)
async def leave_accounts_to_group(client, message):
    if message.from_user.username not in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    name = await client.ask(message.chat.id, "Ø£Ø±Ø³Ù Ø§ÙØ¢Ù Ø§ÙØ±Ø§Ø¨Ø·")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    for session in sessions:
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.leave_chat(name)
        except Exception as e:
            print(f"Error leaving chat: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "ØªÙ ÙØºØ§Ø¯Ø±Ø© Ø§ÙØ­Ø³Ø§Ø¨ Ø§ÙÙØ³Ø§Ø¹Ø¯ Ø¨ÙØ¬Ø§Ø­")

@app.on_message(filters.command("Ø§Ø¶Ù Ø­Ø³Ø§Ø¨", "") & filters.private, group=827363666)
async def add_assistant_account(client, message):
    if not message.from_user.username in DEVS:
        return
    ask = await client.ask(message.chat.id, "ÙÙ ÙØ¯ÙÙ Ø¬ÙØ³Ø©Ø", timeout=300)
    me = ask.text
    if me == "ÙØ§":
        ask = await client.ask(message.chat.id, "Ø§Ø±Ø³Ù ÙÙ Ø§ÙØ¢Ù Ø§ÙØ±ÙÙ", timeout=300)
        hossahm = ask.text
        await message.reply_text("Ø§ÙØªØ¸Ø±Ø Ø¬Ø§Ø±Ù Ø¥Ø±Ø³Ø§Ù Ø§ÙÙÙØ¯")
        cliehnt = Client(name="hfhhfg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
        await cliehnt.connect()
        try:
            code = await cliehnt.send_code(hossahm)
        except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
            return
        ask = await client.ask(message.chat.id, "ØªÙ Ø¥Ø±Ø³Ø§Ù Ø§ÙÙÙØ¯ Ø¥ÙÙ Ø­Ø³Ø§Ø¨ÙØ ÙÙ Ø¨Ø¥Ø±Ø³Ø§Ù Ø§ÙÙÙØ¯ Ø¨ÙØ°Ù Ø§ÙØ·Ø±ÙÙØ©: 1 2 3 4 5", timeout=300)
        hoam = ask.text
        try:
            await cliehnt.sign_in(hossahm, code.phone_code_hash, hoam)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await message.reply_text("Ø§ÙÙÙØ¯ ØºÙØ± ØµØ­ÙØ­ Ø£Ù Ø§ÙØªÙØª ØµÙØ§Ø­ÙØ© Ø§ÙÙÙØ¯")
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await message.reply_text("Ø§ÙÙÙØ¯ ØºÙØ± ØµØ­ÙØ­ Ø£Ù Ø§ÙØªÙØª ØµÙØ§Ø­ÙØ© Ø§ÙÙÙØ¯")
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                ask = await client.ask(message.chat.id, "Ø§ÙØ­Ø³Ø§Ø¨ ÙØ­ÙÙ Ø¨ÙÙÙØ© Ø³Ø±Ø Ø§Ø±Ø³Ù ÙÙÙØ© Ø§ÙØ³Ø± Ø§ÙØ¢Ù", timeout=300)
                hm = ask.text
            except TimeoutError:
                return
            try:
                await cliehnt.check_password(password=hm)
                session = await cliehnt.export_session_string()
            except:
                await message.reply_text("ÙÙÙØ© Ø§ÙØ³Ø± ØºÙØ± ØµØ­ÙØ­Ø©")
                return
        else:
            session = await cliehnt.export_session_string()
        await cliehnt.disconnect()
    elif me == "ÙØ¹Ù":
        ask = await client.ask(message.chat.id, "Ø§Ø±Ø³Ù Ø§ÙØ¬ÙØ³Ù", timeout=300)
        session = ask.text
    file_exists = os.path.exists("sessions.txt")
    with open("sessions.txt", "a") as file:
        if not file_exists:
            file.write(f"{session}\n")
        else:
            file.write("\n")
            file.write(f"{session}\n")
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        for dev in DEVS:
            try:
                await user.send_message(dev, "ØªÙ ØªØ´ØºÙÙ Ø§ÙØ­Ø³Ø§Ø¨ Ø¹Ø²ÙØ²Ù")
            except Exception as e:
                print(f"Error sending message to developer: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "ØªÙ Ø¥Ø¶Ø§ÙØ© Ø§ÙØ­Ø³Ø§Ø¨ Ø¨ÙØ¬Ø§Ø­")

@app.on_message(filters.command("Ø§Ø³ØªØ®Ø±Ø§Ø¬ Ø¬ÙØ³Ù", "") & filters.private)
async def mamhcmfbjvbie(client, message):
    ask = await client.ask(message.chat.id, "Ø§Ø±Ø³Ù ÙÙ Ø§ÙØ§Ù Ø§ÙØ±ÙÙ", timeout=300)
    hossahm = ask.text
    await message.reply_text("Ø§ÙØªØ¸Ø± Ø¬Ø§Ø±Ù Ø§Ø±Ø³Ø§Ù Ø§ÙÙÙØ¯")
    cliehnt = Client(name="hfhhfg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await cliehnt.connect()
    try:
        code = await cliehnt.send_code(hossahm)
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return
    ask = await client.ask(message.chat.id, "ØªÙ Ø§Ø±Ø³Ø§Ù Ø§ÙÙÙØ¯ Ø§ÙÙ Ø­Ø³Ø§Ø¨Ù ÙÙ Ø¨Ø§Ø±Ø³Ø§Ù Ø§ÙÙÙØ¯ \n Ø¨ÙØ°ÙÙ Ø§ÙØ·Ø±ÙÙÙ : 1 2 3 4 5", timeout=300)
    hoam = ask.text  
    try:
        await cliehnt.sign_in(hossahm, code.phone_code_hash, hoam)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        await message.reply_text("Ø§ÙÙÙØ¯ ØºÙØ± ØµØ­ÙØ­ Ø§Ù Ø§ÙØªÙÙ ØµÙØ§Ø­ÙÙ Ø§ÙÙÙØ¯")
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        await message.reply_text("Ø§ÙÙÙØ¯ ØºÙØ± ØµØ­ÙØ­ Ø§Ù Ø§ÙØªÙÙ ØµÙØ§Ø­ÙÙ Ø§ÙÙÙØ¯")
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            ask = await client.ask(message.chat.id, "Ø§ÙØ­Ø³Ø§Ø¨ ÙØ­ÙÙ Ø¨ÙÙÙÙ Ø³Ø± Ø§Ø±Ø³Ù ÙÙÙÙ Ø§ÙØ³Ø± Ø§ÙØ§Ù", timeout=300)
            hm = ask.text
        except TimeoutError:
            return
        try:
            await cliehnt.check_password(password=hm)
            string_session = await cliehnt.export_session_string()
        except:
            await message.reply_text("ÙÙÙÙ Ø§ÙØ³Ø± ØºÙØ± ØµØ­ÙØ­Ù")
            return  
    else:
        string_session = await cliehnt.export_session_string()
    await cliehnt.disconnect()
    SESSION = string_session
    await client.send_message(message.chat.id, f"ØªÙ Ø§Ø³ØªØ®Ø±Ø§Ø¬ Ø§ÙØ¬ÙØ³Ù Ø¨ÙØ¬Ø§Ø­ \n `{SESSION}`")
    
@app.on_message(filters.command(["/start"], "") & filters.private, group=71365578)
async def kep(client, message):
    if message.from_user.username not in DEVS:
        return
    kep = ReplyKeyboardMarkup([["Ø¬ÙØ¨ ÙØ³Ø®Ø© Ø§ÙØ§Ø±ÙØ§Ù"], ["Ø§Ø¶Ù Ø­Ø³Ø§Ø¨", "Ø§Ø³ØªØ®Ø±Ø§Ø¬ Ø¬ÙØ³Ù"], ["Ø¯Ø¹ÙØ© Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª ÙÙÙÙØ§Ø©", "ÙØºØ§Ø¯Ø±Ù Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª ÙÙÙÙØ§Ø©"], ["Ø¹Ø¯Ø¯ Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª", "Ø§ÙØ¶ÙØ§Ù Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª ÙÙÙÙØ§Ø© â"], ["ÙÙÙ Ø§ÙÙÙØ¨ÙØ±Ø¯"]], resize_keyboard=True)
    await message.reply_text("â®â¦¿ Ø§ÙÙÙØ§ Ø¨Úª Ø¹Ø²ÙÙØ²Ù Ø§ÙÙØ·ÙÙØ± Ø§ÙØ§Ø³Ø§Ø³ÙÙ ââ Ø§ÙÙÙ ÙÙØ¨ Ø§ÙØªØ­ÙÙ Ø¨Ø§ÙØ¨ÙØª ÙÙ Ø³ÙØ±Ø³ Ø³ÙÙÙâ¤ï¸âð¥", reply_markup=kep)

@app.on_message(filters.command(["ÙÙÙ Ø§ÙÙÙØ¨ÙØ±Ø¯"], "") & filters.private, group=71328934689)
async def keplook(client, message):
    m = await message.reply("**- ØªÙ Ø§Ø®ÙØ§Ø¡ Ø§ÙØ§Ø²Ø±Ø§Ø± Ø¨ÙØ¬Ø§Ø­\n- ÙÙ ØªØ¨Ù ØªØ·ÙØ¹ÙØ§ ÙØ±Ø© Ø«Ø§ÙÙØ© Ø§ÙØªØ¨ /start**", reply_markup=ReplyKeyboardRemove(selective=True))
 
@app.on_message(filters.command(["Ø¬ÙØ¨ ÙØ³Ø®Ø© Ø§ÙØ§Ø±ÙØ§Ù"], "") & filters.private, group=72636343)
async def upbkgt(client: Client, message: Message):
    with open("sessions.txt", "rb") as file:
        await message.reply_document(document=file)
        
@app.on_message(filters.command("Ø¹Ø¯Ø¯ Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª", "") & filters.private, group=7263638299)
async def caesar_accounts(client, message):
    if not message.from_user.username in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    num_accounts = len(sessions)
    await client.send_message(message.chat.id, f"Ø¹Ø¯Ø¯ Ø§ÙØ­Ø³Ø§Ø¨Ø§Øª Ø§ÙÙØ¶Ø§ÙØ© Ø­Ø§ÙÙØ§Ù ÙÙ {num_accounts}")


if __name__ == "__main__": app.run()