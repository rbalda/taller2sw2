import codigo, tarjeta, codigo

class Pasaje():
        #is_saldo = true/false , dia, valor
        def valor_tiene_tarjeta(self, dia, is_saldo, valor):
                tarjeta.una_tarjeta("janina", 1, codigo.valor_acceso('0012345',1, 12))
                return("tiene tarjeta")

        def valor_cobrar(self, dia, valor, is_saldo):
                if(dia==1 or dia == 2 or dia == 3 or dia == 4):
                        #valor = 0,25
                        if(is_saldo == 1 and valor == 0.25):
                                print("Se cobro exitosamente")
                                return 1
                        else:
                                print("No tienes saldos")
                                return 0

                elif(dia == 5 ):
                        print("Es Gratis!")
                        return 1
                else:
                        print("Dia no valido")
                        return 0
                    
                        
                    
                   
                       
                       
                       
