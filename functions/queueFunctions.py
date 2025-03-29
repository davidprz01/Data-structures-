from model.ticket import Ticket
from controller.ticketController import TicketController


# def add_queue(ticket: Ticket, ticketTypes: dict) -> None:

#     if ticket.type not in ticketTypes:
#         print(f"El tipo de atencion no es valido: {ticket.type}")
#         return
    
#     if ticket.age > 60:
#         ticket.priority_attention = True


#     print("Añadir ticket a la cola")
#     ticketTypes[ticket.type].enqueue(ticket)
#     print("Ticket añadido a la cola")

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    print(f"\nIniciando add_queue para: {ticket.name} ({ticket.type})")
    
    # Verificación de tipo
    if ticket.type not in ticketTypes:
        error_msg = f"Error: Tipo '{ticket.type}' no válido. Tipos aceptados: {list(ticketTypes.keys())}"
        print(error_msg)
        raise ValueError(error_msg)
    
    # Aplicar prioridad automática
    original_priority = ticket.priority_attention
    if ticket.age > 60 and not ticket.priority_attention:
        ticket.priority_attention = True
        print(f"Prioridad automática aplicada (edad {ticket.age} años)")
    
    # Depuración antes de encolar
    print(f"Datos del ticket a encolar:")
    print(f"- Nombre: {ticket.name}")
    print(f"- Tipo: {ticket.type}")
    print(f"- Prioridad: {ticket.priority_attention}")
    print(f"- Edad: {ticket.age}")
    
    try:
        # Encolar el ticket
        ticketTypes[ticket.type].enqueue(ticket)
        
        # Verificación posterior
        print(f"\nTicket de {ticket.name} encolado exitosamente en {ticket.type}")
        print(f"Estado actual de la cola {ticket.type}:")
        
        # Mostrar contenido de la cola (para depuración)
        current = ticketTypes[ticket.type].head
        count = 0
        while current:
            count += 1
            print(f"  {count}. {current.data.name} (Prioridad: {current.priority})")
            current = current.next
        
        if count == 0:
            print("  (La cola está vacía)")
            
    except Exception as e:
        error_msg = f"Error al encolar ticket: {str(e)}"
        print(error_msg)
        raise RuntimeError(error_msg)