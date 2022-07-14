
import click
import cloudinary.uploader
import cloudinary.api
from flask.cli import AppGroup
from api.models import db, Usuario, Actividad, Evento, Participantes_Evento, Tipo_De_Actividad

cloudinary.config( 
  cloud_name = "daint2d1l", 
  api_key = "628783722917876", 
  api_secret = "Csb_-ttIflLqaB_SdRrpcEPpSuU" 
)


"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-provincias" that you can run from the command line
    by typing: $ flask insert-provincias

    """
    #Para agregar a información de las tablas poner en la terminal "flask" + el nombre del comando ej. insert-provincias (para agregar las provincias)
    # $ flask insert-provincias
        
    @app.cli.command("insert-tipo_de_actividad") 
    def insert_tipo_de_actividad_data():
        if len(Tipo_De_Actividad.query.all()) == 0:
            tipos_de_actividad = ["Exterior", "Interior"]
            for tipo_de_actividad in tipos_de_actividad:
                tipo = Tipo_De_Actividad()
                tipo.tipo = tipo_de_actividad
                db.session.add(tipo)
                print("Tipo_de_actividad: ", tipo.tipo, " created.")
            db.session.commit()
            
            print("All tipos de actividad created")

        else:
            print("La tabla Tipo_de_Actividad ya está llena.")

    @app.cli.command("insert-actividades") 
    def insert_actividades_data():
        if len(Actividad.query.all()) == 0:
            actividades = [
                {"nombre": "Juegos de agua", "descripcion": "Planea refrescantes juegos de agua en verano para tus hijos y sus nuevos amigos. Cada participante lleva los implementos necesarios. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":1, "imagen":"url"},
                {"nombre": "Jugar Futbol", "descripcion": "Organiza una jugada al futbol con tus hijos y sus nuevos amigos. Cada participante lleva los implementos necesarios. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable. ", "tipo_de_actividad_id":1, "imagen":"url"},
                {"nombre": "Picnic", "descripcion": "Ten un picnic con tus hijos y sus nuevos amigos. Cada participante lleva algo para compartir entre todos. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":1, "imagen":"url"},
                {"nombre": "Ruta en ruedas", "descripcion": "Montar en Bici, patines o patineta. Cada participante lleva su vehiculo. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":1, "imagen":"url"},
                {"nombre": "Juego Libre", "descripcion": "Tus hijos y sus nuevos amigos podrán jugar libremente en el parque. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":1, "imagen":"url"},
                {"nombre": "Manualidades", "descripcion": "Organiza una sesión de manualidades para tus hijos y sus nuevos amigos. Cada participante lleva los implementos necesarios. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":2, "imagen":"url"},
                {"nombre": "Lectura de cuentos/libros", "descripcion": "Planea una sesión de lectura para tus hijos y sus nuevos amigos. Cada participante puede llevar un libro. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":2, "imagen":"url"},
                {"nombre": "Juegos de mesa/puzzles", "descripcion": "Organiza una sesión de juegos de mesa  y/o puzzles para tus hijos y sus nuevos amigos. Cada participante puede llevar un juego/puzzle. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":2, "imagen":"url"},
                {"nombre": "Juego Libre", "descripcion": "Tus hijos y sus nuevos amigos podrán jugar libremente. Tú eliges el lugar. Cada participante requiere de la compañia de un adulto responsable.", "tipo_de_actividad_id":2, "imagen":"url"}]
            for obj_actividad in actividades:
                actividad = Actividad()
                actividad.nombre = obj_actividad["nombre"]
                actividad.descripcion = obj_actividad["descripcion"]
                actividad.tipo_de_actividad_id = obj_actividad["tipo_de_actividad_id"]
                actividad.imagen = obj_actividad["imagen"]
                db.session.add(actividad)
                print("Actividad: ", actividad.nombre, " created.")
            db.session.commit()  

            print("All actividades created")

        else:
            print("La tabla Actividad ya está llena.")

    @app.cli.command("insert-imagenes_actividades") 
    def insert_imagenes_data():
        imagenes_actividades = [
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657739997/Actividades/Juegos_de_agua_2_yv9fxx.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657740005/Actividades/Jugar_futbol_fgc9oh.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657740014/Actividades/picnic_ld4xkh.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657740761/Actividades/ruta_en_ruedas_2_xeyvhz.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657739995/Actividades/juego_libre_parque_dawbus.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657740011/Actividades/manualidades_2_agwbqz.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657740008/Actividades/lectura_dqkyzu.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657740002/Actividades/juegos_de_mesa_2_zqjk4p.jpg",
            "https://res.cloudinary.com/daint2d1l/image/upload/v1657739992/Actividades/juego_libre_interior_2_pez56h.jpg"]

        todas_actividades = Actividad.query.all()
        for i,actividad in enumerate(todas_actividades):
            actividad.imagen = imagenes_actividades[i]
        db.session.commit()

        print("Imagenes cargadas correctamente")

    
    
