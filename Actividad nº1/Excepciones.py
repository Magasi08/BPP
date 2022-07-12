class Otraexcepcion(Exception):
    pass


try:
    raise Otraexcepcion({'p1': 'valor param1', 'p1': 'valor param2'})
except Otraexcepcion as ex:
    info = ex.args[0]
    print(info)
    print(info['p1'])
    print(info['p2'])