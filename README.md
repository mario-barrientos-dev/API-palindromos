"# CrudFastAPIempleos" 
## Table of Contents
1. [Información General](#general-info)
2. [Tecnologías](#technologies)
3. [Installatión](#installation)

### General Info
***
API-REST elaborada con Flask, para la verificacion de existencia del palindromo mas grande en una oracion, para su uso se debe autenticar e ir a la ruta "/palindromo", para realizar la autenticacion se debe ir a la ruta "/login" y generar un JSON con username :  Mario Barrientos, ademas de ello al momento de hacer las solicitudes de polindromo se debe realizar de la siguiente manera en formato JSON {
    "word": "LA PALABRA A CONSULTAR"
}
## Technologies
***
Lista de tecnologias usadas en el proyecto con su respectiva version

1. click==8.1.3
2. colorama==0.4.5
3. Flask==2.2.2
4. itsdangerous==2.1.2
5. Jinja2==3.1.2
6. MarkupSafe==2.1.1
7. PyJWT==2.5.0
8. python-dotenv==0.21.0
9. Werkzeug==2.2.2
10. wincertstore==0.2

### installation

Para su instalacion se puede realizar con docker