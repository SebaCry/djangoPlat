from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice(invoice_data, output_filename):
    """
    Generates a PDF invoice.

    Args:
        invoice_data (dict): Dictionary containing invoice details.
        output_filename (str): The name of the output PDF file.
    """
    # Create a canvas object
    pdf = canvas.Canvas(output_filename, pagesize=letter)
    pdf.setTitle("Factura")

    pdf.drawString(50, 750, f"Numero telefonico: {invoice_data['numero_telefonico']}")
    pdf.drawString(50, 730, f'Nombre de cliente: {invoice_data['nombre_cliente']}')
    pdf.drawString(50, 710, f'Fecha: {invoice_data['fecha']}')

    pdf.line(50, 700, 550, 700)

    pdf.drawString(50, 680, 'Producto')
    pdf.drawString(300, 680, 'Cantidad')
    pdf.drawString(400, 680, 'Precio')
    pdf.drawString(500, 680, 'Total')

    pdf.line(50,670, 550, 670)

    y = 650

    for producto in invoice_data['productos']:
        pdf.drawString(50, y, producto['nombre'])
        pdf.drawString(300, y, str(producto['cantidad']))
        pdf.drawString(400, y, f"${producto['precio']:.2f}")
        pdf.drawString(500, y, f"${producto['cantidad'] * producto['precio']:.2f}")
        y -= 20

    pdf.line(50, y, 550, y)
    y -= 20
    pdf.drawString(400, y, 'Total')
    pdf.drawString(500, y, f'${invoice_data['total']:.2f}')

    pdf.save()
    print('PDF terminado')



invoice_data = {
    "numero_telefonico": "3223151556",
    "nombre_cliente": "Sebastian Perez",
    "fecha": "2025-06-09",
    "productos": [
        {"nombre": "Item A", "cantidad": 2, "precio": 15.50},
        {"nombre": "Item B", "cantidad": 1, "precio": 50.00},
        {"nombre": "Item C", "cantidad": 4, "precio": 7.25},
    ],
    "total": 2 * 15.50 + 1 * 50.00 + 4 * 7.25,
}

# Generate the PDF
generate_invoice(invoice_data, "Archivo.pdf")
