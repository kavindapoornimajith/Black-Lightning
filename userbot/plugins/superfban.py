import asyncio
from userbot import ALIVE_NAME
from userbot import CMD_HELP
from userbot.utils import lightning_cmd, sudo_cmd
from userbot import bot
lightning = ALIVE_NAME
@bot.on(lightning_cmd("superfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**Superfban coming in order of {lightning}**...")
    fedList = []
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await bot.download_media(
                previous_message, "fedlist"
            )
            await asyncio.sleep(6)
            file = open(downloaded_file_name, "r")
            lines = file.readlines()
            for line in lines:
                try:
                    fedList.append(line[:36])
                except BaseException:
                    pass
            arg = event.text.split(" ", maxsplit=2)
            if len(arg) > 2:
                FBAN = arg[1]
                REASON = arg[2]
            else:
                FBAN = arg[1]
                REASON = " #fban "
        else:
            FBAN = previous_message.sender_id
            REASON = event.text.split(" ", maxsplit=1)[1]
            if REASON.strip() == "":
                REASON = " #fban"
    else:
        arg = event.text.split(" ", maxsplit=2)
        if len(arg) > 2:
            FBAN = arg[1]
            REASON = arg[2]
        else:
            FBAN = arg[1]
            REASON = " #fban "
    try:
        int(FBAN)
        if int(FBAN) == 1232461895 or int(FBAN) == 1754865180 or int(FBAN) == 1311769691 :     
            await event.edit("Sorry Dear but you are trying to ban GOD.")
            return
    except BaseException:
        if FBAN == "@hacker11000" or FBAN == "@paramatin7" or FBAN == "@keinshin" :
            await event.edit("Sorry Dear but you are trying to ban God")
            return
    if Config.PM_PERMIT_GROUP_ID :
        chat = Config.PM_PERMIT_GROUP_ID 
    else:
        chat = await event.get_chat()
    if not len(fedList):
        for a in range(3):
            async with bot.conversation("@MissRose_bot") as bot_conv:
                await bot_conv.send_message("/start")
                await bot_conv.send_message("/myfeds")
                await asyncio.sleep(2)
                response = await bot_conv.get_response()
                await asyncio.sleep(2)
                if "make a file" in response.text:
                    await asyncio.sleep(6)
                    await response.click(0)
                    await asyncio.sleep(6)
                    fedfile = await bot_conv.get_response()
                    await asyncio.sleep(3)
                    if fedfile.media:
                        downloaded_file_name = await bot.download_media(
                            fedfile, "fedlist"
                        )
                        await asyncio.sleep(6)
                        file = open(downloaded_file_name, "r")
                        lines = file.readlines()
                        for line in lines:
                            try:
                                fedList.append(line[:36])
                            except BaseException:
                                pass
                    else:
                        return
                if len(fedList) == 0:
                    await event.edit(f"Checking feds of **{lightning}**\n wait **({a+1}/3)**...")
                else:
                    break
        else:
            await event.edit(f"Error")
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True

            elif In:
                tempFedId += x
        if len(fedList) == 0:
            await event.edit("Something went wrong.")
            return
    await event.edit(f"BL banning you in **{len(fedList)}** for **{lightning}** .")
    try:
        await bot.send_message(chat, f"/start")
    except BaseException:
        await event.edit("PM_PERMIT_GROUP_ID  is incorrect.")
        return
    await asyncio.sleep(3)
    if Config.EXCLUDE_FED:
        excludeFed = Config.EXCLUDE_FED.split("|")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if Config.EXCLUDE_FED and fed in excludeFed:
            await bot.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await bot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await bot.send_message(chat, f"/fban {FBAN} {REASON}")
        await asyncio.sleep(3)
    await event.edit(
        f"Sᴜᴘᴇʀғʙᴀɴ Cᴏᴍᴘʟᴇᴛᴇᴅ, Aғғᴇᴄᴛᴇᴅ Iɴ **{len(fedList) - exCount}** Fᴇᴅs.\n\n#UltraX Userbot"
    )




@bot.on(lightning_cmd("superunfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"**Bl unfban you ijn order of {lightning}**...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.sender_id
    else:
        FBAN = event.pattern_match.group(1)

    if Config.PM_PERMIT_GROUP_ID :
        chat = Config.PM_PERMIT_GROUP_ID 
    else:
        chat = await event.get_chat()
    fedList = []
    for a in range(3):
        async with bot.conversation("@MissRose_bot") as bot_conv:
            await bot_conv.send_message("/start")
            await bot_conv.send_message("/myfeds")
            response = await bot_conv.get_response()
            if "make a file" in response.text:
                await asyncio.sleep(3)
                await response.click(0)
                fedfile = await bot_conv.get_response()
                if fedfile.media:
                    downloaded_file_name = await bot.download_media(
                        fedfile, "fedlist"
                    )
                    file = open(downloaded_file_name, "r")
                    lines = file.readlines()
                    for line in lines:
                        fedList.append(line[: line.index(":")])
                else:
                    return
                if len(fedList) == 0:
                    await event.edit(f"Wait {lightning} ({a+1}/3)...")
                else:
                    break
    else:
        await event.edit(f"Error")
    if "You can only use fed commands once every 5 minutes" in response.text:
        await event.edit("Try again after 5 mins.")
        return
    In = False
    tempFedId = ""
    for x in response.text:
        if x == "`":
            if In:
                In = False
                fedList.append(tempFedId)
                tempFedId = ""
            else:
                In = True

        elif In:
            tempFedId += x

    await event.edit(f"UNFBANNING IN {len(fedList)} FEDS BY {lightning}.")
    try:
        await bot.send_message(chat, f"/start")
    except BaseException:
        await event.edit("PM_PERMIT_GROUP_ID  is incorrect.")
        return
    await asyncio.sleep(5)
    for fed in fedList:
        await bot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(5)
        await bot.send_message(chat, f"/unfban {FBAN}")
        await asyncio.sleep(5)
    await event.edit(f"Superfban cmpleted Affected {len(fedList)} Feds by {lightning}.\n")



CMD_HELP.update(
    {
        "superfban": ".superfban <username/userid> <reason> "

    }
)
