#Author-Bryan McCaffery
#Description-Make simple ascending tower\t\t\t\t

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct
        #Make a collection to extrude all of them 
        profs = adsk.core.ObjectCollection.create()
        # Get the root component of the active design.
        rootComp = design.rootComponent
        extrudes = rootComp.features.extrudeFeatures
        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        #Make ten squares on the bottom
        z = 0
        i = 0
        for x in range(25):
            lines.addTwoPointRectangle(adsk.core.Point3D.create(i,z,0), adsk.core.Point3D.create(i+1,z+1,0))
            if i >= 4:
                z += 1
                i = 0
            else:
                i += 1
        j = 1
        #Extrude those ten squares
        for prof in sketch.profiles:
            extrude_input = rootComp.features.extrudeFeatures.createInput(prof,adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setDistanceExtent(False,adsk.core.ValueInput.createByReal(j))
            block = rootComp.features.extrudeFeatures.add(extrude_input)
            j += 0.5
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
