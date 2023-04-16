""" 
By :- @PhycoNinja13b
modified by :- @veryhelpful

 """

from telethon import events
from Dark.utils import admin_cmd

normiefont = ['a',  'b',  'c', 'd',   'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',
              'v',  'w',  'x',  'y',  'z']
circlefont = ['a⃠', 'b⃠', 'c⃠', 'd⃠', 'e⃠', 'f⃠', 'g⃠', 'h⃠', 'i⃠', 'j⃠', 'k⃠', 'l⃠', 'm⃠', 'n⃠', 'o⃠', 'p⃠', 'q⃠', 'r⃠', 's⃠', 't⃠', 'u⃠',
              'v⃠', 'w⃠', 'x⃠', 'y⃠', 'z⃠']

@dark.on(admin_cmd(pattern="bfc ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`give me a text `")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            circlecharacter = circlefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, circlecharacter)
    await event.edit(string)
    

   




