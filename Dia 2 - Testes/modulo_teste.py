import unittest

class TesteDias(unittest.TestCase):
    Dia_1 = "10 de outubro de 2020"
    Dia_2 = "10 de novembro de 2020"
    
    def dia_crescente(self):
       self.assertEqual(30, Dia_1 + " - " + Dia_2)
       self.assertEqual(30, "10 de Outubro de 2020" + " - " + Dia_2)
       self.assertEqual(32, "08 de Outubro de 2020" + " - " + Dia_2)
        
    def dia_decrescente(self):
        self.assertEqual(30, Dia_2 + " - " + Dia_1)
        
    def dia_invalido(self):
        self.assertEqual(30, "35 de Janeiro de 2020" + " - " + Dia_2)
        self.assertEqual(30, "-10 de Janeiro de 2020" + " - " + Dia_2)
        self.assertEqual(30, "ab de Janeiro de 2020" + " - " + Dia_2)
        
    def mes_invalido(self):
        self.assertEqual(30, "10 de Januario de 2020" + " - " + Dia_2)
        self.assertEqual(30, "30 de Fevereiro de 2020" + " - " + Dia_2)
        self.assertEqual(30, "10 de fEvEreir@ de 2020" + " - " + Dia_2)
        
    def ano_invalido(self):
        self.assertEqual(30, "10 de Outubro de Trinta" + " - " + Dia_2)
        self.assertEqual(30, "10 de Outubro de 2a2$" + " - " + Dia_2)
        self.assertEqual(30, "10 de Outubro de 0" + " - " + Dia_2)
        self.assertEqual(30, "10 de Outubro de -100" + " - " + Dia_2)