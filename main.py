from reportlab.lib.colors import *
from reportlab.lib.units import cm


class canvasSpec:
    def __init__(self):
        self.filename = "myreport"
        self.size = (575.0, 767.0)
        self.width = 575.0
        self.height = 767.0
        self.xgap = 0
        self.ygap = 0
        self.xlist = []
        self.ylist = []
        self.xStart = 0
        self.yStart = 0


def draw(object, canvas, color):
    def xylist():
        xs = []
        ys = []

        for i in range(int(object.width)):
            xs.append(i*10)

        for i in range(int(object.height)):
            ys.append(i*10)

        return xs, ys


    def gridB(canvas, color, xlist, ylist):
        color = HexColor('#bcbcbc')
        canvas.setStrokeColor(color)
        canvas.setLineWidth(0.01 * cm)
        canvas.grid(xlist, ylist)

    xlist, ylist = xylist()
    gridB(canvas, color, xlist, ylist)


from reportlab.pdfgen import canvas

# Create a canvas
cSpec = canvasSpec()
c = canvas.Canvas(cSpec.filename + ".pdf", cSpec.size)

# Main draw func with inputs (object,detailTF,canvas,color,lineWidth)
draw(cSpec, c, pink)

c.showPage()
c.save()
