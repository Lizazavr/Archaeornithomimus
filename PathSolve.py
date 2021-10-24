#подключаем пакеты qboard и numpy
from qboard import Solver
import numpy as np
#загружаем граф смежности
file = np.load('adjacency.npy')

x, y, a, b = 25, 25, 0.01, 1
array = [[0 for i in  range(x)]for j in range(y)]
#массив, по которому будет вычсляться вершина
array2 = ['A','B','C','D','E']

#цикл, проходящий по строкам и столбцам
for i in range(0,x):
	for j in range(0, y):
		#если у нас получается путь из вершины в саму себя, то записываем 0 или штраф
		if (array2[int(i/5)] == array2[int(j/5)]):
			if j == i:
				array[i][j] = 0
				c = 5
				while(j + c < y):
					array[i][j+c] = a 
					array[j+c][i] = a
					c += 5
			else:
				array[i][j] = a
		#если путь удовлетворяет всем условиям - записываем вес из смежной матрицы
		elif (i < j) and (array[i][j] != a):
			array[j][i] = b * file[int(i/5)][int(j/5)]
			array[i][j] = b * file[int(i/5)][int(j/5)]

#определяем параметры
PARAMS = {
"remote_addr": "https://remote.qboard.tech", 
"access_key": "4b6403a0-c30b-4515-b670-ded955eb05e3"
}

#иницилизируем Solver
s = Solver(mode="remote:gurobi", params=PARAMS) 

#задаем матрицу QUBO
#np.save("q.npy",array)
#Q = np.load('q.npy')
Q = array
for i in range(0,x):
	print(Q[i])
#получаем результат
spins, energy = s.solve_qubo(Q, timeout = 30)

#выводим результат
print(spins)

