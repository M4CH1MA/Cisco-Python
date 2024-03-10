#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import telnetlib

class main():
	def __init__(self):
		equipamentos = [{'ip':'192.168.243.132', 'usuario':'cisco', 'senha':'cisco'}]

		vetor_obj = []

		for i in equipamentos:
			vetor_obj.append(conexao_equipamento(i))

		for j in vetor_obj:
			j.start_conn()



class conexao_equipamento():
	def __init__(self, dado):
		self.ip = dado['ip']
		self.usuario = dado['usuario']
		self.senha = dado['senha']

	def start_conn(self):
		self.tn = telnetlib.Telnet()
		self.tn.open(self.ip, '23', 100)
		self.tn.read_until(b':') #comando para esperar o outro comando executar
		self.tn.write((self.usuario+'\n').encode())
		self.tn.read_until(b':') 
		self.tn.write((self.senha+'\n').encode())
		saida = self.tn.read_until(b'#').decode() # Aguarda o caracter # R1# 
		print(saida)

if __name__ == "__main__":
	main()
