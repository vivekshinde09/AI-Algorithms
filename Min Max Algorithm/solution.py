class Graph:
    
    def __init__(self):
        self.graph={}
    
    def setGraph(self):
        nodes=int(input("Enter How many nodes present in graph:"))
        for i in range(nodes):
            node=input(f"Enter the node {i+1}:")
            childs=int(input(f"Enter how many childs present of {node}:"))
            
            if childs==0:
                values=[]
                for i in range(2):
                    value=int(input(f"Enter value {i+1}:"))
                    values.append(value)
                self.graph[node]=values
                print()
            else:

                child_list=[]
                for j in range(childs):
                    child=input(f"Enter the child {j+1}:")
                    child_list.append(child)
                self.graph[node]=child_list
                print()
    
    def Display(self):
        for node,child in self.graph.items():
            print(f"{node} : {child}")
    
    def min_max(self,start,depth):
        
        if isinstance(self.graph[start][0],int):
            return max(self.graph[start]) if depth%2==0 else min(self.graph[start])
        
        child_node=[]
        for child in self.graph[start]:
            value=self.min_max(child,depth-1)
            child_node.append(value)
        
        if depth%2==0:
            return max(child_node)
        else:
            return min(child_node)
    
    




def main():
    g=Graph()
    
    while True:
        print("Press 1 to Setting graph.")
        print("Press 2 to Display graph.")
        print("Press 3 for Min Max algoriithm.")
        print("Press 4 to Exit.")
        print()
        choice=int(input("Enter the choice:"))
        print()
        
        match choice:
            
            case 1:
                g.setGraph()
            case 2:
                g.Display()
            case 3:
                node=input("Enter Source node:")
                depth=int(input("Enter the depth of graph:"))
                print(f"The Final result:{g.min_max(node,depth)}")
            case 4:
                print("Exit..")
                break
            case _:
                print("Invalid Choice, Press Again.")

if __name__=="__main__":
    main()


    