import math
data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for i in data:
    if not math.isnan(i):
        filtered_data.append(i)

print(filtered_data)
