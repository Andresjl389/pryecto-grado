from fastapi.responses import FileResponse
from weasyprint import HTML
import os
from repositories.kitchen_config import get_by
from repositories.kitchen_type import get_type_by_id
from services.assigment_service import send_message_to_ai



def generate_pdf(config_id, user_id, db):
    kitchen_config = get_by(user_id, config_id, db)
    if not kitchen_config:
        raise Exception("Kitchen configuration not found")

    kitchen_type = get_type_by_id(db, kitchen_config.kitchen_type_id)
    if not kitchen_type:
        raise Exception("Kitchen type not found")

    recommendation_text = send_message_to_ai(user_id, config_id, db)


    html_content = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Open Sans', sans-serif; margin: 40px; }}
            h1, h2, h3 {{ color: #2c3e50; }}
            table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
            table, th, td {{ border: 1px solid #ccc; }}
            th, td {{ padding: 10px; }}
        </style>
    </head>
    <body>
        <h1>Informe de Organización de Cocina</h1>
        <p><strong>Fecha:</strong> 2024-XX-XX</p>
        <hr>
        <h2>Datos de Configuración</h2>
        <table>
            <tr><th>Campo</th><th>Valor</th></tr>
            <tr><td>Tipo de cocina</td><td>{kitchen_type.type}</td></tr>
            <tr><td>Área disponible</td><td>{kitchen_config.area} m²</td></tr>
            <tr><td>Número de estaciones</td><td>{kitchen_config.num_stations}</td></tr>
            <tr><td>Número de empleados</td><td>{kitchen_config.staff_count}</td></tr>
            <tr><td>Notas</td><td>{kitchen_config.notes}</td></tr>
        </table>

        <h2>Distribución y Recomendaciones</h2>
        <p>{recommendation_text}</p>

        <footer style="margin-top: 50px; font-size: 12px; text-align: center;">
            Generado por [Nombre de tu App] - 2024
        </footer>
    </body>
    </html>
    """

    # Crear el PDF
    output_path = f"generated_pdfs/kitchen_report_{config_id}.pdf"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    HTML(string=html_content).write_pdf(output_path)

    # Devolver el PDF como respuesta
    return FileResponse(
        path=output_path,
        filename=f"reporte_cocina_{config_id}.pdf",
        media_type="application/pdf"
    )