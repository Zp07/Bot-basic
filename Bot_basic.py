
 # Bot: Atención al cliente

# Supongamos que camiTech quiere construir un bot que nos ayude a reclutar nuevos alumnos para la ciencia de datos

# Datos user
print("Responde las siguientes preguntas:" +"/n")
name = input("name: ")
last_name = input("last_name: ")
age = input("edad: ")

 # Data bases (basic)
cursos = {
    "DS1":{
        "course name":"Introducción a la ciencia de datos con python",
        "star date":"10/06/2023",
        "cost":500,
        "instructor":"Camilo Zapata"
    },
    "P1" : {
        "course name":"Introducción a python",
        "star date":"18/06/2023",
        "cost":500,
        "instructor":"Camilo Zapata"
    }
    
}

# function create courses
def create_course(id_,c_name,star_date,cost,instructor):
    cursos[id_] = {
        "course name":c_name,
        "star date" : star_date,
        "cost": cost,
        "instructor": instructor
    }

create_course('p2','Curso intensivo de python','01/08/23','250','Camilo zapata')

#This devolve a loop for data bases
for c in cursos.keys():
    print(f"Nombre del curso: {cursos[c]['course name']}")
    print(f"Fecha de inicio: {cursos[c]['star date']}")
    print(f"Costo: ${cursos[c]['cost']}")
    print("-------"+'\n')

# Create bot basic()
def bot():
    interes = input("¿Te interesa inscribirte a un curso de programación ").lower()
    if interes == "si":
        print('\n'+"¡Que bueno que te interesó!"+'\n'+'¿Cual curso te interesa?'+'\n')
        contador = 1
        for c in cursos.keys():
            print(f"{contador}- {cursos[c]['course name']}"+'\n')
            contador += 1
        curso = input("Indice del curso seleccionado ")
        curso_key = list(cursos.keys())[int(curso)-1]
        more_info = input('¿Te gustaría recibir más información ').lower()
        
        if more_info == "si":
            print('\n'+"-------")
            print(f"Nombre del curso: {cursos[curso_key]['course name']}")
            print(f"Fecha de inicio: {cursos[curso_key]['star date']}")
            print(f"Costo: ${cursos[curso_key]['cost']}")
            print("-------"+'\n')
            print('\n'+'Perfecto!')
            
            pago = input("Estamos listos para realizar el pago? ").lower()
            if pago == "si":
                print("Perfecto! dame un momento")
            else:
                print("Excelente! piensalo y regresa")
        
        elif more_info == "no":
            print("Perfecto! Que tenga un buen día")
            bot()
        else:
            print("No entendí tu instrucción")
            bot()
        
            
        
    elif interes =="no":
        print("Entendido! En caso de cambiar la opinión, aquí estaré para brindarte información")
    else:
        print("No entendí la respuesta, vuelve a intentarlo")
        bot()

#meta
app = bot()

