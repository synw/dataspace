from ..core.env import is_running_in_browser


class HtmlColors:
    def red(self, *msg):
        color = "red"
        return self._msg(color, *msg)

    def blue(self, *msg):
        color = "steelblue"
        return self._msg(color, *msg)

    def green(self, *msg):
        color = "forestgreen"
        return self._msg(color, *msg)

    def yellow(self, *msg):
        color = "yellow"
        return self._msg(color, *msg)

    def purple(self, *msg):
        color = "purple"
        return self._msg(color, *msg)

    def bold(self, *msg):
        res = []
        for m in msg:
            res.append(str(m))
        txt = " ".join(res)
        return f'<span style="font-weight:bold">{txt}</span>'

    def underline(self, *msg):
        res = []
        for m in msg:
            res.append(str(m))
        txt = " ".join(res)
        return f'<span style="text-decoration:underline">{txt}</span>'

    def _msg(self, color, *msg):
        res = []
        for m in msg:
            res.append(str(m))
        txt = " ".join(res)
        return f'<span style="color:{color}">{txt}</span>'


class Colors:
    def red(self, *msg):
        color = "\033[91m"
        return self._msg(color, *msg)

    def blue(self, *msg):
        color = "\033[94m"
        return self._msg(color, *msg)

    def green(self, *msg):
        color = "\033[92m"
        return self._msg(color, *msg)

    def yellow(self, *msg):
        color = "\033[93m"
        return self._msg(color, *msg)

    def purple(self, *msg):
        color = "\033[95m"
        return self._msg(color, *msg)

    def bold(self, *msg):
        color = "\033[1m"
        return self._msg(color, *msg)

    def underline(self, *msg):
        color = "\033[4m"
        return self._msg(color, *msg)

    def _msg(self, color, *msg):
        res = []
        for m in msg:
            res.append(str(m))
        txt = " ".join(res)
        col = color + txt + "\033[0m"
        return col


if is_running_in_browser is True:
    colors = HtmlColors()
else:
    colors = Colors()
