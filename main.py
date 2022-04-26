from reportlab.lib.pagesizes import *
from reportlab.lib.colors import *
from reportlab.lib.units import cm


class Settings:
    def __init__(self):
        self.filename = "test"  # no need to assign a file extention
        self.size = (575.0, 767.0)

        # Minor line setting:
        self.colorMinor = pink  # check the default setting below
        self.lineWidthMinor = 1


class canvasSpec:
    def __init__(self):
        self.filename = "test"
        self.size = (575.0, 767.0)
        self.width = 575.0
        self.height = 767.0
        self.xgap = 0
        self.ygap = 0
        self.xlist = []
        self.ylist = []
        self.xStart = 0
        self.yStart = 0


def draw(object, canvas, color, lineWidth):
    def xylist(setting):
        xs = []
        ys = []

        for i in range(int(object.width)):
            xs.append(i*10)

        for i in range(int(object.height)):
            ys.append(i*10)

        return xs, ys


    def gridB(object, canvas, color, lineWidth, xlist, ylist):
        color = HexColor('#bcbcbc')
        canvas.setStrokeColor(color)
        canvas.setLineWidth(0.01 * cm)
        canvas.grid(xlist, ylist)

    xlist, ylist = xylist(canvas)
    gridB(object, canvas, color, lineWidth, xlist, ylist)


from reportlab.pdfgen import canvas

# Create a canvas
cSpec = canvasSpec()
c = canvas.Canvas(cSpec.filename + ".pdf", cSpec.size)

# Main draw func with inputs (object,detailTF,canvas,color,lineWidth)
draw(cSpec, c, pink, 1)

c.showPage()
c.save()
