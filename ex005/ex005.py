import wx
import datetime

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))
        panel = wx.Panel(self)

        self.nome_label = wx.StaticText(panel, label="Nome:", pos=(10, 10))
        self.nome_text = wx.TextCtrl(panel, pos=(100, 10))

        self.data_nascimento_label = wx.StaticText(panel, label="Data de Nascimento (AAAA-MM-DD):", pos=(10, 40))
        self.data_nascimento_text = wx.TextCtrl(panel, pos=(200, 40))

        self.enviar_botao = wx.Button(panel, label="Enviar", pos=(10, 70))
        self.Bind(wx.EVT_BUTTON, self.verificar_idade, self.enviar_botao)

        self.resultado_label = wx.StaticText(panel, label="", pos=(10, 100))
    def calcular_idade(self, data_nascimento):
        data_atual = datetime.date.today()
        data_nascimento = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
        return idade
    def verificar_idade(self, event):
        nome = self.nome_text.GetValue()
        data_nascimento = self.data_nascimento_text.GetValue()

        try:
            idade = self.calcular_idade(data_nascimento)
            if idade > 17:
                mensagem = f"Olá {nome}, você tem {idade} anos. Você já é maior de idade."
            else:
                mensagem = f"Olá {nome}, você tem {idade} anos. Você ainda é menor de idade."
            self.resultado_label.SetLabel(mensagem)
        except ValueError:
            self.resultado_label.SetLabel("Data de nascimento inválida. Use o formato AAAA-MM-DD.")

app = wx.App()
frame = MyFrame(None, -1, "Verificação de Idade")
frame.Show(True)
app.MainLoop()