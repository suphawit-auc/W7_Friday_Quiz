#!/usr/bin/env python
# coding: utf-8

# In[12]:


board= [["-","-","-"],["-","-","-"],["-","-","-"]]
game_stillplay=True
winner=None
currentplayer="X"
def showboard():
    print(board[0][0]+" | "+board[0][1]+" | "+board[0][2])
    print(board[1][0]+" | "+board[1][1]+" | "+board[1][2])
    print(board[2][0]+" | "+board[2][1]+" | "+board[2][2])


# In[13]:


def playerturn(currentplayer):
    #list1=[board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]]
    list1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    position=int(input("Choose where you want to place from 1-9: "))
    board[list1[position-1][0]][list1[position-1][1]]=currentplayer
    showboard()


# In[14]:


def startgame():
    showboard()
    while game_stillplay:
        print(currentplayer+' Turn')
        playerturn(currentplayer)
        gameend()
        swapplayer()
    if winner=='X':
        print ('X is the winner!!')
    elif winner=='O':
        print ('O is the winner!!')
    elif winner==None:
        print('Tie game!!')


# In[15]:


def gameend():
    checkwin()
    checktie()


# In[16]:


def checkwin():
    global winner
    winrow=checkrow()
    wincolumn=checkcolumn()
    windiago=checkdiago()
    if winrow:
        winner=winrow
    elif wincolumn:
        winner=wincolumn
    elif windiago:
        winner=windiago
    else:
        winner=None
    


# In[17]:


def checkrow():
    global game_stillplay
    #row1=board[0]!="-"
    #row2=board[1]!="-"
    #row3=board[2]!="-"
    row1=board[0][0]==board[0][1]==board[0][2]!="-"
    row2=board[1][0]==board[1][1]==board[1][2]!="-"
    row3=board[2][0]==board[2][1]==board[2][2]!="-"
    if row1 or row2 or row3:
        game_stillplay=False
    if row1:
        return board[0][0]
    if row2:
        return board[1][0]
    if row3:
        return board[2][0]


# In[18]:


def checkcolumn():
    global game_stillplay
    column1=board[0][0]==board[1][0]==board[2][0]!="-"
    column2=board[0][1]==board[1][1]==board[2][1]!="-"
    column3=board[0][2]==board[1][2]==board[2][2]!="-"
    if column1 or column2 or column3:
        game_stillplay=False
    if column1:
        return board[0][0]
    if column2:
        return board[0][1]
    if column3:
        return board[0][2]


# In[19]:


def checkdiago():
    global game_stillplay
    diago1=board[0][0]==board[1][1]==board[2][2]!="-"
    diago2=board[0][2]==board[1][1]==board[2][0]!="-"
    if diago1 or diago2:
        game_stillplay=False
    if diago1:
        return board[2][2]
    if diago2:
        return board[2][0]


# In[20]:


def swapplayer():
    global currentplayer
    if currentplayer=='X':
       
        currentplayer='O'
    elif currentplayer=='O':
        currentplayer='X'
        


# In[21]:


def checktie():
    global game_stillplay
    for k in board:
        if '-' in k :
            break;
    else:
        game_stillplay=False
    


# In[ ]:


startgame()


# # 

# ##### 

# In[ ]:




