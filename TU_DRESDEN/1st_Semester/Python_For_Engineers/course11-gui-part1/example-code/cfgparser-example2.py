import configparser

c = configparser.SafeConfigParser()
c.read('parameters.ini')
print(c.sections())

m1 = c.get('Parameter', 'm1')
m2 = c.get('Parameter', 'm2')

print(m1)
print(m2)
