import datetime
from dateutil.relativedelta import relativedelta

from .colors import colors


START_TIME = None


def _unpack_msg(*msg):
    """
    Convert all message elements to string
    """
    li = []
    for m in msg:
        li.append(str(m))
    return " ".join(li)


def _msg(label, *msg):
    """
    Prints a message with a label
    """
    txt = _unpack_msg(*msg)
    print("[" + label + "] " + txt)


def msg_info(*msg):
    """
    Prints a message with an info prefix
    """
    label = colors.blue("INFO")
    _msg(label, *msg)


def msg_start(*msg):
    """
    Prints an start message
    """
    global START_TIME
    START_TIME = datetime.datetime.now()
    label = colors.purple("START")
    _msg(label, *msg)


def _endmsg(rd) -> str:
    """
    Returns an end message with elapsed time
    """
    msg = ""
    s = ""
    if rd.hours > 0:
        if rd.hours > 1:
            s = "s"
        msg += colors.bold(str(rd.hours)) + " hour" + s + " "
    s = ""
    if rd.minutes > 0:
        if rd.minutes > 1:
            s = "s"
        msg += colors.bold(str(rd.minutes)) + " minute" + s + " "
    # if rd.seconds > 0:
    #    msg+=str(rd.seconds)
    # else:
    #    msg+="0."
    milliseconds = int(rd.microseconds / 1000)
    if milliseconds > 0:
        msg += colors.bold(str(rd.seconds) + "." + str(milliseconds))
    msg += " seconds"
    return msg


def msg_end(self, *msg):
    """
    Prints an end message with elapsed time
    """
    global START_TIME
    if START_TIME is None:
        raise Exception(
            "No start time set: please use start() " "before using this function"
        )
    endtime = datetime.datetime.now()
    rd = relativedelta(endtime, START_TIME)
    endmsg = _endmsg(rd)
    label = colors.purple("END")
    msg += ("in " + endmsg,)
    _msg(label, *msg)
    START_TIME = None


def msg_warning(*msg):
    """
    Prints a warning
    """
    label = colors.yellow("WARNING")
    _msg(label, *msg)


def msg_ok(*msg):
    """
    Prints a message with an ok prefix
    """
    label = colors.green("OK")
    _msg(label, *msg)
