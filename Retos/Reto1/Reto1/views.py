from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, Template
from sodapy import Socrata
from IPython.display import display
import json
import pandas as pd
import dateutil



def saludo(request):
    # Recibe un request

    # Enlazar URL con esta vista
    return HttpResponse("Hola Mundo funciona la web con Django")


def Generar_Dataframe():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("sdvb-4x4j", limit=5300)
    # Convert to pandas DataFrame
    df = pd.DataFrame.from_records(results)
    df["uso_vacuna"] = df["uso_vacuna"].apply(
        lambda x: str(x).replace("/", ","))
    df['fecha_resolucion'] = df['fecha_resolucion'].apply(
        dateutil.parser.parse)
    df['fecha_corte'] = df['fecha_corte'].apply(dateutil.parser.parse)
    return df


def Guardar_Dataframe(Dataframe_html):
    # Guardar Datos
    file = open("Reto1/Plantillas/Guardado.html", "w")
    file.write(Dataframe_html)
    file.close()


def Estilo_Dataframe(df):
    styles = [
        dict(selector="tr:hover",
             props=[("background", "#f4f4f4")]),
        # Th --> Titulos
        dict(selector="th", props=[("color", "red"),
                                   ("border", "1px solid #eee"),
                                   ("padding", "12px 3px"),
                                   ("border-collapse", "collapse"),
                                   ("background", "#84F6C5"),
                                   ("text-transform", "uppercase"),
                                   ("font-size", "15px")
                                   ]),
        # Td --> Cada fila
        dict(selector="td", props=[("color", "black"),
                                   ("border", "1px solid #eee"),
                                   ("padding", "12px 35px"),
                                   ("border-collapse", "collapse"),
                                   ("font-size", "15px")
                                   ]),
        # Configuraciones Generales Tabla
        dict(selector="table", props=[
            ("font-family", 'Times New Roman'),
            ("margin", "10px "),
            ("border-collapse", "collapse"),
            ("border", "1px solid #eee"),
            ("border-bottom", "2px solid #00cccc"),
        ]),
        dict(selector="caption", props=[("caption-side", "bottom")])
    ]
    #s= results_df.style.set_table_styles(styles).highlight_max().highlight_null(null_color='red')
    Data = df.style.set_table_styles(styles)
    return Data


def Carga_datos(request):

    df = Generar_Dataframe()
    s = Estilo_Dataframe(df)

    #object = df.to_html()
    # Cargar archivo
    doc_externo = open("Reto1/Plantillas/datos.html")
    # Crear template o plantilla  (Almacenar documento)
    plt = Template(doc_externo.read())
    # Cerrar archivo
    doc_externo.close()
    # Creacion contexto
    # Los contextos reciben diccionarios , las claves
    ctx = Context({"Dataframe": s.render()})
    # Renderizar el documento
    documento = plt.render(ctx)
    '''
    Guardar_Dataframe(s.render())
    '''
    return HttpResponse(documento)


def Visualizacion_Plantilla(request):

    df = Generar_Dataframe()
    s = Estilo_Dataframe(df)
    # Cargar archivo
    doc_externo = open(
        "Reto1/Plantillas/Dataframe.html")

    # Crear template o plantilla  (Almacenar documento)
    plt = Template(doc_externo.read())
    # Cerrar archivo
    doc_externo.close()
    # Creacion contexto
    # Los contextos reciben diccionarios , las claves
    ctx = Context({"Dataframe": s.render()})
    # Renderizar el documento
    documento = plt.render(ctx)

    return HttpResponse(documento)


def busqueda(request):

    # Cargar archivo
    doc_externo = open(
        "Reto1/Plantillas/busquedas.html")

    # Crear template o plantilla  (Almacenar documento)
    plt = Template(doc_externo.read())

    # Cerrar archivo
    doc_externo.close()

    # ---------- Obtencion Dataframe --------------
    df = Generar_Dataframe()
    #s = Estilo_Dataframe(df)

    # ---------- Configracion Parametros Busquedas --------------

    nombre_columnas = list(df.columns.values)
    nombre_Vacunas = df['laboratorio_vacuna'].unique().tolist()
    nombre_Territorios = df['nom_territorio'].unique().tolist()
    nombre_Uso = df['uso_vacuna'].unique().tolist()
    nombre_a_o = df['a_o'].unique().tolist()
    nombre_resolucion = df['num_resolucion'].unique().tolist()
    nombre_codigo = df['cod_territorio'].unique().tolist()
    nombre_fecharesolucion = df['fecha_resolucion'].unique().tolist()
    nombre_fechacorte = df['fecha_corte'].unique().tolist()
    
    listaColumnas = json.dumps(nombre_columnas)
    listaVacunas = json.dumps(nombre_Vacunas)
    listaTerritorios = json.dumps(nombre_Territorios)
    listaUsos = json.dumps(nombre_Uso)
    listaa_o = json.dumps(nombre_a_o)
    listaResolucion = json.dumps(nombre_resolucion)
    listaCodigo = json.dumps(nombre_codigo)
    listaFecharesolucion = json.dumps(nombre_fecharesolucion)
    listaFechacorte = json.dumps(nombre_fechacorte)
    
  

   # ---------- Lectura de Parametros deseados de Busqueda --------------
    consultaRecuadro = request.GET.get("recuadro")
    consultaLista = request.GET.get("cosa")
    consultaLista1 = request.GET.get("opt")
    consultaLista2 = request.GET.get("opt2")
    consultaLista3 = request.GET.get("opt3")
    global df_consultado 
    
    
    # ---------- Busquedas --------------
    if consultaLista != '0': 
        print(type(consultaLista),consultaLista)
        
        if (consultaLista=='1'):      
            print('Se Realizo busqueda tipo 1')
        #df[(df['laboratorio_vacuna']==Desplegable1) & (df['nom_territorio']==Desplegable2)]
            df_consultado = df[(df['laboratorio_vacuna'] == consultaLista1) & (df['nom_territorio'] == consultaLista2)]
        elif(consultaLista=='2'):
        # Se Realizo busqueda tipo 2
            df_consultado = df[(df['uso_vacuna']==consultaLista1) & (pd.to_numeric(df['cod_territorio'])==int(consultaRecuadro))]
        elif (consultaLista=='3'):
            # Se Realizo busqueda tipo 3
            
            if consultaLista1 == 'num_resolucion':
                df_consultado = df[df['num_resolucion']==consultaLista2]
            elif(consultaLista1 == 'a_o'):
                df_consultado = df[df['a_o']==consultaLista2]
            elif(consultaLista1 == 'cod_territorio'):
                df_consultado = df[df['cod_territorio']==consultaLista2]
            elif(consultaLista1 == 'nom_territorio'):
                df_consultado = df[df['nom_territorio']==consultaLista2]
            elif(consultaLista1 == 'laboratorio_vacuna'):
                df_consultado = df[df['laboratorio_vacuna']==consultaLista2]
            elif(consultaLista1 == 'uso_vacuna'):
                df_consultado = df[df['uso_vacuna']==consultaLista2]
   
        elif (consultaLista=='4'):
            
            # Se Realizo busqueda tipo 4
            if consultaLista2=='>':
                df_consultado =df[pd.to_numeric(df['cantidad'])>int(consultaRecuadro)]
            elif consultaLista2=='<':
                df_consultado =df[pd.to_numeric(df['cantidad'])<int(consultaRecuadro)]
            elif consultaLista2=='=':
                df_consultado =df[pd.to_numeric(df['cantidad'])==int(consultaRecuadro)]
            elif consultaLista2=='<=':
                df_consultado =df[pd.to_numeric(df['cantidad'])<=int(consultaRecuadro)]
            elif consultaLista2=='>=':
                df_consultado =df[pd.to_numeric(df['cantidad'])>=int(consultaRecuadro)]
       
        elif (consultaLista=='5'):
             # Se Realizo busqueda tipo 5
            df_consultado = df[(df[consultaLista1]==consultaLista2) | (df[consultaLista1]==consultaLista3)]
        else : 
            df_consultado=df  
    else: 
        df_consultado=df  
    #df_consultado=df  
       #-----------Opciones de Organización ------------------------ 
    s = Estilo_Dataframe(df_consultado)
    
        # Creacion contexto
    ctx = Context({"listaColumnas": listaColumnas,
                   "listaVacunas": listaVacunas,
                   "listaUsos": listaUsos,
                   "listaTerritorios": listaTerritorios,
                   "listaa_o": listaa_o,
                   "listaResolucion": listaResolucion,
                   "listaCodigo": listaCodigo,
                   "listaFecharesolucion": listaFecharesolucion,
                   "listaFechacorte": listaFechacorte,
                   "Dataframe": s.render(),
                   "ConsultadoRecuadro": consultaRecuadro,
                   "ConsultadoLista": consultaLista,
                   "ConsultadoLista1": consultaLista1,
                   "ConsultadoLista2": consultaLista2,
                   "ConsultadoLista3": consultaLista3,
                   })
    # Renderizar el documento
    documento = plt.render(ctx)
    
    if request.method == 'POST':
        a = request.POST['Orden']
        global df_final
        df_consultado['cantidad']=pd.to_numeric(df_consultado['cantidad'])
        df_consultado['cod_territorio']=pd.to_numeric(df_consultado['cod_territorio'])
        
        if (a=='1'):
            print("Se quiere opcion1")
            #Cantidad Menor
            df_final = df_consultado.sort_values('cantidad',ascending=True)  
        elif (a=='2'):
            print("Se quiere opcion2")
            #Cantidad Mayor
            df_final = df_consultado.sort_values('cantidad',ascending=False)
        elif (a=='3'):
            print("Se quiere opcion3")
            #Territorio Ascendente
            df_final= df_consultado.sort_values('nom_territorio',ascending=True)
        elif (a=='4'):
            print("Se quiere opcion4")
            #Territorio Descendente
            df_final = df_consultado.sort_values('nom_territorio',ascending=False)
        elif (a=='5'):
            print("Se quiere opcion5")
            #Cod Territorio Ascendente
            df_final = df_consultado.sort_values('cod_territorio',ascending=True)
        elif (a=='6'):
            print("Se quiere opcion6")
            #Cod Territorio Descendente
            df_final = df_consultado.sort_values('cod_territorio',ascending=False)
        elif (a=='7'):
            print("Se quiere opcion7")
            #Laboratorio Ascendente
            df_final = df_consultado.sort_values('laboratorio_vacuna',ascending=True)
        elif (a=='8'):
            print("Se quiere opcion8")
            #Laboratorio Descendente
            df_final = df_consultado.sort_values('laboratorio_vacuna',ascending=False)
            
        x = Estilo_Dataframe(df_final)
        return JsonResponse({"resultado": x.render()})
    else:
        
    
        return HttpResponse(documento)








