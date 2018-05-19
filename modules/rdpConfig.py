class RdpConfig:
    def __init__(self, prog):
        self.prog = prog
        pass
    def getDefaultCmd(self):
        return (self.prog + ' --plugin cliprdr --ntlm --composition -x m -u Administrator -p "xxxxxxxx" -g 1920x1000 xxxxxxx')