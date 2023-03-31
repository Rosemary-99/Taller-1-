# Ejecución

Integrantes: Rosemary Ríos Pulido

Alcance del proyecto: El presente proyecto tiene como objetivo detallar e integrar de forma práctica y didáctica las habilidades adquiridas durante el curso de Gestión de Datos, aquí se evidencia mediante una aplicación que hace uso de datos estructurados y modelos machin learning, como se puede apoyar a plataformas como Spotify con la interacción de sus usuarios para recomendar canciones, de acuerdo con sus gustos y la data recopilada durante años en esta plataforma. La aplicación desarollada involucra componentes de almacenamiento y transformación de datos, creación y publicación de modelos de machine learning (backend), así como de interacción con el usuario (frontend).

Contexto aplicación: Recomendación de canciones a partir de una simulación de reproducción realizada por el usuario. Una vez el usuario reproduce una canción, la aplicación le recomienda un conjunto de canciones que potencialmente serán de su agrado.

Carcateristicas generales del proyecto: El proyecto se basa en la metodología CRISP-DM, por tal motivo como se evidencia en el documento final, se inicia por un entendimiento del negocio, seguido de un entimiento de los datos, preparación de los datos, modelación parte en la cual se construye el modelo, evaluación en donde se valida su funcionamiento y el despliegue que finalmente arroja como resultado la recomendación de las canciones para los usuarios. 
Organización del repositorio

1) Taller_1_Spotify_Rosemary_Rios.ipynb
2) Ajustes_data_frame_para_exportar_código_parte_1_taller_.ipynb
3) Project_Mongodb_to_bigquery.ipynb 
4) Anexos 1, 2 y 3
5) .json
6) Dashboard power bi (adjunto en la entrega del aula virtual ya que por el tamaño del archivo no se puede subir en github)
7) Recomienda_Spotify.ipynb
8)SS_app.jpg
9)Dashboard (1).pdf
10) main.py
11) prediction_model.py
12) main.html
13) recomendaciónpg.html
14) detallesinterfaz.css
15) Taller parte 3.pdf 

Detalles de la Ejecución
- Inicie corriendo Taller_1_Spotify_Rosemary_Rios.ipynb
- De acuerdo con la metodología CRISP- DM para poder modelar y utilizar los archivos con los datos adecuados, se retrocede a la etapa 3  de Data Preparation realizando un ajuste del primer paso antes de exportar el track_df se realizó una nueva limpieza de datos retirando los paréntesis cuadrados [] y las comillas simples, para que dentro de la base de datos de Postgress se pudiera realizar una conversión y así los datos no fueran recibidos solo como un texto si no como un  Array, guardándolo como un archivo csv con la siguiente función: track_df.to_cs. Lo mismo ocurrió con artis_mod, con la diferencia que en este; para géneros se dejó la información como un texto plano sin mucha modificación correr Ajustes_data_frame_para_exportar_código_parte_1_taller_.ipynb
- Una vez normalizados los 2 dos archivos se realizó la importación hacia la base de datos de  Postgress, para ello se utilizó Jupyter como bloc de notas para realizar la conexión, se adjunta código por cada una de las tablas (Anexo 1-import_songs.py y Anexo 2 import_artist.py)
- Para ejecutar correctamente los códigos, en cada una de las importaciones es necesario que quien quiera correr el programa cambie en la conexión el password y la ruta en read_csv, de este modo al  momento de comprobar su funcionamiento lo podrá realizar desde su equipo. De igual forma, para  no generar un error en la instalación se debe ejecutar en el CMD de Windows lo siguiente:
pip install pandas
pip install psycopg2-binary
pip install SQLAlchemy
- Una vez importados los datos a Postgress, fue necesario crear una nueva columna en la tabla de songs (tracks_mod) dado que al importar la columna artist y id_artist esta no era tomada como un arreglo; para ello se utilizó el siguiente código:
ALERT TABLE songs ADD COLUMN artist1 TEXT [];
UPDATE songs SET artist1 = string_to_array(artists, ‘,’);
ALERT TABLE songs ADD COLUMN id_artist1 TEXT [];
UPDATE songs SET id_artist1 = string_to_array(id_artists, ‘,’);
Esta función permitió encontrar la llave que conectaría las tablas ver anexo 3.
- Con los datos de canciones y artistas limpios y almacenados en PostgreSQL y BigQuery, se construyeron dos productos de datos, estos los puede consultar el docente en la entrega del aula virtual o dentro del PDF Taller parte 3.pdf 
- Correr Recomienda_Spotify.ipynb
- en su escritorio puede abrir picharm allí en una hoja diferente copie los siguientes codigos: main.py,  prediction_model.py, main.html, recomendaciónpg.html detallesinterfaz.css

Cabe resaltar que por el tamaño de los archivos los CSV normalizados no se pueden cargar en Git Hub, sin embargo al ejecutar cada uno de los codigos y de acuerdo con las instrucciones, se generarán los nuevos archivos CSV.
