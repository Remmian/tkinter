from fpdf import FPDF
import os.path


def getDatasClient():
    home = os.getcwd()
    routeFile = f"{home}/src/products/venta.txt"

    with open(routeFile, "r") as file:
        lines = file.readlines()
        fields = lines[0].split("|")
    return fields
    # fieldPassword = fields[0].split(":")[1].strip()


def addNewLine(text, xposition, yposition, fontzise, fontstyle=''):
    pdf.set_font('Arial', fontstyle, fontzise)
    pdf.ln(yposition)
    pdf.cell(xposition)
    pdf.cell(0, 0, text, 0)


def main():
    global pdf
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_margins(0, 0, 0)

    addNewLine('Detalle de la compra', 50, 2, 28, 'B')

    pdf.line(x1=0, y1=20, x2=230, y2=20)

    # Labels for the products
    # addNewLine("Cliente: ", 10, 20, 16, '')
    # addNewLine("Prenda: ", 10, 20, 16, '')
    # addNewLine("Talla: ", 10, 20, 16, '')
    # addNewLine("Cantidad: ", 10, 20, 16, '')

    labels = ["Cliente: ", "Prenda: ", "Talla: ", "Cantidad: "]
    datas = getDatasClient()
    print(datas)

    for data in datas:
        addNewLine(data, 120, 20, 20, '')

    pdf.output('detalles_compra.pdf', 'F')


if __name__ == '__main__':
    main()
