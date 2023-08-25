"""
El módulo sys es un módulo incorporado en Python que proporciona acceso a variables y 
funciones relacionadas con la configuración y el funcionamiento del intérprete de Python. 
A través del módulo sys, puedes interactuar con aspectos del sistema, así como obtener 
información sobre el entorno de ejecución de tu programa.

Algunas de las funciones y atributos más comunes del módulo sys incluyen:

1) sys.argv: Una lista que contiene los argumentos de línea de comandos pasados al script Python en ejecución. 
El primer elemento (sys.argv[0]) generalmente contiene el nombre del archivo del script.

2) sys.exit(): Una función que se utiliza para salir del programa. Puedes pasar un código de 
salida opcional como argumento.

3) sys.modules: Un diccionario que contiene todos los módulos importados actualmente. 
Las claves son los nombres de los módulos y los valores son las referencias a los módulos.

4) sys.path: Una lista de directorios donde Python busca módulos para importar. 
Puedes modificar esta lista para agregar rutas de búsqueda personalizadas.

5) sys.platform: Una cadena que indica la plataforma en la que se está ejecutando
 Python (por ejemplo, "win32" para Windows o "linux" para Linux).

6) sys.version: Una cadena que muestra la versión de Python que estás utilizando.

7)sys.stdin, sys.stdout, sys.stderr: Flujos de entrada, salida y error estándar
 respectivamente. Puedes redirigir estos flujos para capturar o redirigir la entrada/salida.

8) sys.getsizeof(): Una función que devuelve el tamaño en bytes de un objeto.

9) sys.maxsize: El valor máximo permitido para un objeto de tipo int en la plataforma actual.

10) sys.getfilesystemencoding(): Devuelve el nombre del sistema de codificación de archivos 
utilizado por el sistema operativo."""