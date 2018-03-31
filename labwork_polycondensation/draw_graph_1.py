from matplotlib import pyplot as plt
import numpy as np

def draw_graph():
	# открыть файл со всеми данными и извлечь из них время и 1/1-p
	time = []
	rate = []
	with open('final_data.txt') as file:
		lines = file.read().split("\n")
		for line in lines[:-1]:
			time.append(float(line.split(" ")[0]))
			rate.append(float(line.split(" ")[-1]))

	# numpy может расчитать нам линейное приближение
	# сначала получаем тангенс угла наклона (slope) и касательную к ординате при x=0
	polyfit = np.polyfit(time, rate, 1)

	# теперь делаем линию приближения
	polyfit_line = np.array(time) * polyfit[0] + polyfit[1]

	# наводим немного красоты
	fig = plt.figure()
	fig.suptitle('Зависимость 1/(1-p) от времени', fontsize=14, fontweight='bold')
	ax = fig.add_subplot(111)
	ax.set_xlabel('Время от начала реакции, сек')
	ax.set_ylabel('1/(1-p)')
	ax.text(2000, -0.015, u'tg(α): %.8f' % (polyfit[0]), style="italic")

	# по оси абсцисс – время, по оси ординат – 1/1-p, поэтому:
	plt.scatter(time, rate, color="black")

	# добавляем прямую линию
	plt.plot(time, polyfit_line, color="black")

	# plt.show()
	fig.savefig('time_vs_rate_of_reaction.png', dpi=800)
	print("Угол наклона прямой: %.8f" % (polyfit[0]))