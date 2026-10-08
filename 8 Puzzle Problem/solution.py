import heapq


class EightPuzzle:

    def __init__(self):

        self.puzzle=()
        # self.goal=()
        
        # self.puzzle = (
        #     (1, 2, 3),
        #     (0, 4, 6),
        #     (7, 5, 8)
        # )

        
        self.goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 0)
        )

    def getInput(self):

        puzzle = []

        print("Type the numbers in order\n")
        print("For blank space type 0")

        for i in range(3):

            row = []

            for j in range(3):
                value = int(input(f"Element[{i}][{j}]: "))
                row.append(value)

            puzzle.append(row)

        # Convert list of lists -> tuple of tuples
        self.puzzle = tuple(tuple(row) for row in puzzle)
        
    def Display(self):

        for i in range(3):
            for j in range(3):
                print(self.puzzle[i][j], end=" ")
            print()


    def right_move(self, state):

        for x in range(3):
            for y in range(3):
                if state[x][y] == 0:
                    i, j = x, y
                    break
            else:
                continue
            break

        
        new_state = [list(row) for row in state]

        if j == 2:
            return None

        temp = new_state[i][j]
        new_state[i][j] = new_state[i][j + 1]
        new_state[i][j + 1] = temp

        
        return tuple(tuple(row) for row in new_state)


    def left_move(self, state):

        for x in range(3):
            for y in range(3):
                if state[x][y] == 0:
                    i, j = x, y
                    break
            else:
                continue
            break

        
        new_state = [list(row) for row in state]

        if j == 0:
            return None

        temp = new_state[i][j]
        new_state[i][j] = new_state[i][j - 1]
        new_state[i][j - 1] = temp

        
        return tuple(tuple(row) for row in new_state)


    def up_move(self, state):

        for x in range(3):
            for y in range(3):
                if state[x][y] == 0:
                    i, j = x, y
                    break
            else:
                continue
            break

        if i == 0:
            return None

         
        new_state = [list(row) for row in state]

        temp = new_state[i][j]
        new_state[i][j] = new_state[i - 1][j]
        new_state[i - 1][j] = temp

         
        return tuple(tuple(row) for row in new_state)


    def down_move(self, state):

        for x in range(3):
            for y in range(3):
                if state[x][y] == 0:
                    i, j = x, y
                    break
            else:
                continue
            break

        if i == 2:
            return None

         
        new_state = [list(row) for row in state]

        temp = new_state[i][j]
        new_state[i][j] = new_state[i + 1][j]
        new_state[i + 1][j] = temp

         
        return tuple(tuple(row) for row in new_state)


    def h_value(self, state):

        h = 0

        for i in range(3):
            for j in range(3):

                if state[i][j] != 0:

                    if self.goal[i][j] != state[i][j]:
                        h += 1

        return h


    def eight_puzzle(self, puzzle):

        open_list = []
        close_list = []
        parent = {}
        path = []
        visited = set()

        g = 0

        h = self.h_value(puzzle)
        f = g + h

        moves = [
            self.right_move,
            self.left_move,
            self.up_move,
            self.down_move
        ]

        heapq.heappush(open_list, (f, g, puzzle))

         
        visited.add(puzzle)

        while len(open_list) != 0:

            f, g, curr_state = heapq.heappop(open_list)

            close_list.append(curr_state)

            if curr_state == self.goal:

                current = self.goal

                while current != puzzle:

                    path.append(current)

                    current = parent[current]

                path.append(puzzle)

                path.reverse()

                print("Goal node is found!")


                for state in path:

                    print()

                    for row in state:
                        print(row)

                print("\nTotal moves:", len(path) - 1)

                return path


            for move in moves:

                new_state = move(curr_state)

                if new_state is not None and new_state not in visited:

                    h = self.h_value(new_state)

                    new_g = g + 1

                    f = new_g + h

                    parent[new_state] = curr_state

                    heapq.heappush(
                        open_list,
                        (f, new_g, new_state)
                    )

                    visited.add(new_state)


 
def main():
    Ep=EightPuzzle()
    
    while True:
        
        print("1. For Giving puzzle info")
        print("2. Display")
        print("3. For 8 puzzle solution")
        print("4. For Exit")
        choice=int(input("Enter Choice:"))
        
        match choice:
            
            case 1:
                Ep.getInput()
                print('\n')
            case 2:
                Ep.Display()
                print('\n')
            case 3:
                Ep.eight_puzzle(Ep.puzzle)
                print('\n')
            case 4:
                print("Exit.")
                break
            case _:
                print("Enter valid choice. Press again.")
                
if __name__=="__main__":
    main()