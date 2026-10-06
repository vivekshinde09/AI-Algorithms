import heapq

class Graph:


    def __init__(self):
        self.graph = {}
        self.nodes = 0
        self.distance = []
        self.h_distance = []

        # Already given data - kept unchanged
        self.graph = {
            'A': [('B', 2), ('C', 4)],
            'B': [('D', 3), ('E', 5)],
            'C': [('F', 4)],
            'D': [('G', 2)],
            'E': [('G', 3)],
            'F': [('G', 2)],
            'G': []
        }

        self.h_distance = {
            'A': 7,
            'B': 5,
            'C': 4,
            'D': 2,
            'E': 3,
            'F': 2,
            'G': 0
        }


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


    def a_Star(self, start_node, goal_node):

        open_list = []
        close_list = []

        g = {start_node: 0}

        h = self.h_distance[start_node]
        f = g[start_node] + h

        heapq.heappush(open_list, (f, start_node))

        while len(open_list) != 0:

            f, curr_node = heapq.heappop(open_list)

            if curr_node == goal_node:

                print(
                    f"Goal foud, Closest distance is {f}"
                )

                break

            heapq.heappush(close_list, curr_node)

            for child_node, dist in self.graph[curr_node]:

                new_g = dist + g[curr_node]

                h = self.h_distance[child_node]

                f = new_g + h

                print(g)

                if child_node not in g or new_g < g[child_node]:

                    g[child_node] = new_g

                    h = self.h_distance[child_node]

                    f = new_g + h

                    heapq.heappush(
                        open_list,
                        (f, child_node)
                    )


    def best_first_search(graph, heuristic, start, goal):

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
    print("1. Display Graph")
    print("2. A* Search")
    print("3. Best First Search")
    print("4. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        g.Display()

    elif choice == "2":

        start = input("Enter start node: ").upper()
        goal = input("Enter goal node: ").upper()

        g.a_Star(start, goal)

    elif choice == "3":

        start = input("Enter start node: ").upper()
        goal = input("Enter goal node: ").upper()

        # Your original function is kept unchanged.
        g.best_first_search(
            g.graph,
            g.h_distance,
            start,
            goal
        )

    elif choice == "4":

        print("Program ended.")
        break

    else:

        print("Invalid choice!")
    
