import getpass
import time
import prman

def drawScene(ri, zpos=0):
    ri.Attribute("identifier", {"name": "straw"})
    ri.TransformBegin()
    ri.Translate(0, 0, zpos + 0.1)
    ri.Rotate(90, 1, 0, 0)
    ri.Scale(0.1, 0.1, 200)
    ri.Torus(0.5, 0.01, 0, 360, 360)
    ri.TransformEnd()
    ri.AttributeEnd()


def main(
    filename,
    shadingrate=10,
    pixelvariance=0.1,
    fov=45,
    width=2048,
    height=2048,
    integrator="PxrPathTracer",
    integratorParams={},
):
    ri = prman.Ri()
    ri.Begin(filename)
    ri.Display("rgb.exr", "it", "rgba")
    ri.Format(width, height, 1)

    #setup raytrace
    ri.Hider("raytrace", {"int incremental": [1]})
    ri.ShadingRate(shadingrate)
    ri.PixelVariance(pixelvariance)
    ri.Integrator(integrator, integratorParams)
    ri.Projection(ri.PERSPECTIVE, {ri.FOV: fov})

    #translate cam
    





file_name = "straw.rib"

ri.Begin(file_name)
ri.ArchiveRecord(ri.COMMENT, "start our world")
ri.Display("straw.exr", "it", "rgba")
ri.Format(2048, 2048, 1)
ri.Projection(ri.PERSPECTIVE, {ri.FOV:45})


ri.WorldBegin()


ri.ArchiveRecord(ri.COMMENT, "end our world")
ri.WorldEnd()

ri.End()