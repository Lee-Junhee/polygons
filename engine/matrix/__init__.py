from polygon import Polygon

class Matrix:
    view = None
    content = None
    edges = None
    polygons = None

    def multiply(m1, m2):
        #matrix multiplication code here
        for i in range(len(m2[0])):
            col = [0, 0, 0, 0]
            for j in range(4):
                for k in range(4):
                    col[k] += m1.content[k][j] * m2[j][i]
            for j in range(4):
                m2[j][i] = col[j]

    def __init__(self, view=(0, 0, 1)):
        self.view = view
        self.edges = [[], [], [], []]
        self.polygons = [[], [], [], []]
        self.ident()

    def addPoint(matrix, point):
        for i in range(3):
            matrix[i].append(point[i])
        matrix[3].append(1)

    def addEdge(self, p1, p2):
        Matrix.addPoint(self.edges, p1)
        Matrix.addPoint(self.edges, p2)

    def addPolygon(self, p1, p2, p3):
        Matrix.addPoint(self.polygons, p1)
        Matrix.addPoint(self.polygons, p2)
        Matrix.addPoint(self.polygons, p3)

    def ident(self):
        self.content = [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
                ]

    def print(self):
        print("Edges: ")
        for i in range(4):
            for j in self.edges[i]:
                print("%.2f" % j, end = "\t", flush=True)
            print("")
        print("Polygons: ")
        for i in range(4):
            for j in self.polygons[i]:
                print("%.2f" % j, end = "\t", flush=True)
            print("")

    def addEdges(self, lines):
        matrix = self.edges
        for i in range(len(matrix[3]) // 2):
            lines.append([int(matrix[0][2 * i]), int(matrix[1][2 * i]), 
                    int(matrix[0][2 * i + 1]), int(matrix[1][2 * i + 1])])

    def addPolygons(self, lines):
        matrix = self.polygons
        v = self.view
        for i in [3 * j for j in range(len(matrix[3]) // 3)]:
            n = Polygon.normal([matrix[x][i] for x in range(3)], [matrix[x][i + 1] for x in range(3)], [matrix[x][i + 2] for x in range(3)])
            if n[0] * v[0] + n[1] * v[1] + n[2] * v[2]  > 0:
                lines.append([matrix[x][i] for x in range(2)] + [matrix[x][i + 1] for x in range(2)])
                lines.append([matrix[x][i + 1] for x in range(2)] + [matrix[x][i + 2] for x in range(2)])
                lines.append([matrix[x][i + 2] for x in range(2)] + [matrix[x][i] for x in range(2)])
        self.matrix = Matrix()

    def lines(self):
        l = []
        self.addEdges(l)
        self.addPolygons(l)
        print(self.polygons)
        return l
