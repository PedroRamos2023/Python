import wx
import datetime

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))
        panel = wx.Panel(self)

        self.nome_label = wx.StaticText(panel, label="Nome:", pos=(10, 10))
        self.nome_text = wx.TextCtrl(panel, pos=(100, 10))

        self.idade_label = wx.StaticText(panel, label="Idade:", pos=(10, 40))
        self.idade_text = wx.TextCtrl(panel, pos=(100, 40))

        self.calcular_botao = wx.Button(panel, label="Calcular Data de Nascimento", pos=(10, 70))
        self.calcular_botao.Bind(wx.EVT_BUTTON, self.calcular_data_nascimento)

        self.resultado_label = wx.StaticText(panel, label="", pos=(10, 100))

    def calcular_data_nascimento(self, event):
        nome = self.nome_text.GetValue()
        idade_str = self.idade_text.GetValue()

        try:
            idade = int(idade_str)
            data_atual = datetime.date.today()
            ano_nascimento = data_atual.year - idade
            resultado = f"Olá, {nome}! Você nasceu em {ano_nascimento}."
        except ValueError:
            resultado = "Por favor, insira uma idade válida."

        self.resultado_label.SetLabel(resultado)

app = wx.App()
frame = MyFrame(None, -1, "Calculadora de Data de Nacimento")
frame.Show(True)
app.MainLoop()