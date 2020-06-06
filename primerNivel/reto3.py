'''
Reto #3 “Mensaje multilínea”
Instrucciones: seguro has visto que en Platzi hay más de 600 cursos 
¿puedes mostrar a que categorías corresponden en una sola línea de código?
Debe mostrarse así:
Platzi cuenta con cursos de:
[categoría1]
[categoría2]
[categoría3]
[categoría4]
[categoría5]
[categoría6]
'''
categories = ['Desarrollo e ingeniería', 'Diseño y UX', 
'Marketing', 'Negocios y emprendimiento', 'Producción audiovisual',
'Crecimiento profesional']
#Printing the categories in one line
for i in categories:
    print(str([i]))