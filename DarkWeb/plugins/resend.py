# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from Dark.utils import admin_cmd, sudo_cmd
from DarkWeb.cmdhelp import CmdHelp


@dark.on(admin_cmd(pattern="resend"))
@dark.on(sudo_cmd(pattern="resend", allow_sudo=True))
async def _(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)

CmdHelp("resend").add_command(
  "resend", "<reply>", "Resends the replied message in current chat"
).add()