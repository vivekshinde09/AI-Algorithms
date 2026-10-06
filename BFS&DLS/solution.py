class Graph:

    def __init__(self):
        # self.graph = {
        #     'A': ['B', 'C', 'D'],
        #     'B': ['E', 'F'],
        #     'C': ['G', 'H'],
        #     'D': ['I', 'J'],
        #     'E': ['K', 'L'],
        #     'F': ['M'],
        #     'G': ['N'],
        #     'H': [],
        #     'I': ['O'],
        #     'J': [],
        #     'K': [],
        #     'L': [],
        #     'M': [],
        #     'N': [],
        #     'O': []
        #     }
        self.graph={}

    def getInput(self):
        nodes=int(input("Enter number of vertice present in Graph:"))
        for i in range(nodes):
            parent=input("Enter the parent key:")
            childs=int(input("Enter the childs present:"))
            child_nodes=[]
            for j in range(childs):
                node=input("Enter child node:")
                child_nodes.append(node)
            self.graph[parent]=child_nodes
        return self.graph

    def BredthFirst(self,start):
        visited=[]
        queue=[]
        visited.append(start)
        queue.append(start)
        while queue:
            curr=queue.pop(0)
            print(curr , end=" ")
            for neighbour in self.graph[curr]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    
    def Depthlimited(self,start,goal,limit):

        if start==goal:
            print("Goal Found.")
            return True
        if limit==-1:
            return False

        for neighbour in self.graph[start]:
            if self.DepthFirst(neighbour,goal,limit-1):
                return True
        return False


    def Display(self):
        print("-----Graph-----")
        for key,val in self.graph.items():
            print(f"{key} -> {val}")

g=Graph()

            
while True:
    print("\n")
    print("For Setting graph press 1.")
    print("For Display graph press 2.")
    print("For applying Depth Limited Search press 3.")
    print("For applying Bredth First Search press 4.")
    print("For Exit press 5.")
    choice=int(input("Enter the choice:"))

    match choice:
        case 1:
            print("Follow the instructions to set the Graph.",end="\n")
            g.getInput()
        case 2:
            g.Display()
        case 3:
            g.Depthlimited()
        case 4:
            g.BredthFirst()
        case 5:
            print("Exiting...")
            break
        case _:
            print("Enter the choice as per the Instruction.")
