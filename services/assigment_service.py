from uuid import UUID
from google import genai
from sqlalchemy.orm import Session
from repositories.kitchen_config import get_by
from repositories.kitchen_type import get_type_by_id

client = genai.Client(api_key="AIzaSyDJZ6xQdUuxyF_uvqKiJfZV0lgXC6xofdQ")


def send_message_to_ai(user_id: UUID, config_id: UUID, db: Session):
    kitchen_config = get_by(user_id, config_id, db)
    if not kitchen_config:
        raise Exception("Kitchen configuration not found")

    kitchen_type = get_type_by_id(db, kitchen_config.kitchen_type_id)
    if not kitchen_type:
        raise Exception("Kitchen type not found")
    
    prompt = (
        f"Quiero que actúes como un diseñador experto en organización de cocinas de restaurantes.\n"
        f"Esta es la información de la cocina:\n\n"
        f"- Tipo de cocina: {kitchen_type.type}\n"
        f"- Área disponible: {kitchen_config.area} m2\n"
        f"- Número de estaciones de trabajo: {kitchen_config.num_stations}\n"
        f"- Número de empleados: {kitchen_config.staff_count}\n"
        f"- Notas: {kitchen_config.notes}\n\n"
        f"Con base en estos datos, proporciona una recomendación detallada sobre cómo organizar el espacio, "
        f"ubicación de estaciones, optimización de flujos de trabajo y sugerencias para mejorar la eficiencia."
    )


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text
    

    
    
    # return {'config': kitchen_config, 'type':kitchen_type}

