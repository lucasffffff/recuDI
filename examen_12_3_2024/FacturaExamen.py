from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


class Factura:

    def __init__(self,NOMBRE, numCliente="1", nameCliente="Ana", apellidos="Perez Diz", direccion="Garcia Barbon",
                ciudad="Vigo", provincia="Pontevedra", cp="36214", telf="986456780", pais="España", agComercial="1"):
        self.numCliente = numCliente
        self.nameCliente = nameCliente
        self.apellidos = apellidos
        self.direccion = direccion
        self.ciudad = ciudad
        self.provincia = provincia
        self.cp = cp
        self.telf = telf
        self.pais = pais
        self.agComercial = agComercial



        self.sampleSheet = getSampleStyleSheet()
        self.elementosDoc = []
        # llamamos a los metodos
        self.tabla()

        # construimos el pdf
        self.documento = SimpleDocTemplate(NOMBRE, pagesize=A4)
        self.documento.build(self.elementosDoc)

    def tabla(self):
        elementos = [
            ["Numero cliente", self.numCliente, "Nome Cliente", self.nameCliente],
            ["Apellidos", self.apellidos, "", ""],
            ["Direccion:", self.direccion, "", ""],
            ["Cidade", self.ciudad, "Provincia", self.provincia],
            ["Codigo Postal", self.cp, "Telefono", self.telf],
            ["Pais", self.pais, "Axenta Comercial", self.agComercial]
        ]
        style = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.lightgrey),
            ("BACKGROUND", (2, 0), (2, 0), colors.lightgrey),
            ("BACKGROUND", (2, 3), (2, -1), colors.lightgrey),
        ]

        table = Table(data=elementos, style=style, colWidths=[100,120,100,100])
        self.elementosDoc.append(table)
if __name__ == "__main__":
    factura = Factura()
    print("Factura creada")