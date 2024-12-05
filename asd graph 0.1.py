from collections import deque
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    adjacency_matrix = [list(map(int, line.split())) for line in file]

labels = [0] * n
queue = deque()
current_label = 1

for i in range(n):
    if labels[i] == 0:
        queue.append(i)
        labels[i] = current_label
        current_label += 1
        while queue:
            vertex = queue.popleft()
            for neighbor in range(n):
                if adjacency_matrix[vertex][neighbor] == 1 and labels[neighbor] == 0:
                    queue.append(neighbor)
                    labels[neighbor] = current_label
                    current_label += 1

with open('output.txt', 'w') as output_file:
    output_file.write(' '.join(map(str, labels)) + '\n')
