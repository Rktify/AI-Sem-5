def mazeBoard():
    maze = {
        "0,0": ["0,1"],
        "0,1": ["0,2"],
        "0,2": ["0,3"],
        "0,3": ["0,4", "1,3"],
        "0,4": [ ],
        "1,3": ["1,2", "2,3", "1,4"],
        "1,2": ["1,1"],
        "1,1": ["1,0"],
        "1,0": ["2,0"],
        "2,0": ["3,0"],
        "3,0": ["3,1"],
        "3,1": ["2,1", "3,2"],
        "2,1": [ ],
        "3,2": ["2,2", "4,2"],
        "2,2": [ ],
        "4,2": ["4,1", "4,3"],
        "4,1": ["4,0"],
        "4,0": [ ],
        "4,3": ["4,4", "3,3"],
        "3,3": [ ],
        "4,4": ["3,4"],
        "3,4": ["2,4"],
        "2,4": ["1,4"],
        "1,4": ["1,3"],
        "2,3": [ ]
    }
    return maze


def bfs(maze, start, target):
    visited = set()
    Q = []
    Q.append(start)

    while (Q != []):
        u = Q.pop(0)

        visited.add(u)
        print("Visited: ",u)

        if u == target:
           print("Reached target: ", target)
           break

        for v in maze[u]:
          if (v not in visited) and (v not in Q ):
            Q.append(v)
            print("Added neighbour: ", v)

def main():
    start = "0,0"
    target = "2,1"
    maze = mazeBoard()
    bfs(maze, start, target)

main()
