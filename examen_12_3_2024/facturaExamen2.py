from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


class Factura2:

    def __init__(self, modeloTabla):
        self.modeloTabla = modeloTabla
        for elementos in self.modeloTabla:
            self.numCliente = elementos[0]
            self.nameCliente = elementos[1]
            self.apellidos = elementos[2]
            self.direccion = elementos[3]
            self.ciudad = elementos[4]
            self.provincia = elementos[5]
            self.cp = elementos[6]
            self.telf = elementos[7]
            self.pais = elementos[8]
            self.agComercial = elementos[9]



        self.sampleSheet = getSampleStyleSheet()
        self.elementosDoc = []
        # llamamos a los metodos
        self.tabla()

        # construimos el pdf
        self.documento = SimpleDocTemplate("factura.pdf", pagesize=A4)
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

        table = Table(data=elementos, style=style, colWidths=100)
        self.elementosDoc.append(table)
if __name__ == "__main__":
    factura = Factura()
    print("Factura creada")