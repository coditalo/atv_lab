def insertion_sort(vetor):
    count = 0
    n = len(vetor)
    
    for i in range(1, n):
        x = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > x:
            vetor[j + 1] = vetor[j]
            j -= 1
            count += 1
        vetor[j + 1] = x

    return count


import random


def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]
def main():
    vetor = generate_random_array(10)
    print("Array de entrada:", vetor)
    result = insertion_sort(vetor)
    print("Deslocamentos realizados:", result)

if __name__ == '__main__':
    main()