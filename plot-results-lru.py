import matplotlib.pyplot as plt
import numpy as np

# Dados formatados
configurations = {
    '4 KB': [
        {'Memória': 128, 'Page faults': 542203, 'Páginas escritas': 68824},
        {'Memória': 256, 'Page faults': 488195, 'Páginas escritas': 59878},
        {'Memória': 512, 'Page faults': 445628, 'Páginas escritas': 51781},
        {'Memória': 1024, 'Page faults': 406130, 'Páginas escritas': 45507}
    ],
    '128 KB': [
        {'Memória': 2048, 'Page faults': 254674, 'Páginas escritas': 32803},
        {'Memória': 4096, 'Page faults': 212959, 'Páginas escritas': 26420},
        {'Memória': 8192, 'Page faults': 181448, 'Páginas escritas': 22181},
        {'Memória': 16384, 'Page faults': 152367, 'Páginas escritas': 18250}
    ],
    '256 KB': [
        {'Memória': 16384, 'Page faults': 144269, 'Páginas escritas': 18733}
    ],
    '512 KB': [
        {'Memória': 16384, 'Page faults': 147139, 'Páginas escritas': 20844}
    ]
}

# Preparação dos dados para o gráfico de barras
configs = []
mems = []
page_faults = []
paginas_escritas = []

for config, values in configurations.items():
    for value in values:
        configs.append(config)
        mems.append(value['Memória'])
        page_faults.append(value['Page faults'])
        paginas_escritas.append(value['Páginas escritas'])

# Convertendo para numpy arrays para facilitar a manipulação
configs = np.array(configs)
mems = np.array(mems)
page_faults = np.array(page_faults)
paginas_escritas = np.array(paginas_escritas)

# Definindo a largura das barras
bar_width = 0.35

# Índices das barras
indices = np.arange(len(mems))

# Gráfico de Page Faults
fig, ax = plt.subplots(figsize=(14, 7))
rects1 = ax.bar(indices - bar_width/2, page_faults, bar_width, label='Page Faults')

# Gráfico de Páginas Escritas
rects2 = ax.bar(indices + bar_width/2, paginas_escritas, bar_width, label='Páginas Escritas')

# Adicionando os rótulos, título e a legenda
ax.set_xlabel('Configuração de Páginas e Memória (KB)')
ax.set_ylabel('Quantidade')
ax.set_title('Comparação de Page Faults e Páginas Escritas')
ax.set_xticks(indices)
ax.set_xticklabels([f'{config}\n{mem} KB' for config, mem in zip(configs, mems)])
ax.legend()

# Adicionando uma grade
ax.grid(True, axis='y')

# Exibindo o gráfico
plt.tight_layout()
plt.show()
