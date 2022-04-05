# Generacion de etrenamiento e inferencia para modelo de machine learning usando  AWS

Este proyecto contiene el desarrollo de un modelo de aprendizaje automatico desplegado en aws usando los siguientes componentes de 
de AWS: lambda functions, api gateway, bucket s3, iam role, cloudFormation,aws sam, aws cli.

El despliegue de esta  solucion se realizo en el ide de pycharm y los stack generados fueron desplegados desde el ide anteriormente mencionado mediante el plugin de aws (Aws toolkit)

# Tabla de contenido
- [Definicion](#definicion)
- [Requisitos](#requisitos)
- [Uso de AWS](#aws)
- [Despliegue](#despliegue)



## Definición:

    .
    ├── Deployment Model        
    │   ├── LambdaInference          
    │   │   ├── __init__.py           
    │   │   ├── app.py                
    │   │   ├── Dockerfile            
    │   │   ├── functions.py         
    │   │   ├── requirements.txt      
    │   │   └── utils.py              
    │   ├── LambdaTrain           
    │   │   ├── __init__.py           
    │   │   ├── app.py                
    │   │   ├── Dockerfile            
    │   │   ├── functions.py          
    │   │   ├── requirements.txt      
    │   │   └── utils.py              
    ├── events                        
    ├── images                        
    ├── tests                         
    ├── .gitignore                    
    └── template.yaml                 



A continuacion se detalla la arquitectura para la solucion propuesta


![image.png](images\arquitectura.PNG)

## Requisitos:

* Installar aws cli en su equipo y verificar su instalacion
```JSON
C:\Users\user>aws --version
aws-cli/2.2.11 Python/3.8.8 Windows/10 exe/AMD64 prompt/off
```
* configurar aws cli con claves de usuario de aws cli
```JSON
C:\Users\user>aws configure
AWS Access Key ID [****************LK4H]:
AWS Secret Access Key [****************2oVo]:
Default region name [us-east-1]:
Default output format [aws_juan]:

```
* intallar aws sam
```JSON
C:\Users\user>sam --version
SAM CLI, version 1.24.1
```
* installar el plugin de aws en pycharm
![image.png](images\pycharm.PNG)

* installar docker

```JSON
C:\Users\user>docker --version
Docker version 20.10.5, build 55c4c88
```

## Uso de AWS

* Funciones Lambdas:

 Las funciones lambdas son servicios serverles de aws los cuales nos permiten generar ejecuciones de codigo en maximo 15 minutos y usando un maximo de  en memoria son muy buenas para la exposicion de modelos como servicio puesto que su costo es por milisegundoos y es escalable puesto que crece de manera horizontal es decir se proveen recursos de manera elastica para responder a las diferentes peticiones del cliente.
 
 * Lambda Train