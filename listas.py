import os
import openpyxl
import sys
import sqlite3

path = "sentida"

def main():
    eleccion_archivo = len(os.listdir("."))+2
    for archivo in os.listdir(path):
        print(os.listdir(path).index(archivo), archivo)
    while eleccion_archivo not in range(len(os.listdir(path))+1):
        eleccion_archivo = int(input("Seleccione un archivo para abrir:"))
        if eleccion_archivo not in range(len(os.listdir(path))+1):
            print("Por favor seleccione una de las opciones!")

    archivo_abrir = "".join([path, "\\",os.listdir(path)[eleccion_archivo]])
    print("Ud elegio abrir ", archivo_abrir)
    input()

    try:
        wb_obj = openpyxl.load_workbook(archivo_abrir)

    except:
        print("No se pudo abrir el archivo", sys.exc_info()[0])
        return

    sheet = wb_obj.active
    print(sheet)
    lista = {}
    nro = 0
    grupo = str(nro)
    lista [grupo] = {}
    articulo = ""
    for row in sheet.iter_rows ():

        for cell in row:

            if (nro % 3) == 0:
                grupo = str(nro)
                articulo = cell.value
                try:
                    lista[grupo][articulo] = {}
                except:
                    lista[grupo] = {}
                    lista[grupo][articulo] = {}

            elif (nro % 3) == 1 and cell.value is not None and type(cell.value) != str:
                lista[grupo][articulo]["min"] = cell.value

            elif (nro % 3) == 2 and cell.value is not None and type(cell.value) != str:
                lista[grupo][articulo]["may"] = cell.value
            try:
                lista[grupo][articulo]["margen"] = round (100 * (lista[grupo][articulo]["min"] -
                                                                    lista[grupo][articulo]["may"]) /
                                                             lista[grupo][articulo][
                                                                 "may"], 2)
            except:
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

            print(q, v)

    print(tipos.items())
    input("hasta aca llegue con el analisis del archivo")

    conn = sqlite3.connect('spider.sqlite')
    cur = conn.cursor()
    for k in lista.keys():
        for q, v in lista[k].items():
            try:
                cur.execute('INSERT OR IGNORE INTO ProductosShiri (nombre, precio) VALUES ( ?, ? )', (q, v["min"]))
                print("Actualizando...", q, v["min"])
                conn.commit()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                continue

    for k, v in tipos.items ():
        cur.execute ('INSERT OR IGNORE INTO Categoria (name) VALUES ( ? )', (v,))
        print ("Actualizando...", v)
        conn.commit ()


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

                print(f"Actualizando...{categoria[0]} en {q}")

                conn.commit()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                continue

    cur.close()


if __name__ == '__main__':
    main()
