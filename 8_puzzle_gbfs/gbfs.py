from state import State
from queue import PriorityQueue
def Greedy(given_state,n):
    forntier=PriorityQueue()
    explored=[]
    counter=0
    root=State(given_state,None,None,0,0)

    #root.evaluation()
    evaluation=root.Misplaced_Tiles(n)
    frontier.put((evaluation,counter,root))#To insert node

    while not frontier.empty():
        current_node=frontier.get()#complete initial state
        current_node=current_node[2]# how many initial tiels
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(),len(explored)
        children=current_node.expand(n)

        for child in children:
            if child.state not in explored:
                counter+=1
                evaluation=child.Misplaced_Tiles(n)
                frontier.put((evaluation,counter,child))
    return
        
    
