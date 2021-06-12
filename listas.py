import os
import openpyxl
import sys
import sqlite3

path = "sentida"


def limpio_pantalla():
    os.system("cls")


def muestro_titulo(mensaje):
    print("\t", "*" * len(mensaje))
    print("\t", mensaje)
    print("\t", "*" * len(mensaje))


def elijo_archivo():
    mensaje = ""
    eleccion_archivo = len(os.listdir(path))+1
    while eleccion_archivo not in range(len(os.listdir(path))):
        limpio_pantalla()
        muestro_titulo("Archivos de Listas de Precio")
        print("\t"+"*"*(len(os.listdir(path)[0])+3))
        for archivo in os.listdir(path):
            print("\t", os.listdir(path).index(archivo), archivo)
        print(mensaje)
        try:
            eleccion_archivo = int(input("\n\tSeleccione un archivo para abrir:"))
        except:
            mensaje = "\n\tERROR!!!..UD. NO SELECCIONO UNA OPCION VALIDA!...INTENTE DE NUEVO!"
            continue
        if eleccion_archivo not in range(len(os.listdir(path))):
            mensaje = "\n\tERROR!!!..UD. NO SELECCIONO UNA OPCION VALIDA!...INTENTE DE NUEVO!"
    return "".join([path, "\\", os.listdir(path)[eleccion_archivo]])


def proceso_excel(archivo_abrir):
    limpio_pantalla()
    muestro_titulo(archivo_abrir)
    try:
        wb_obj = openpyxl.load_workbook(archivo_abrir)

    except:
        print("No se pudo abrir el archivo", sys.exc_info()[0])
        return

    sheet = wb_obj.active
    print(sheet, end="\r")
    lista = {}
    nro = 0
    grupo = str(nro)
    lista[grupo] = {}
    articulo = ""
    for row in sheet.iter_rows():

        for cell in row:

            if (nro % 3) == 0:
                grupo = str(nro)
                articulo = cell.value
                try:
                    lista[grupo][articulo] = {}
                except:
                    print("error: ", sys.exc_info()[0], end="\r")
                    lista[grupo] = {}
                    lista[grupo][articulo] = {}

            elif (nro % 3) == 1 and cell.value is not None and type(cell.value) != str:
                lista[grupo][articulo]["min"] = cell.value

            elif (nro % 3) == 2 and cell.value is not None and type(cell.value) != str:
                lista[grupo][articulo]["may"] = cell.value
            try:
                lista[grupo][articulo]["margen"] = round(100 * (lista[grupo][articulo]["min"] -
                                                                lista[grupo][articulo]["may"]) /
                                                         lista[grupo][articulo][
                                                             "may"], 2)
            except:
                print("error: ", sys.exc_info()[0], end="\r")
                next

            if nro < 9:
                nro += 1
            else:
                nro = 0
    tipos = {}
    n_tipo = 0
    tipo = ""

    for k in lista.keys():
        for q, v in lista[k].items():
            if v == {}:
                tipo = q
                n_tipo += 1
                continue

            tipos[n_tipo] = tipo
            v["tipo"] = n_tipo

            print(q, v, end="\r")

    print(tipos.items())
    input("\tSe termino de procesar archivo excel, continua?")
    return [tipos, lista]


def proceso_sql(tipos, lista):
    limpio_pantalla()
    muestro_titulo("Actualizando base de datos")

    conn = sqlite3.connect('spider.sqlite')
    cur = conn.cursor()
    for k in lista.keys():
        for q, v in lista[k].items():
            try:
                cur.execute('INSERT OR IGNORE INTO ProductosShiri (nombre, precio) VALUES ( ?, ? )', (q, v["min"]))
                print("Actualizando Productos y Precios...", q, v["min"], end="\r")
                conn.commit()
            except:
                print("Unexpected error:", sys.exc_info()[0], end="\r")
                continue

    for k, v in tipos.items():
        cur.execute('INSERT OR IGNORE INTO Categoria (name) VALUES ( ? )', (v,))
        print("Actualizando Categorias...", v, end="\r")
        conn.commit()

    for k in lista.keys():
        for q, v in lista[k].items():

            try:
                desc_categ = tipos[v["tipo"]]

                cur.execute("SELECT id, name FROM Categoria where name = ?", (desc_categ, ))
                categoria = cur.fetchone()

                cur.execute("SELECT nombre, categoria_id FROM ProductosShiri where nombre = ?", (q, ))

                cur.execute('''UPDATE ProductosShiri 
                            set categoria_id = ? 
                            where nombre = ?''', (categoria[0], q))

                print(f"Actualizando...{categoria[0]} en {q}", end="\r")

                conn.commit()
            except:
                print("Unexpected error:", sys.exc_info()[0], end="\r")
                continue

    cur.close()


def main():
    archivo_abrir = elijo_archivo()
    print("\n\tUd elegio abrir: ", archivo_abrir)
    input("\tContinua?")
    tipos, lista = proceso_excel(archivo_abrir)
    proceso_sql(tipos, lista)


if __name__ == '__main__':
    main()
