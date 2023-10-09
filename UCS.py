from collections import defaultdict
from queue import PriorityQueue


class Node:
    def __init__(self, name, path, cost=0):
        self.name = name  # 노드 이름
        self.path = path  # 시작 노드로 부터 경로
        self.cost = cost  # 시작 노드로 부터의 가중치 합

    def expand(self, graph):
        # 그래프에서 현재 노드의 자식 노드로 생성할 수 있는 노드를 리스트로 반환
        return [Node(i, [], graph.get(self.name).get(i)) for i in graph.get(self.name).keys()]

    def __lt__(self, other):
        return self.cost < other.cost  # 비교 연산자 재정의

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def generateGraph(edges):
    graph = defaultdict(dict)
    for u, v, dist in edges:
        graph[u][v] = dist
    return graph


def UCS(graph, src, dest):
    queue = PriorityQueue()  # 우선 순위 큐 생성
    queue.put(Node(src, [], 0))
    visited = set()

    while queue:
        current = queue.get()

        if current not in visited:  # 이미 방문한 노드가 아니면
            visited.add(current)  # 현재 노드를 방문 했다고 체크, set을 이용하여 O(1) 시간 복잡도를 보장
            print(f'방문: {current.name}')

            for state in current.expand(graph):  # 현재 노드의 자식 노드 생성
                if state not in visited:
                    state.cost += current.cost  # 방문된 가중치 합을 자식 노드에 넣는다
                    state.path = current.path + [current.name]  # 자식 노드의 경로에 부모 노드의 경로와 부모 노드를 추가
                    queue.put(state)  # 큐에 추가

        if current.name == dest:  # 현재 노드가 목표 노드면 종료
            current.path.append(current.name)  # 도착 목표 노드에 도달하면 path에 목표 노드를 추가한다
            print(f'Shortest distance is {current.cost}')  # 최단 거리 비용을 출력한다
            print(f'And Search path is {current.path}')  # 최단 거리 경로를 출력한다
            return


if __name__ == "__main__":
    weighted_edges = [['a', 'b', 5], ['b', 'a', 5],
                      ['a', 'c', 4], ['c', 'a', 4],
                      ['b', 'c', 5], ['c', 'b', 5],
                      ['b', 'e', 6], ['e', 'b', 6],
                      ['c', 'e', 8], ['e', 'c', 8],
                      ['b', 'd', 7], ['d', 'b', 7],
                      ['c', 'd', 3], ['d', 'c', 3],
                      ['e', 'g', 3], ['g', 'e', 3],
                      ['d', 'f', 3], ['f', 'd', 3],
                      ['f', 'g', 2], ['g', 'f', 2]]

    graph = generateGraph(weighted_edges)
    UCS(graph, 'a', 'g')