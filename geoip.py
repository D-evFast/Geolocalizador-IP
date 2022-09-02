import requests #Importamos la librería.
def geoip(ip):   #Función que se encargará de geolocalizar la ip. 
    datos = ["city", "region", "country","org"]
    dict_data = {"city": None, "region": None, "country": None, "org": None}
    #Tipos de datos necesarios (lista y diccionario)
    for x in datos: #Recorremos la lista para ir acoplando información al diccionario.
        url = f"https://ipinfo.io/{ip}/{x}" #Url a la cual haremos la petición para recibir la información.
        response = requests.get(url) #Con la librería request hacemos la petición. 
        if response.status_code == 200: #Si el estado es 200 es que la petición fue correcta. 
            result = response.content.decode("utf-8").replace("\n", "") #Obtenemos los valores de la respuesta. 
            if result != "": 
                dict_data[x] = result
            else:
                dict_data[x] = "Desconocido."
            #Hacemos una validación por si llega a faltar información.
        else:
            dict_data[x] = 404
        #Declaramos 404 en los valores del diccionario y abajo arrojamos el error xD.
    if dict_data["city"] == 404:
        print("Dirección IP fuera de rango o prohibida.")
        #En caso de que la respuesta no sea 202 (correcta), arrojamos un error. 
    else:
        print(f"Información obtenida ({ip}):\n\nPaís: {dict_data['country']}.\nCiudad: {dict_data['city']}.\nRegión: {dict_data['region']}.\nISP: {dict_data['org']}")
    #Imprimimos la información en caso de que no haya error 404 (no haya errores).
def main(): #Función donde pediremos la IP al usuario y se pasará como parametro a "geoip()" que es la función que recién comente arriba. 
    ip = input("Ingrese la dirección IP: ") #Pedimos IP.
    geoip(ip) #Pasamos ip.

main() #Ejecutamos.
