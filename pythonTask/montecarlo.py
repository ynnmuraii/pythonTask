import random
from concurrent.futures import ProcessPoolExecutor

def calc_pi(n):
    inside = 0
    for i in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return (inside / n) * 4

if __name__ == "__main__":
    n = int(input("Количество точек для генерации: "))

    with ProcessPoolExecutor() as executor:
        pi = executor.submit(calc_pi, n)
        print(f"Оценка числа Pi: {pi.result()}")