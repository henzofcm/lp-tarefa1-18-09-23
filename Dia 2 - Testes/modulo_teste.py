import unittest
import aplicativo as app

class TesteDias(unittest.TestCase):
    Dia_1 = "10 de outubro de 2020"
    Dia_2 = "10 de novembro de 2020"
    
    def dia_crescente(self):
       self.assertEqual(app.numero_de_dias_entre_datas(Dia_1, Dia_2), 30)
       self.assertEqual(app.numero_de_dias_entre_datas("10 de Outubro de 2020", Dia_2), 30)
       self.assertEqual(app.numero_de_dias_entre_datas("08 de Outubro de 2020",Dia_2), 30)
        
    def dia_decrescente(self):
        self.assertEqual(Dia_2 + " - " + Dia_1, 30)
        
    def dia_invalido(self):
        self.assertEqual(app.numero_de_dias_entre_datas("35 de Janeiro de 2020", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("-10 de Janeiro de 2020", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("ab de Janeiro de 2020", Dia_2), 30)
        
    def mes_invalido(self):
        self.assertEqual(app.numero_de_dias_entre_datas("10 de Januario de 2020", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("30 de Fevereiro de 2020", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("10 de fEvEreir@ de 2020" , Dia_2), 30)
        
    def ano_invalido(self):
        self.assertEqual(app.numero_de_dias_entre_datas("10 de Outubro de Trinta", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("10 de Outubro de 2a2$", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("10 de Outubro de 0", Dia_2), 30)
        self.assertEqual(app.numero_de_dias_entre_datas("10 de Outubro de -100", Dia_2), 30)
        
if __name__ == '__main__':
    unittest.main()