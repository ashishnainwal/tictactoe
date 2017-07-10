#!/usr/bin/env python

# from IPython.display import clear_output

#Define the board"
lst = ['k0','k1','k2','k3','k4','k5','k6','k7','k8']

#take player's names

players = []

def player_name():
	player1 = raw_input("Enter Player1's name:")
	player2 = raw_input("Enter Player2's name:")
	global players
	players = [player1,player2]
	print 'players are', players[0],':symbol is X and',players[1],':symbol is O'

player_name()
print players[0]

def show_board():
#	clear_output()
	print lst[0],'|',lst[1],'|',lst[2]
	print '--------------'
	print lst[3],'|',lst[4],'|',lst[5]
	print '--------------'
	print lst[6],'|',lst[7],'|',lst[8]

#show board first time
show_board()

value = ['X','O']

def take_input(playername):
	while 1:
		print 'Your turn user', playername
		global cell
		global lst
		cell = raw_input('which cell:')
		x = lst.count(cell)
		if (x != 1):
			print 'invalid cell'
			continue
		else:
			break

def update_board(cell,value):
    index = int(cell[1])
    lst[index] = value
    print 'inserting', value, 'to the cell', cell

result = 0

def success(playername):
	global result
	if ((lst[0] == lst[1]) and (lst[1] == lst[2])):
		result = 1
		print playername, 'has won'
	elif (lst[0] == lst[3]) and (lst[3] == lst[6]):
		result = 1
		print playername, 'has won'
	elif (lst[0] == lst[4]) and (lst[4] == lst[8]):
		result = 1
		print playername, 'has won'
	elif (lst[3] == lst[4]) and (lst[4] == lst[5]):
		result = 1
		print playername, 'has won'
	elif (lst[6] == lst[7]) and (lst[7] == lst[8]):
		result = 1
		print playername, 'has won'
	elif (lst[1] == lst[4]) and (lst[4] == lst[7]):
		result = 1
		print playername, 'has won'
	elif (lst[2] == lst[5]) and (lst[5] == lst[8]):
		result = 1
		print playername, 'has won'
		
	

#main program

#define player key
key=1

for i in range(9):
	global key
	global result
	if key==1:
		key=0
	elif key==0:
		key =1
	
	take_input(players[key])
	
	update_board(cell,value[key])
	
	show_board()
	
	success(players[key])
	
	if result == 1:
		break
	
	
if result == 0:
	print 'GAME DRAW'	

