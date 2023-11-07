#Heuristic function based on number of misplaced tiles

def Misplaced_Tiles(self,n):
    counter=0
    self.heuristic=0
    for i in range(n*n):
        for j in range(n*n):
            if(self.state[i]!=self.goal[j]):
                counter+=1
            self.heuristic=self.heuristic+counter
    self.greedy_evaluation=self.heuristic
    return(self.greedy_evaluation)

@staticmethod

#this would remove illigal moves for a given state
def available_moves(x,n):
    moves=['Left','Right','Up','Down']
    if x%n==0:
        moves.remove('Left')
    if x%n==n-1:
        moves.remove('Right')
    if x-n<0:
        moves.remove('Up')
    if x+n>n*n-1:
        moves.remove('Down')
    return moves

#Produces children of a given state
def expand(self,n):
    x=self.state.index(0)
    moves=self.available_moves(x,n)

    children=[]
    for direction in moves:
        temp=self.state.copy()
        if direction =='Left':
            temp[x],temp[x-1]=temp[x-1],temp[x]
        elif direction=='Right':
        
        
        
    
