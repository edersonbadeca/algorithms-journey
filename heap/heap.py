def heapify(arr, arr_size, i):
    largest = i # inicializa o maior como raiz
    left = 2 * i + 1 # indice do filho esquerdo
    right = 2 * i + 2 # indice do filho direito
    if left < arr_size and arr[left] > arr[largest]:
        largest = left

    if right < arr_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, arr_size, largest)

def heap_sort(arr):
    arr_size = len(arr)
    for i in range(arr_size // 2 - 1, -1, -1):  # constroi um heap maximo
        heapify(arr, arr_size, i)
    for i in range(arr_size - 1, 0, -1): # extrai elementos um por um por um
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
print(f'Array original: {arr}')
heap_sort(arr)
print(f'Array ordenado: {arr}')
