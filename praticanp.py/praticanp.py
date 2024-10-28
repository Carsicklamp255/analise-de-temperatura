import numpy as np
import matplotlib.pyplot as plt

temperatura = np.random.randint(15, 35, size = 30)

print(temperatura)

# calcule a temperatura media do mês
print(f'a media é: {np.min(temperatura):.2f} C.')
print(f'a media é: {np.max(temperatura):.2f} C.')

# calcule a mediana das temperaturas
print(f'a mediana é: {np.median(temperatura):.2f} ')

'''manipulação de dados
apresentar uma lista contendo apenas as ocorrências de temperatura iguais ou superiores a 30 C.
'''

print(temperatura[temperatura >= 30])

'''
crie uma nova lista das temperaturas na escala farenheit
'''
F = 1,8 * temperatura + 32
print(F)

# gerador de grafico de temperatura grafico
plt.plot(temperatura, marker = 'o')
plt.title('temperaturas diárias ao longo do m')
plt.xlabel('dia')
plt.ylabel('temperatura (c)')
plt.show()

semanas = np.array_split(temperatura, 4)
print(semanas)

medias_semanais = [np.mean(semanas) for semana in semanas]
print(medias_semanais)

plt.bar(range(1,5), medias_semanais)
plt.title('medias das temperaturas')
plt.xlabel('semana')
plt.ylabel('temperatura média (c)')
plt.xticks(range(1,5,), ['semana 1', 'semana 2', 'semana 3', 'semana 4'])
plt.show()
