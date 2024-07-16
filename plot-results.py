import matplotlib.pyplot as plt
import pandas as pd

# Dados de desempenho formatados
data = {
    "Memória (KB)": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 16384, 16384],
    "Page faults (FIFO)": [562648, 505272, 459999, 417686, 274889, 227910, 193555, 163367, 156537, 163585],
    "Páginas escritas (FIFO)": [74403, 64855, 56419, 49341, 42201, 32739, 26560, 21490, 23114, 26965],
    "Page faults (LRU)": [542203, 488195, 445628, 406130, 254674, 212959, 181448, 152367, 144269, 147139],
    "Páginas escritas (LRU)": [68824, 59878, 51781, 45507, 32803, 26420, 22181, 18250, 18733, 20844],
    "Page faults (Random)": [573212, 488195, 474387, 428456, 292379, 242473, 204191, 170886, 166901, 177748],
    "Páginas escritas (Random)": [75649, 59878, 59459, 51989, 43308, 34281, 27663, 22302, 23942, 28209],
    "Page faults (2A)": [552479, 493908, 450676, 410182, 260326, 216357, 184805, 155407, 147307, 151015],
    "Páginas escritas (2A)": [71058, 61588, 53549, 47314, 35174, 27579, 23221, 19086, 19674, 21975],
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Função para plotar gráficos de desempenho
def plot_performance(df):
    memory_sizes = df["Memória (KB)"].to_numpy()

    # Gráfico de Page Faults
    plt.figure(figsize=(12, 6))
    plt.plot(memory_sizes, df["Page faults (FIFO)"].to_numpy(), label="FIFO", marker='o')
    plt.plot(memory_sizes, df["Page faults (LRU)"].to_numpy(), label="LRU", marker='o')
    plt.plot(memory_sizes, df["Page faults (Random)"].to_numpy(), label="Random", marker='o')
    plt.plot(memory_sizes, df["Page faults (2A)"].to_numpy(), label="2A", marker='o')
    plt.xlabel("Memória (KB)")
    plt.ylabel("Page Faults")
    plt.title("Comparação de Page Faults entre Algoritmos")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

    # Gráfico de Páginas Escritas
    plt.figure(figsize=(12, 6))
    plt.plot(memory_sizes, df["Páginas escritas (FIFO)"].to_numpy(), label="FIFO", marker='o')
    plt.plot(memory_sizes, df["Páginas escritas (LRU)"].to_numpy(), label="LRU", marker='o')
    plt.plot(memory_sizes, df["Páginas escritas (Random)"].to_numpy(), label="Random", marker='o')
    plt.plot(memory_sizes, df["Páginas escritas (2A)"].to_numpy(), label="2A", marker='o')
    plt.xlabel("Memória (KB)")
    plt.ylabel("Páginas Escritas")
    plt.title("Comparação de Páginas Escritas entre Algoritmos")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

# Chamar a função para plotar os gráficos
plot_performance(df)
