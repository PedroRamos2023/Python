import wx

class TicTacToeFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Jogo da Velha", size=(600, 600))
        
        self.player_x_name = ""
        self.player_o_name = ""
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.game_started = False
        
        self.panel = wx.Panel(self)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.player_x_text = wx.TextCtrl(self.panel, value="Jogador X", size=(100, -1))
        self.player_o_text = wx.TextCtrl(self.panel, value="Jogador O", size=(100, -1))
        self.start_button = wx.Button(self.panel, label="Iniciar Jogo")
        self.start_button.Bind(wx.EVT_BUTTON, self.start_game)
        
        sizer = wx.GridSizer(3, 3, 0, 0)
        for row in range(3):
            for col in range(3):
                button = wx.Button(self.panel, id=wx.ID_ANY, label='', size=(100, 100))
                button.Bind(wx.EVT_BUTTON, lambda event, r=row, c=col: self.on_button_click(event, r, c))
                self.buttons[row][col] = button
                sizer.Add(button, 0, wx.EXPAND)
        
        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel_sizer.Add(self.player_x_text, 0, wx.ALL | wx.CENTER, 5)
        self.panel_sizer.Add(self.player_o_text, 0, wx.ALL | wx.CENTER, 5)
        self.panel_sizer.Add(self.start_button, 0, wx.ALL | wx.CENTER, 5)
        self.panel_sizer.Add(sizer, 0, wx.ALL | wx.CENTER, 10)
        
        self.panel.SetSizerAndFit(self.panel_sizer)
        self.Center()
        
    def start_game(self, event):
        self.player_x_name = self.player_x_text.GetValue()
        self.player_o_name = self.player_o_text.GetValue()
        self.game_started = True
        
    def on_button_click(self, event, row, col):
        if self.game_started:
            button = self.buttons[row][col]
            if not button.Label:
                button.Label = self.current_player
                self.board[row][col] = self.current_player
                winner = self.check_winner()
                if winner:
                    wx.CallAfter(self.show_message, f"{self.get_player_name(winner)} ganhou!")
                    self.reset_board()
                elif self.is_full():
                    wx.CallAfter(self.show_message, "Empate!")
                    self.reset_board()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        # Verifica se algum jogador ganhou
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] != '':
                return self.board[row][0]
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '':
                return self.board[0][col]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return self.board[0][2]
        
        return None

    def is_full(self):
         # Verifica se o tabuleiro está cheio
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def reset_board(self):
         # Reinicia o tabuleiro
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].Label = ''
                self.board[row][col] = ''
        self.player = 'X'

    
    def get_player_name(self, player):
        # Obtém o nome do jogador com base no símbolo ('X' ou 'O')
        return self.player_x_name if player == 'X' else self.player_o_name

    def show_message(self, message):
        wx.MessageBox(message, "Fim do Jogo", wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App()
    frame = TicTacToeFrame()
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()