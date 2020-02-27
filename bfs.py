import queue

def create_maze():
    maze = []
    maze.append(["#","#","#","#","#","o","#"])
    maze.append(["#"," "," "," ","#"," ","#"])
    maze.append(["#"," ","#"," "," "," ","#"])
    maze.append(["#"," ","#"," "," ","#","#"])
    maze.append(["#"," ","#","#","#","#","#"])
    maze.append(["#"," "," "," "," "," ","#"])
    maze.append(["#","#","#","#","#","x","#"])
    return maze

def print_maze(maze,path=""):
    for x,pos in enumerate(maze[0]):
        if pos == "o":
            start = x
    
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1;
        elif move == "R":
            i += 1;
        elif move == "U":
            j -= 1;
        elif move == "D":
            j += 1;
        pos.add((j,i))

    for j,row in enumerate(maze):
        for i,col in enumerate(row):
            if (j,i) in pos:
                print("+ ",end="")
            else:
                print(col+" ",end="")
        print()

def valid(maze,moves):
    for x,pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1;
        elif move == "R":
            i += 1;
        elif move == "U":
            j -= 1;
        elif move == "D":
            j += 1;
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
    return True

def findEnd(maze,moves):
    for x,pos in enumerate(maze[0]):
        if pos == "o":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1;
        elif move == "R":
            i += 1;
        elif move == "U":
            j -= 1;
        elif move == "D":
            j += 1;
        if maze[j][i] == "x":
            print("found : "+moves)
            print_maze(maze,moves)
            return True
    return False


nums = queue.Queue()
nums.put("")
add = ""
maze = create_maze()

while not findEnd(maze,add):
    add = nums.get()
    for j in ["L","R","U","D"]:
        put = add +j
        if valid(maze,put):
            nums.put(put)