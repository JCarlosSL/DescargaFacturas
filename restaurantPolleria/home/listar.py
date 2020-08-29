from os import getcwd,scandir
from os.path import abspath
from .lecture import lectura

path = 'home/'+'static/facturas'
pdf = 'pdf'
def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
    #obtiene la ruta principal
    #return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

def ListarFacturas():

    facturas = []
    direcciones = ls(path)
    for i in direcciones:
        direccion = i.split('.')
        tipo = direccion[1]
        name = direccion[0]
        if tipo!=pdf:
            info = name.split('-')
            (fecha,ruc) = lectura(path+'/'+name,name)
            info.append(fecha)
            info.append(ruc)
            facturas.append(info)
    return facturas

#print(ListarFacturas())
