import numpy as np
import matplotlib.pyplot as plt
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

A = 1.34941
x_start = -10
x_end = 10
step = 0.1
x_values = np.arange(x_start, x_end + step, step)
y_values = -0.0001 * (np.abs(np.sin(x_values)*np.sin(A)*np.exp(np.abs(100 - np.sqrt(x_values**2 + A**2)/np.pi))) + 1)**0.1

data = Element('data')
xdata = SubElement(data, 'xdata')
ydata = SubElement(data, 'ydata')

for x, y in zip(x_values, y_values):
    x_elem = SubElement(xdata, 'x')
    x_elem.text = f"{x:.1f}".replace(".0", "")
    y_elem = SubElement(ydata, 'y')
    y_elem.text = f"{y:.5f}".rstrip("0").rstrip(".")

xml_str = minidom.parseString(tostring(data)).toprettyxml(indent="")
xml_str = xml_str.replace('<?xml version="1.0" ?>', '<?xml version="1.1" encoding="UTF-8"?>')

with open('result.xml', 'w', encoding='utf-8') as f:
    f.write(xml_str)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'b-', linewidth=2, label=f'y = -0.0001*(|sin(x)sin({A})exp(|100-√(x²+{A}²)/π|)| +1)^0.1')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

print("Файл result.xml создан")