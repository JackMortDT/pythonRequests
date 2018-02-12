import requests, json

response = requests.get('https://api.github.com/user')
response2 = requests.get('https://www.facebook.com')

#Response para la peticion
print(response.status_code)
#Respuesta 401 Unauthorized

print(response2.status_code)
#Respuesta 200 OK

#Pasando valores en la url por medio de llaves y valores
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

valor = "value4"
#Pasando valores en la url con una lista como valor
payload = {'key1': 'value1', 'key2': ['value2', 'value3', valor]}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
#Nota: se pueden pasar valores desde una variable externa

print("*****"*20)

#Con esto podemos leer el contenido de la respuesta del servidor
r = requests.get('http://httpbin.org/')
print(r.status_code)
print(r.text)

#Se puede ver el cuerpo de la respuesta como bytes, para solicitudes que no son de texto
print("****"*20)
print(r.content)

#Respuesta de json
print("****"*20)
print(r.json)

#Si se desea obtener la respuesta de socket sin procesar del servidor, puede acceder '.raw'
print("****"*20)
r = requests.get('http://httpbin.org/', stream=True)
print(r.raw)

#Normalmente, desea enviar algunos datos codificados en forma, como un formulario HTML. 
#Para hacer esto, simplemente pase un diccionario al argumento de datos. 
#Su diccionario de datos se codificará automáticamente cuando se realice la solicitud.
print("****"*20)
payload = {'key1': 'uno', 'key2': ['dos', 'tres']}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

#Se pueden pasar multiples valores igualmente, en forma de lista o separados por coma con
#la misma llave
print("****"*20)
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

#Se puede obtener un mensaje de error mas especifico
print("****"*20)
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
#print(bad_r.raise_for_status())

#Esto se usa para obtener los headers en una petición
print("****"*20)
r = requests.get('http://httpbin.org/')
print(r.headers)

#Y se puede obtener un dato en especifico, no importando si esta en mayusculas o no
print("****"*20)
print(r.headers['Content-Type'])
print(r.headers['Date'])
print(r.headers.get('date'))

#Se pueden persistit algunas cookies en las solicitudes 
print("****"*20)
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

#los parámetros de nivel de método no se conservarán en todas las solicitudes, incluso si se usa una sesión
print("****"*20)
s = requests.Session()
r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
r = s.get('http://httpbin.org/cookies')
print(r.text)

#Se pueden obtener los encabezados que enviamos al servidor
print("****"*20)
r = requests.get('http://www.instagram.com')
print(r.headers)
print("****"*20)
print(r.request.headers)