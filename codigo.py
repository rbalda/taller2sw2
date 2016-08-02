class Control():
        def valor_acceso(self, codigo, dia, hora):
                if(codigo > 0 and dia > 0):
                        contarDigito=0
                        for cifra in codigo:
                                contarDigito +=1
                                if(contarDigito > 7 or contarDigito < 7):
                                        print("Codigo incorrecto")
                                        #break
                                else:
                                        if(codigo[0] == '0' and codigo[1] == '0'):
                                                print("Es un trabajador")
                                                if(dia == 1 or dia == 2 or dia ==3 or dia == 4 or dia == 5):
                                                        print("ACCESO PERMITIDO")
                                                        print("Este dia tiene acceso a las 24 horas")
                                                        if ((dia == 6 or dia == 7) and (hora >= 10 and hora <= 15)):
                                                                print("ACCESO PERMITIDO")
                                                                #print("Este dia tiene acceso de 10:00 a 15:00 horas)
                                                        elif(hora < 10 or hora > 15):
                                                                print("ACCESO DENGADO")
                                                                print("Este dia tiene acceso de 10:00 a 15:00 horas")
                                                        
                                                        
                                                
                                        elif(codigo[0] != '0' and codigo[1] != '0'):
                                                print("Es un estudiante")
                                                if((dia == 1 or dia == 2 or dia ==3 or dia == 4 or dia == 5) and (hora > 8 and hora < 18 )):
                                                        print("ACCESO PERMITIDO de 8 a 18 ")
                                                else:
                                                        print("ACCESO denegado solo de L - V de 8 a 18 ")
                                                        
                                                        

                                                        
                                                        
                                                        
                                
                                    
                                    
                       
