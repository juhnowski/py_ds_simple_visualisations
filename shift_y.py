from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013,1014]

plt.bar([2012.6, 2013.6],mentions,0.8)
plt.xticks(years)
plt.ylabel("Число")

plt.ticklabel_format(useOffset=False)
# Дезориентирующая ось
#plt.axis([2012.5, 2014.5, 499, 506])
#plt.title("Огромный прирост")
#plt.show()

plt.axis([2012.5, 2014.5, 100, 550])
plt.title("Больше не такой огромный")
plt.show()