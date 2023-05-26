SuccList = {'Oradea':[['Zerind',374],['Sibiu',253]],'Zerind':[['Oradea',380],['Arad',366]],
          'Arad':[['Timisoara',329],['Sibiu',253],['Zerind',374]],
          'Timisoara':[['Arad',366],['Lugoj',244]],
          'Lugoj':[['Timisoara',329],['Mehadia',241]],
          'Mehadia':[['Lugoj',244],['Dobreta',242]],
          'Dobreta':[['Mehadia',241],['Craiova',160]],
          'Craiova':[['Dobreta',242],['Rimnicu Vilcea',193],['Pitesti',100]],
          'Sibiu':[['Arad',366],['Oradea',380],['Rimnicu Vilcea',193],['Fagaras',176]],
          'Rimnicu Vilcea':[['Sibiu',253],['Craiova',160],['Pitesti',100]],
          'Fagaras':[['Sibiu',253],['Bucharest',0]],
          'Pitesti':[['Bucharest',0],['Rimnicu Vilcea',193],['Craiova',160]],
          'Bucharest':[['Fagaras',176],['Pitesti',100],['Giurgiu',77],['Urziceni',80]],
          'Giurgiu':[['Bucharest',0]],
          'Urziceni':[['Bucharest',0],['Hirsova',151],['Vaslui',199]],
          'Hirsova':[['Urziceni',80],['Eforie',161]],
          'Eforie':[['Hirsova',151]],
          'Vaslui':[['Urziceni',80],['Iasi',226]],
          'Iasi':[['Neamt',234],['Vaslui',199]],
          'Neamt':[['Iasi',226]]}

Start='Arad'
Goal='Bucharest'
Closed = []
SUCCESS=True
FAILURE=False
State=FAILURE

def MOVEGEN(N):
	New_list=[]
	if N in SuccList.keys():
		New_list=SuccList[N]
	
	return New_list
	
def GOALTEST(N):
	if N == Goal:
		return True
	else:
		return False

def APPEND(L1,L2):
	New_list=list(L1)+list(L2)
	return New_list
	
def SORT(L):
	L.sort(key = lambda x: x[1]) 
	return L 
	
def BestFirstSearch():
	OPEN=[[Start,5]]
	CLOSED=[]
	global State
	global Closed
	while (len(OPEN) != 0) and (State != SUCCESS):
		print("------------")
		N= OPEN[0]
		print("N=",N)
		del OPEN[0] #delete the node we picked
		
		if GOALTEST(N[0])==True:
			State = SUCCESS
			CLOSED = APPEND(CLOSED,[N])
			print("CLOSED=",CLOSED)
		else:
			CLOSED = APPEND(CLOSED,[N])
			print("CLOSED=",CLOSED)
			CHILD = MOVEGEN(N[0])
			print("CHILD=",CHILD)
			for val in CLOSED:
				if val in CHILD:
					CHILD.remove(val)
			for val in OPEN:
				if val in CHILD:
					CHILD.remove(val)
			OPEN = APPEND(CHILD,OPEN) #append movegen elements to OPEN
			print("Unsorted OPEN=",OPEN)
			SORT(OPEN)
			print("Sorted OPEN=",OPEN)
			
	Closed=CLOSED
	return State
	
#Driver Code
result=BestFirstSearch() #call search algorithm
print(Closed,result)




















