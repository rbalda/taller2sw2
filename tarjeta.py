import codigo

class Tarjeta ():
    nombreCompleto = ""
    codigo
    saldo = 0

    def __init__ (self, _nombreCompleto, _codigo, _saldo):
        self.nombreCompleto = _nombreCompleto
        self.codigo = codigo.Codigo (_codigo)
        self.saldo = _saldo

    def esValida (self):
        return self.codigo.esValido()

    def haySaldoDisponible (self, pasaje):
        if self.saldo>=pasaje:
            return True
        return False

    def debitarSaldo (self, pasaje):
        self.saldo=self.saldo-pasaje


    
