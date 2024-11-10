""" * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa."""

print('Hola, bienvenido a tu agenda')
print("""Elige que quieres hacer:
1.-Buscar
2.-Insertar
3.-Eliminar contacto
""")

eleccion=int(input())

contactos={}

if eleccion == 2:
    nombre = input('Nombre: ')
    telefono = int(input('Teléfono: '))
    contactos[nombre]=telefono

print(contactos)