from math import log


class CalculaIPv4:
    def __init__(self, ip, mascara=None, cidr=None):
        self._ip = ip
        self._mascara = mascara
        self._cidr = cidr
        self._rede = None
        self._numips = 0
        self._broadcast = None
        self.trata_dados()
        self.calcula_rede()
        self.calcula_broadcast()
        self._numips = pow(2, 32 - self._cidr) - 2
        print(f'IP: ', self._ip)
        print(f'Máscara: ', self._mascara)
        print(f'Rede: ', self._rede)
        print(f'Broadcast: ', self._broadcast)
        print(f'Prefixo: ', self._cidr)
        print(f'Número de IPs da rede: ', self._numips)

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def cidr(self):
        return self._cidr

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @staticmethod
    def octetos(string):
        return string.split('.')

    @staticmethod
    def transforma_bin(num):
        byte = [0, 0, 0, 0, 0, 0, 0, 0]
        div = [128, 64, 32, 16, 8, 4, 2, 1]
        num = int(num)
        for v in range(8):
            if num / div[v] >= 1:
                byte[v] = '1'
                num = num % div[v]
            else:
                byte[v] = '0'
        return byte

    def transforma_cidr(self):
        mascara = ['0', '0', '0', '0']
        var = '255'
        intervalo = int(self._cidr / 8)
        for x in range(intervalo):
            mascara[x] = var
        if intervalo < 4:
            n = 8 - self._cidr % 8
            mascara[intervalo] = str(pow(2, 8) - pow(2, n))
            self._mascara = '.'.join(x for x in mascara)

    def transforma_mascara(self):
        octetos = self.octetos(self._mascara)
        for x in range(3, 0, -1):
            var = int(octetos[x])
            if var:
                if var == 255:
                    cidr = 8 * x
                    self._cidr = cidr
                else:
                    cidr = 32 - log(256 - var, 2)
                    self._cidr = int(cidr)
                return None

    def calcula_rede(self):
        ip = self.octetos(self._ip)
        ip[3] = '0'
        self._rede = '.'.join(x for x in ip)

    def calcula_broadcast(self):
        ip = self.octetos(self._ip)
        ip[3] = str(pow(2, 32 - self._cidr) - 1)
        self._broadcast = '.'.join(x for x in ip)

    def trata_dados(self):
        if self._mascara is None:
            self.transforma_cidr()
        else:
            self.transforma_mascara()

    def imprime_bin(self, num):
        var_bin = ['0', '0', '0', '0']
        for x in range(4):
            var = self.octetos(num)
            var_bin[x] = ''.join(x for x in self.transforma_bin(int(var[x])))
        print('.'.join(x for x in var_bin))
