import configparser

c = configparser.SafeConfigParser()
c.add_section('Parameter')
c.set('Parameter', 'm1', '1.5')
c.set('Parameter', 'm2', '5')

with open('parameters.ini', 'w') as fid:
    c.write(fid)
