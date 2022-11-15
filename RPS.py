def RPS(player1,player2):

	if player1 == player2 :
		print ("Draw")
	else if player1== 'P':
		if player2=='S':
			print ("player2 wins!!")
		else :
			print ("player1 wins!!")
	else if player1=='S':
		if player2=='P':
			print ("player1 wins!!")
		else:
			print ("player2 wins!!")
	else:
		if player2=='S':
			print ("player1 wins!!")
		else:
			print ("player2 wins!!")
