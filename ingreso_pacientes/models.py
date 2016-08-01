from django.db import models

# Create your models here.
class Prestamo():
	"""
	Autor: Erika Narvaez
	Nombre de funcin: valor_total
	Entrada: valor del prestamo, y tiempo de plazo
	Salida: capital total a devolver al banco
	Descripcion: Funcion que realiza los respectivos calculos para obtener el valor a pagar del prestamo pedido en un tiempo plazo.
	"""
	def valor_total(self,prestamo,tiempo):
		if(prestamo < 5000 and tiempo <= 3):
			comision=(prestamo *2)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo >= 5000 and prestamo < 10000 and tiempo <= 6):
			comision=(prestamo*3)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.25)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo >= 10000 and prestamo <= 20000 and tiempo <= 12):
			comision=(prestamo*4)/100
			capital_total=float(prestamo+comision)
			interes=float(((capital_total*1.5)/100)*tiempo)
			return float(capital_total+interes)
		if(prestamo > 20000):
			print("El banco no puede otorgar dicho prestamo ya que excede al monto definido")
			return None


class Paciente(models.Model):
    nombres = models.CharField(max_length=500)
    apellidos = models.CharField(max_length=500)
    cedula = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s %s'%(self.apellidos,self.nombres)

class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente)
    nro_historia= models.CharField(max_length=6)


class Consulta(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica,related_name='consultas')
    fecha = models.DateField()
    diagnostico = models.CharField(max_length=500)
    codigo_diagnostico = models.CharField(unique=True,max_length=10)