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


def genero_menu(lista, titulo, mensaje =""):
    lista.append("Salir")
    seleccion = len(lista)+1
    while seleccion not in range(len(lista)):
        limpio_pantalla()
        muestro_titulo(titulo)
        for cada_opcion in lista:
            print("\t", lista.index(cada_opcion), cada_opcion)
        print(mensaje)

        try:
            seleccion = int(input("\n\tSeleccione una opcion:"))

        except KeyboardInterrupt:
            print('')
            print('Program interrupted by user...')
            break

        except:
            mensaje = "\n\tERROR!!!..UD. NO SELECCIONO UNA OPCION VALIDA!...INTENTE DE NUEVO!"
            continue
        if seleccion not in range(len(lista)):
            mensaje = "\n\tERROR!!!..UD. NO SELECCIONO UNA OPCION VALIDA!...INTENTE DE NUEVO!"
    return seleccion


def elijo_archivo():
    eleccion_archivo = genero_menu(os.listdir(path), "Archivos de Lista de Precio")
    if eleccion_archivo == len(os.listdir(path)):
        return
    else:
        return "".join([path, "\\", os.listdir(path)[eleccion_archivo]])


def proceso_excel(archivo_abrir):
    limpio_pantalla()
    muestro_titulo(archivo_abrir)
    print("\n\tUd elegio abrir: ", archivo_abrir)
    input("\tContinua?")
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


def main(salir=False):
    while not salir:
        opcion = genero_menu(["Elijo archivo", "Genero Excel", "Actualizo Base de datos"],
                             "Procesador-Actualizador de Listas")
        if opcion == 0:
            archivo_abrir = elijo_archivo()
        elif opcion == 1:
            tipos, lista = proceso_excel(archivo_abrir)
        elif opcion == 2:
            proceso_sql(tipos, lista)
        else:
            limpio_pantalla()
            muestro_titulo("Gracias por utilizar este SCRIPT, vuelva pronto")
            salir = True


if __name__ == '__main__':
    main()
