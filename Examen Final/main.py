import pandas as pd
import random


def generar_conjunto_datos(num_filas, semilla=42):
    random.seed(semilla)
    datos = {
        'Edad': [random.randint(18, 60) for _ in range(num_filas)],
        'Altura': [round(random.uniform(150, 190), 2)
                   for _ in range(num_filas)],
        'Peso': [round(random.uniform(50, 100), 2) for _ in range(num_filas)],
        'ManoDominante': [
            'Diestro' if random.random() < 0.9 else 'Zurdo'
            for _ in range(num_filas)
        ],
        'Genero': random.choices(['Masculino', 'Femenino'], k=num_filas)
    }
    return pd.DataFrame(datos)


seed = 0xB61097
conjunto_datos = generar_conjunto_datos(1000, semilla=seed)
conjunto_datos.to_csv('conjunto_datos' + str(seed) + '.csv', index=False)
