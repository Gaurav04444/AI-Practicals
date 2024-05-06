from collections import dequeue

def fill_first(x,y,a):
    return(a,y)
def fill_second(x,y,b):
    return(x,b)
def empty_first(x,y,a):
    return(0,y)
def empty_second(x,y,b):
    return(x,0)
def pour_from_second_to_first(x,y,a,b):
    return(min(x+y,a),max(0,x+y-a))
def pour_from_first_to_second(x,y,a,b):
    return(max(0,x+y-b),min(x+y,b))

def bfs(initial_state,goal_state,a,b):
    queue=dequeue([(initial_state,[initial_state])])
    while queue:
        state,path=queue.popleft()
        x,y=state
        if (x<a):
            queue.append(fill_first(x,y,a),path+[fill_first(x,y,a)])
        if (y<b):
            queue.append(fill_second(x,y,b),path+[fill_second(x,y,b)])
        if (x>0):
            queue.append(empty_first(x,y,a),path+[empty_first(x,y,a)])
        if (y>0):
            queue.append(empty_second(x,y,b),path+[empty_second(x,y,b)])
        if (y>0):
            queue.append(pour_from_second_to_first(x,y,a,b),path+[pour_from_second_to_first(x,y,a,b)])
        if (x>0):
            queue.append(pour_from_first_to_second(x,y,a,b),path+pour_from_first_to_second(x,y,a,b))
    return false
                         

initial_state=(0,0)
goal_state=(4,3)
a=5
b=3
result=bfs(initial_state,goal_state,a,b)
if result:
    print("SOlution found")
    for step in result:
       	print(result)
else:
    print("result not found")


