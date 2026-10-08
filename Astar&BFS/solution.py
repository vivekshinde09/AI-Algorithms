import heapq

class Graph:


    def __init__(self):
        self.graph = {}
        self.nodes = 0
        self.distance = []
        self.h_distance = []

        # Already given data - kept unchanged
        # self.graph = {
        #     'A': [('B', 2), ('C', 4)],
        #     'B': [('D', 3), ('E', 5)],
        #     'C': [('F', 4)],
        #     'D': [('G', 2)],
        #     'E': [('G', 3)],
        #     'F': [('G', 2)],
        #     'G': []
        # }

        # self.h_distance = {
        #     'A': 7,
        #     'B': 5,
        #     'C': 4,
        #     'D': 2,
        #     'E': 3,
        #     'F': 2,
        #     'G': 0
        # }


    def getInput(self):

        self.nodes = int(input("Enter number of nodes present in graph:"))

        for i in range(self.nodes):

            node = input("Enter the source node:")

            self.h_distance.append(
                input(f"Enter the heuristic distance of node {node} :")
            )

            childs = int(
                input(f"Enter present child nodes for node {node}:")
            )

            child_nodes = []

            for j in range(childs):

                info = []

                info.append(
                    input(f"Enter the child node {j+1}:")
                )

                info.append(
                    int(input("Enter the distance :"))
                )

                child_nodes.append(info)

            self.graph[node] = child_nodes

        self.distance = [99 for i in range(self.nodes)]
        self.distance[0] = 0


    def Display(self):

        print()

        for node, childs in self.graph.items():

            print(node, end=" : ")

            for child in childs:
                print(child, end=" ")

            print()

        print()


    def a_star(self,start,goal):
    
        open_list=[]
        close_list=[]
        parent={}
        path=[]
        g={start:0}

        h=self.h_distance[start]

        f=h+g[start]
        heapq.heappush(open_list,(f,start))
        while len(open_list)!=0:

            f,curr_node=heapq.heappop(open_list)
            close_list.append(curr_node)

            if curr_node==goal:
                current=goal
                while current!=start:   
                    path.append(current)
                    current=parent[current]
                path.append(start)
                path.reverse()
                print(f"The goal is found, the minimum distance is {f}")
                print(f"Path:","->".join(path))
                return

            for child_node,dist in self.graph[curr_node]:
                new_g=g[curr_node]+dist
                h=self.h_distance[child_node]
                f=new_g+h

                if child_node not in g or new_g<g[child_node]:
                    g[child_node]=new_g
                    heapq.heappush(open_list,(f,child_node))
                    parent[child_node]=curr_node


    def best_first_search(self,graph, heuristic, start, goal):

        open_list = []
        closed_list = []

        # (heuristic, node)
        heapq.heappush(
            open_list,
            (heuristic[start], start)
        )

        while len(open_list) != 0:

            h, current = heapq.heappop(open_list)

            print("Visiting:", current, "h =", h)

            if current == goal:

                print("Goal found!")

                return

            closed_list.append(current)

            for child, cost in graph[current]:

                if child not in closed_list:

                    h = heuristic[child]

                    heapq.heappush(
                        open_list,
                        (h, child)
                    )

    print("Goal not found!")
    

# ---------------------------------------

# MAIN PROGRAM

# ---------------------------------------

g = Graph()

while True:


    print("\n========== AI SEARCH ALGORITHMS ==========")
    print("1. Give graph info")
    print("2. Display Graph")
    print("3. A* Search")
    print("4. Best First Search")
    print("5. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")
    match choice:
        
        case 1:
            g.getInput()
        case 2:
            g.Display()
        case 3:
            start = input("Enter start node: ").upper()
            goal = input("Enter goal node: ").upper()
        
            g.a_star(start, goal)
            
        case 4:
            start = input("Enter start node: ").upper()
            goal = input("Enter goal node: ").upper()
            
                    # Your original function is kept unchanged.
            g.best_first_search(g.graph,g.h_distance,start,goal)
        case 5:
            print("Program ended.")
            break
        case _:
            print("Invalid choice! Press again.")
    