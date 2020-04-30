from die import Die
import pygal

die = Die()

results = []
for roll_num in range(1000):
    result1 = die.roll()
    result2 = die.roll()
    results.append(result1+result2)

frequencies = []
for value in range(2,die.num_sides*2+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequencise of result"

hist.add('D6',frequencies)
hist.render_to_file('die_visults.svg')
