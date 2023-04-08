def check_win(pile):
    if(pile[0] == 0 or pile[1] == 0):
        return 1
    else:
        return 0
    
def check_points(player,pile):
    points = 0
    points = (pile[0] * 2) + (pile[1] * 3)
    if(player == 'human'):
        points = -abs(points)

    return points

def next_move(pile):
    new_pile = []
    new_pile.append([pile[0]-1,pile[1]])
    new_pile.append([pile[0],pile[1]-1])

    return new_pile


def minmax(player,pile):
    best = [0,0]
    temp_v = 0
    v = 0
    if(check_win(pile)):
        points = check_points(player,pile)
        return points,None
    
    if(player == 'computer'):
        v = float('-inf')
        moves = next_move(pile)
        for i in moves:
            temp = minmax('human',i)
            temp_v = temp[0]
            #print(temp)
            if(temp_v > v):
                v = temp_v
                best = i
    else:
        v = float('inf')
        moves = next_move(pile)
        for i in moves:
            temp = minmax('computer',i)
            temp_v = temp[0]
            #print(temp)
            if(temp_v < v):
                v = temp_v
                best = i

    #print('v',v)
    #print('best',best)
    return [v,best]

def minmax_ab(player,pile,alpha=-10000000, beta=10000000):
    best = [0,0]
    temp_v = 0
    v = 0
    if(check_win(pile)):
        points = check_points(player,pile)
        return points,None
    
    if(player == 'computer'):
        v = float('-inf')
        moves = next_move(pile)
        for i in moves:
            temp = minmax_ab('human',i,alpha,beta)
            temp_v = temp[0]
            #print(temp)
            if(temp_v > v):
                v = temp_v
                best = i
            if(temp_v >= beta):
                break
            if(alpha < temp_v):
                alpha = temp_v

    else:
        v = float('inf')
        moves = next_move(pile)
        for i in moves:
            temp = minmax_ab('computer',i,alpha,beta)
            temp_v = temp[0]
            #print(temp)
            if(temp_v < v):
                v = temp_v
                best = i
            if(temp_v <= alpha):
                break
            if(beta > temp_v):
                beta = temp_v

    #print('v',v)
    #print('best',best)
    return [v,best]

def initial_input():
    pile = []
    red = int(input("Number of red marbles:"))
    blue = int(input("Number of blue marbles:"))
    player = str(input("Enter the initial player:"))

    pile.append(red)
    pile.append(blue)

    return player,pile

def human_play(pile):
    if(check_win(pile)):
        final_sore = abs(check_points('human',pile))
        print("Human wins!")
        print("Human score:",final_sore)
    else:
        print("It's your turn!")
        print("Marble count:")
        print("Red:",pile[0])
        print("Blue:",pile[1])
        print("Enter 'red' or 'blue' to remove a marble from that pile:")
        move_pile = str(input("Pile colour:"))

        if(move_pile == "red"):
            pile[0] = pile[0] - 1
        elif(move_pile == "blue"):
            pile[1] = pile[1] - 1
        else:
            print("Invalid selection!")
        
        computer_play(pile)

def computer_play(pile):
    if(check_win(pile)):
        final_sore = check_points('computer',pile)
        print("Computer wins!")
        print("Computer score:",final_sore)
    else:
        score,best_move = minmax_ab('computer',pile)
        print()
        if(pile[0] != best_move[0]):
            print("Computer has selected RED pile and removed a marble")
        if(pile[1] != best_move[1]):
            print("Computer has selected BLUE pile and removed a marble")
        pile[0] = best_move[0]
        pile[1] = best_move[1]
        print("Pile status after computer move:",best_move)
        print()

        human_play(pile)
    #print(best_move)

def main():
    player, pile = initial_input()
    if(player == 'computer'):
        computer_play(pile)
    if(player == 'human'):
        human_play(pile)

main()
#print(minmax_ab('computer',pile))