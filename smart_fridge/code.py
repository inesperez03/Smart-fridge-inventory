from datetime import datetime, timedelta
from time import sleep

def añadir_producto(id):
  id_esc = id.value
  global dic_productos
  global dic_id_prod
  #Mirar que producto esta asociado a la ID
  if id_esc in dic_id_prod:
    prod_nom = dic_id_prod[id_esc][0]
  else:
    titulo_añadir_confirmación.value = "No está el producto en la base de datos"
    titulo_añadir_confirmación.show()
    return
  #Calcular la caducidad
  fecha = datetime.today() + timedelta(days=dic_id_prod[id_esc][1])
  #Añadir producto en el listado de productos
  if id_esc in dic_productos:
    dic_productos[id_esc][1] += 1
    dic_productos[id_esc][2].append(fecha)
  else:
    dic_productos[id_esc] = [prod_nom, 1, [fecha]]
  titulo_añadir_confirmación.value = "Se ha añadido el producto (" + prod_nom + ") con exito"
  titulo_añadir_confirmación.show()

def eliminar_producto(id):
  id_esc = id.value
  global dic_productos
  global dic_id_prod
  #Mirar que producto esta asociado a la ID
  if id_esc in dic_id_prod:
    prod_nom = dic_id_prod[id_esc][0]
  else:
    titulo_retirar_confirmación.value = "No está el producto en la base de datos"
    titulo_retirar_confirmación.show()
    return
  #Eliminar producto en el listado de productos
  if id_esc in dic_productos:
    if dic_productos[id_esc][1] > 1:
      dic_productos[id_esc][1] -= 1
      del dic_productos[id_esc][2][0]
    else:
      del dic_productos[id_esc]
    titulo_retirar_confirmación.value = "Se ha eliminado el producto (" + prod_nom + ") con exito"
    titulo_retirar_confirmación.show()
  else:
    titulo_retirar_confirmación.value = "No está el producto en la nevera"
    titulo_retirar_confirmación.show()

#Esta función indica los productos proximos a caducar en menos de 7 días.

def caducidad_proxima():
  global dic_productos
  global dic_id_prod
  lista_caducidad_proxima = []
  for id_esc in dic_productos:
    for fecha_caducidad in dic_productos[id_esc][2]:
      dias_faltantes = fecha_caducidad - datetime.today()
      if dias_faltantes.days < 7:
        lista_caducidad_proxima.append((dic_productos[id_esc][0],dias_faltantes.days))
  return lista_caducidad_proxima

def recetas(op):
  global dic_productos
  global dic_id_prod
  lista_productos_faltantes = []
  inventario_actual = []
  receta = []
  for producto in dic_productos:
      inventario_actual.append(dic_productos[producto][0])
  if(op == 1):
      receta = ["Tomate frito", "Cebolla", "Espaguetis", "Queso", "Carne picada", "Aceite"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)
  elif (op == 2):
      receta = ["Yogurt","Aceite","Azucar","Harina","Huevos","Limón"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)
  elif (op == 3):
      receta = ["Aceite","Huevos","Cebolla","Patata"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)
  elif (op == 4):
      receta = ["Harina","Aceite","Huevo","Tomate frito","Cebolla", "Atún"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)
  elif (op == 5):
      receta = ["Patata","Guisantes","Atún","Huevo","Aceite"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)
  elif (op == 6):
      receta = ["Leche","Azucar","Huevo","Limón"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)
  elif (op == 7):
      receta = ["Harina","Azucar","Huevos","Aceite","Chocolate"]
      for ingr in receta:
          if ingr not in inventario_actual:
              lista_productos_faltantes.append(ingr)


  return receta, lista_productos_faltantes


n = 0
dic_productos = {}
dic_id_prod = {'8422241812846':('Queso', 50), '8076809513739':('Tomate frito', 6), '8420722980015':('Aceite',300),
               '8431876011920':('Leche',15), '8436537300092':('Yogurt',30), '8480000835475':('Cebolla',5),
               '8720039607453':('Azucar',190),'8001348103363':('Harina',90),'8410728100036':('Chocolate',50),
               '5702017596976':('Espaguetis',150),'8410843145165':('Carne picada',5),'3379140056381':('Guisantes',15),
               '3560071006433':('Patata',5), '2050000012433':('Huevos', 7),'8480000232649':('Atún',30),
               '8424088112219':('Limón',16)}



from guizero import App, Text, PushButton, Picture, TextBox, Window, Box, ListBox

def option(opcion):
    welcome_message.value = opcion

def open_window(ventana):
    if(ventana == 1):
        Añadir_ventana.show(wait=True)
    elif (ventana == 2):
        Retirar_ventana.show(wait=True)
    elif (ventana == 3):
        lista_caducidad_prod.clear()
        lista_caducidad_cant.clear()
        for prod in caducidad_proxima():
            print(prod[0])
            lista_caducidad_prod.append(prod[0])
            lista_caducidad_cant.append(prod[1])

        Caducidad_ventana.show(wait=True)
    elif (ventana == 4):
        Receta_ventana.show(wait=True)
    elif (ventana == 5):
        lista_inventario_prod.clear()
        lista_inventario_cant.clear()
        for prod in dic_productos:
            lista_inventario_prod.append(dic_productos[prod][0])
            lista_inventario_cant.append(dic_productos[prod][1])

        Inventario_ventana.show(wait=True)

def close_window(ventana):
    if(ventana == 1):
        Añadir_ventana.hide()
    elif (ventana == 2):
        Retirar_ventana.hide()
    elif (ventana == 3):
        Caducidad_ventana.hide()
    elif (ventana == 4):
        Receta_ventana.hide()
    elif (ventana == 5):
        Inventario_ventana.hide()
    elif (ventana == 6):
        Receta_ventana2.hide()

app = App(title="Nevera inteligente")
welcome_message = Text(app, text="Bienvenido a la nevera inteligente", size=20, font="Times New Roman", color="Darkblue")

#Añadir producto

Añadir_ventana = Window(app, title="Añadir producto")
Añadir_ventana.hide()
abrir_añadir = PushButton(app, command=open_window, args=[1], text="Añadir producto",width="fill", height="fill", align="left")


titulo_añadir = Text(Añadir_ventana, text="Añadir producto", size=20, font="Times New Roman", color="Darkblue",  align="top",height="fill")
introd_cod_añadir = Text(Añadir_ventana, text="Introduce el codigo que quieras añadir", size=15, font="Times New Roman", color="red",  align="top", height="fill")
codigo_añadir = TextBox(Añadir_ventana,height="fill", width="fill")
confirmar_id_añadir = PushButton(Añadir_ventana, text="Confirmar", command=añadir_producto, align="top", args=[codigo_añadir])
titulo_añadir_confirmación = Text(Añadir_ventana, text="Nada", size=15, font="Times New Roman", color="green",  align="top", height="fill")
titulo_añadir_confirmación.hide()

cerrar_añadir_box = Box(Añadir_ventana, width="fill", align="bottom")
cerrar_añadir = PushButton(cerrar_añadir_box, args=[1], text="Cerrar", command=close_window, align="right")



#Retirar producto

Retirar_ventana = Window(app, title="Retirar producto")
Retirar_ventana.hide()
abrir_quitar = PushButton(app, command=open_window, args=[2], text="Retirar producto",width="fill", height="fill", align="right")


titulo_retirar = Text(Retirar_ventana, text="Retirar producto", size=20, font="Times New Roman", color="Darkblue",  align="top",height="fill")
introd_cod_retirar = Text(Retirar_ventana, text="Introduce el codigo que quieras retirar", size=15, font="Times New Roman", color="red",  align="top", height="fill")
codigo_retirar = TextBox(Retirar_ventana,height="fill", width="fill")
confirmar_id_retirar = PushButton(Retirar_ventana, text="Confirmar", command=eliminar_producto, align="top", args=[codigo_retirar])
titulo_retirar_confirmación = Text(Retirar_ventana, text="Nada", size=15, font="Times New Roman", color="green",  align="top", height="fill")
titulo_retirar_confirmación.hide()

cerrar_retirar_box = Box(Retirar_ventana, width="fill", align="bottom")
cerrar_retirar = PushButton(cerrar_retirar_box, args=[2], text="Cerrar", command=close_window, align="right")


#Caducidad

Caducidad_ventana = Window(app, title="Caducidad")
Caducidad_ventana.hide()
abrir_caducidad = PushButton(app, command=open_window, args=[3], text="Lista de proximos caducados", width="fill", height="fill", align="bottom")

titulo_caducidad = Text(Caducidad_ventana, text="Lista de proximos caducados", size=20, font="Times New Roman", color="Darkblue",  align="top",height="fill")

caducidad_box = Box(Caducidad_ventana, width="fill", height="fill", align="top")
caducidad_box_prod = Box(caducidad_box, width="fill", height="fill", align="left")
caducidad_box_cant = Box(caducidad_box, width="fill", height="fill", align="left")


titulo_caducidad_prod = Text(caducidad_box_prod, text="Productos", size=16, font="Times New Roman", color="Darkgreen",  align="top")
lista_caducidad_prod = ListBox(caducidad_box_prod, items=[], height="fill", width="fill", align="left")
lista_caducidad_prod.text_size = 12

titulo_caducidad_cant = Text(caducidad_box_cant, text="Días restantes", size=16, font="Times New Roman", color="Darkgreen",  align="top")
lista_caducidad_cant = ListBox(caducidad_box_cant, items=[], height="fill", width="fill", align="left")
lista_caducidad_cant.text_size = 12

cerrar_caducidad_box = Box(Caducidad_ventana, width="fill", align="bottom")
cerrar_caducidad = PushButton(cerrar_caducidad_box, args=[3], text="Cerrar", command=close_window, align="right")


#Recetas

def open_receta(num):
    ingredientes_total_lista.clear()
    ingredientes_faltan_lista.clear()
    if(num == 1):
        Receta_ventana2.title = "Espaguetis a la boloñesa"
        ingredientes_tittle.value = "Espaguetis a la boloñesa"
        plato.value = "Espaguetis.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)
    elif (num == 2):
        Receta_ventana2.title = "Bizcocho de yogur"
        ingredientes_tittle.value = "Bizcocho de yogur"
        plato.value = "Bizcocho.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)
    elif (num == 3):
        Receta_ventana2.title = "Tortilla de patata con cebolla"
        ingredientes_tittle.value = "Tortilla de patata con cebolla"
        plato.value = "Tortilla.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)
    elif (num == 4):
        Receta_ventana2.title = "Empanada de tomate"
        ingredientes_tittle.value = "Empanada de tomate"
        plato.value = "Empanada.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)
    elif (num == 5):
        Receta_ventana2.title = "Ensaladilla rusa"
        ingredientes_tittle.value = "Ensaladilla rusa"
        plato.value = "Ensaladilla.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)
    elif (num == 6):
        Receta_ventana2.title = "Flan de huevo"
        ingredientes_tittle.value = "Flan de huevo"
        plato.value = "Flan.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)
    elif (num == 7):
        Receta_ventana2.title = "Galletas de chocolate"
        ingredientes_tittle.value = "Galletas de chocolate"
        plato.value = "Galletas.png"
        receta, lista_productos_faltantes = recetas(num)
        for ingr1 in receta: ingredientes_total_lista.append(ingr1)
        for ingr2 in lista_productos_faltantes: ingredientes_faltan_lista.append(ingr2)

    Receta_ventana2.show(wait=True)

Receta_ventana = Window(app, title="Recetas")
Receta_ventana.hide()

abrir_receta = PushButton(app, command=open_window, args=[4], text="Receta",width="fill", height="fill", align="top")
Receta1 = PushButton(Receta_ventana, command=open_receta, args=[1], text="Espaguetis a la boloñesa",width="fill", height="fill", align="top")
Receta2 = PushButton(Receta_ventana, command=open_receta, args=[2], text="Bizcocho de yogur",width="fill", height="fill", align="top")
Receta3 = PushButton(Receta_ventana, command=open_receta, args=[3], text="Tortilla de patata con cebolla",width="fill", height="fill", align="top")
Receta4 = PushButton(Receta_ventana, command=open_receta, args=[4], text="Empanada de tomate",width="fill", height="fill", align="top")
Receta5 = PushButton(Receta_ventana, command=open_receta, args=[5], text="Ensaladilla rusa",width="fill", height="fill", align="top")
Receta6 = PushButton(Receta_ventana, command=open_receta, args=[6], text="Flan de huevo",width="fill", height="fill", align="top")
Receta7 = PushButton(Receta_ventana, command=open_receta, args=[7], text="Galletas de chocolate",width="fill", height="fill", align="top")


cerrar_receta_box = Box(Receta_ventana, width="fill", align="bottom")
cerrar_receta = PushButton(cerrar_receta_box, args=[4], text="Cerrar", command=close_window, align="right")

#Ingredientes

Receta_ventana2 = Window(Receta_ventana, title="Ingredientes")
Receta_ventana2.hide()

ingredientes_tittle = Text(Receta_ventana2, text="No receta", size=16, font="Times New Roman", color="Darkgreen",  align="top")

ingredientes_lista_box = Box(Receta_ventana2, width="fill", align="left")
ingredientes_total_tittle = Text(ingredientes_lista_box, text="Ingredientes", size=16, font="Times New Roman", color="Darkgreen",  align="top")
ingredientes_total_lista = ListBox(ingredientes_lista_box, items=[], height="fill", width="fill", align="top")
ingredientes_faltan_tittle = Text(ingredientes_lista_box, text="Ingredientes restantes", size=16, font="Times New Roman", color="Darkgreen",  align="top")
ingredientes_faltan_lista = ListBox(ingredientes_lista_box, items=[], height="fill", width="fill", align="top")

right_ingrediente_box = Box(Receta_ventana2, align="right", height="fill")

plato = Picture(right_ingrediente_box, image="Espaguetis.png", align="right", height=150, width=190)

cerrar_ingrediente = PushButton(right_ingrediente_box, args=[6], text="Cerrar", command=close_window, align="bottom")





#Inventario

Inventario_ventana = Window(app, title="Inventario")
Inventario_ventana.hide()

abrir_inventario = PushButton(app, command=open_window, args=[5], text="Inventario",width="fill", height="fill", align="top")

titulo_inventario = Text(Inventario_ventana, text="Inventario", size=20, font="Times New Roman", color="Darkblue",  align="top",width="fill")


inventario_box = Box(Inventario_ventana, width="fill", height="fill", align="top")
inventario_box_prod = Box(inventario_box, width="fill", height="fill", align="left")
inventario_box_cant = Box(inventario_box, width="fill", height="fill", align="left")


titulo_inventario_prod = Text(inventario_box_prod, text="Productos", size=16, font="Times New Roman", color="Darkgreen",  align="top")
lista_inventario_prod = ListBox(inventario_box_prod, items=[], height="fill", width="fill", align="left")
lista_inventario_prod.text_size = 12

titulo_inventario_cant = Text(inventario_box_cant, text="Cantidades", size=16, font="Times New Roman", color="Darkgreen",  align="top")
lista_inventario_cant = ListBox(inventario_box_cant, items=[], height="fill", width="fill", align="left")
lista_inventario_cant.text_size = 12

cerrar_inventario_box = Box(Inventario_ventana, width="fill", align="bottom")
cerrar_inventario = PushButton(cerrar_inventario_box, args=[5], text="Cerrar", command=close_window, align="right")



app.display()