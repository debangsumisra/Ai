import heapq

class Position:
    def __init__(self, r, c):
        self.r, self.c = r, c
    def __add__(self, other):
        return Position(self.r + other[0], self.c + other[1])
    def __eq__(self, other):
        return self.r == other.r and self.c == other.c
    def __lt__(self, other):  # needed for heapq
        return (self.r, self.c) < (other.r, other.c)
    def __hash__(self):
        return hash((self.r, self.c))

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows, self.cols = len(maze), len(maze[0])
        self.start = self._find('A')
        self.end = self._find('B')

    def _find(self, symbol):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == symbol:
                    return Position(i, j)

    def _neighbors(self, pos):
        steps = [(-1,0),(1,0),(0,-1),(0,1)]
        for dr, dc in steps:
            nr, nc = pos.r+dr, pos.c+dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.maze[nr][nc] != 1:
                yield Position(nr, nc)

    def _h(self, a, b):
        return abs(a.r - b.r) + abs(a.c - b.c)  # Manhattan

    def solve(self):
        heap = [(0,0,self.start,[self.start])]
        best = {self.start:0}
        while heap:
            f,g,pos,path = heapq.heappop(heap)
            if pos == self.end:
                return path
            for nb in self._neighbors(pos):
                ng = g+1
                if nb not in best or ng < best[nb]:
                    best[nb] = ng
                    heapq.heappush(heap,(ng+self._h(nb,self.end),ng,nb,path+[nb]))
        return None

    def show(self, path=None):
        path_set = {(p.r,p.c) for p in path} if path else set()
        print("\n".join(
            "".join(
                "A" if (i,j)==(self.start.r,self.start.c) else
                "B" if (i,j)==(self.end.r,self.end.c) else
                "." if (i,j) in path_set else
                "#" if self.maze[i][j]==1 else " "
                for j in range(self.cols)
            ) for i in range(self.rows)
        ))

def main():
    maze = [
        ['A',0,1,0,0,0,1,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0,0],
        [1,0,0,0,1,0,0,0,1,1,1,0],
        [0,1,1,0,0,1,1,0,0,0,1,0],
        [0,0,0,0,1,0,1,1,1,0,0,0],
        [1,1,1,0,1,0,0,0,1,1,1,0],
        [0,0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,0,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0,0,0],
        [1,1,1,1,1,1,0,1,0,1,1,0],
        [0,0,0,0,0,0,0,1,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,'B'],
    ]
    solver = MazeSolver(maze)
    print("\nMaze:")
    solver.show()
    path = solver.solve()
    print("\nPath:")
    solver.show(path)

if __name__ == "__main__":
    main()
