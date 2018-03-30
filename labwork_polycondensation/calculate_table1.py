from draw_graph_1 import draw_graph

# initial – массы самих колб
# experimental – все данные в формате || время (сек) | масса колбы с пробой | объем на титрование ||

# Для расчета b
# b = V * T
# нужен титр

normality = float(input("Какова нормальность раствора, использованного для титрования? > "))
molar_mass = float(input("Какова молекулярная масса этого раствора? > "))
titre = round((normality * molar_mass)/1000, 5)

# извлекаем исходные массы колб
init_masses = []
with open("initial.txt") as file:
	init_masses = [float(x) for x in file.read().split("\n")]

# извлекаем экспериментальные данные
experimental = []
with open('experimental.txt') as file:
	experimental = file.read().split("\n")

# из них извлекаем объемы, пошедшие на титрование, и массы колб со взятыми пробами
volumes = []
after_masses = []
for data_line in experimental:
	volumes.append(float(data_line.split(" ")[2]))
	after_masses.append(float(data_line.split(" ")[1]))

# а потом оставляем в одном массиве только массы взятых проб
final_masses = []
for init_mass, after_mass in zip(init_masses, after_masses):
	final_masses.append(round(after_mass - init_mass, 5))

# считаем Ge
neutral_equivalents = []
for mass, volume in zip(final_masses, volumes):
	b = volume * titre
	neutral_equivalents.append(round(mass/b, 5))

# считаем последний столбик
last_column = []
# необходимые константы
water = 18
catalyst = 172
repeating_part = 258
a = 0.0044
for item in neutral_equivalents:
	calculation = (item - water)/(repeating_part + (2 * catalyst * a) - (2 * a * item))
	last_column.append(round(calculation, 5))

# дописываем Ge к имеющимся данным
with_ge = []
for Ge, rest_data in zip(neutral_equivalents, experimental):
	with_ge.append(rest_data + " " + str(Ge))

# дописываем последний столбик
final_data = []
for last, rest in zip(last_column, with_ge):
	final_data.append(rest + " " + str(last))

# записываем это всё в красивый файл
filename = "final_data.txt"

with open(filename, 'a') as file:
	for item in final_data:
		file.write(item + "\n")

# построить первый график по этим данным
draw_graph()