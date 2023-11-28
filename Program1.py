import statistics

def statystyki():
    with open('data.txt', 'r') as f:
        data = [int(line.strip()) for line in f]

    suma = sum(data)
    srednia = statistics.mean(data)
    wariancja = statistics.variance(data)
    dominanta = statistics.mode(data)
    min_value = min(data)
    max_value = max(data)

    print(f'Suma: {suma}')
    print(f'Średnia: {srednia}')
    print(f'Wariancja: {wariancja}')
    print(f'Dominanta: {dominanta}')
    print(f'Wartość najmniejsza: {min_value}')
    print(f'Wartość największa: {max_value}')

statystyki()
