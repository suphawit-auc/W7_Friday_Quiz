class Board :
    def __init__(self): #ATTRIBUTE
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.game_stillplay = True
        self.winner = None
        self.player = "X"
        self.turn = 0
    def clearBoard(self): #CLEAR BOARD
        printer = Printer()
        for i in range(3) :
            for j in range(3) :
                self.board[i][j] = "-"
        printer.show(self)
    def win_Check(self): #WIN CHECK CONDITION
        #CHECK ROW
        row1 = self.board[0][0] == self.board[0][1] == self.board[0][2] != "-"
        row2 = self.board[1][0] == self.board[1][1] == self.board[1][2] != "-"
        row3 = self.board[2][0] == self.board[2][1] == self.board[2][2] != "-"
        if row1 or row2 or row3:
            self.game_stillplay=False
        if row1:
            self.winner= self.board[0][0]
        if row2:
            self.winner= self.board[1][0]
        if row3:
            self.winner= self.board[2][0]
        #CHECK COLUMN
        column1 = self.board[0][0] == self.board[1][0] == self.board[2][0] != "-"
        column2 = self.board[0][1] == self.board[1][1] == self.board[2][1] != "-"
        column3 = self.board[0][2] == self.board[1][2] == self.board[2][2] != "-"
        if column1 or column2 or column3:
            self.game_stillplay = False
        if column1:
            self.winner = self.board[0][0]
        if column2:
            self.winner = self.board[0][1]
        if column3:
            self.winner = self.board[0][2]
	#CHECK CROSS
        diago1 = self.board[0][0] == self.board[1][1] == self.board[2][2] != "-"
        diago2 = self.board[0][2] == self.board[1][1] == self.board[2][0] != "-"
        if diago1 or diago2:
            self.game_stillplay = False
        if diago1:
            self.winner = self.board[2][2]
        if diago2:
            self.winner = self.board[2][0]
    def tie_Check(self):
        for k in self.board:
            if '-' in k :
                break;
        else:
            self.game_stillplay = False
    def startgame(self):
        textinput = TextInput()
        printer = Printer()
        printer.show(self)
        while self.game_stillplay:
            print(self.player + ' Turn')
            textinput.getInput(self)
            #self.sameCheck()
            printer.show(self)
            self.win_Check()
            self.tie_Check()
            if self.player == 'X':
                self.player = 'O'
            elif self.player == 'O':
                self.player = 'X'
        if self.winner == 'X':
            print ('X is the winner!!\n')
            table.clearBoard()
        elif self.winner == 'O':
            print ('O is the winner!!\n')
            table.clearBoard()
        elif self.winner == None:
            print('Tie game!!\n')
            table.clearBoard()
    def getChar(self,position):
        list1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        return self.board[list1[position-1][0]][list1[position-1][1]]
    def setChar(self,position):
        list1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        if(self.error_check(position)):
            self.board[list1[position-1][0]][list1[position-1][1]]=self.player
    def error_check(self,position):
        list1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        if self.board[list1[position-1][0]][list1[position-1][1]]!='-':
            if(self.player=='X'):
                self.player='O'
            elif(self.player=='O'):
                self.player='X'
            return False
        else:
            return True
class Printer :
    def show(self,obj):
        print(obj.getChar(1) + " | " + obj.getChar(2) + " | " + obj.getChar(3))
        print(obj.getChar(4) + " | " + obj.getChar(5) + " | " + obj.getChar(6))
        print(obj.getChar(7) + " | " + obj.getChar(8) + " | " + obj.getChar(9))
class TextInput() :
    def getInput(self,obj):
        position = int(input("Choose where you want to place from 1-9: "))
        obj.setChar(position) 
table = Board()
table.startgame()
