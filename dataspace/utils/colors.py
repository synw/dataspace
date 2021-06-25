# -*- coding: utf-8 -*-


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


colors = Colors()
