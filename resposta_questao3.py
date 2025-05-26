import bisect
import random

def activityNotifications(gastosCliente, d):
    notificacoes = 0
    lista = sorted(gastosCliente[:d])
    
    for i in range(d, len(gastosCliente)):
        # Calcula a mediana
        if d % 2 == 1:
            m = lista[d // 2]
        else:
            m = (lista[d // 2 - 1] + lista[d // 2]) / 2

        if gastosCliente[i] >= 2 * m:
            notificacoes += 1
        
        old_value = gastosCliente[i - d]
        index = bisect.bisect_left(lista, old_value)
        lista.pop(index)

        
        new_value = gastosCliente[i]
        bisect.insort(lista, new_value)

    return notificacoes

def gerar_dados(n, max_val=200):
    return [random.randint(0, max_val) for _ in range(n)]

def main():
    teste = True
    if teste:
        n, d = 9, 5
        gastos = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    else:
        n, d = 10, 5
        gastos = gerar_dados(n)

    print(f"n = {n}, d = {d}")
    print("Gastos:", gastos)
    resultado = activityNotifications(gastos, d)
    print("Notificações:", resultado)

if __name__ == '__main__':
    main()