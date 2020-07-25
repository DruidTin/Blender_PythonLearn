import bpy

# Setting 設定
name = 'Gridtasric'
rows = 5
columns = 10
size = 1

#建立網面函數 function
def face(column,row):

    return(column * rows + row,
            (column + 1) * rows + row,
            (column + 1) * rows + 1 + row,
            column * rows + 1 + row)


# Looping to create the grid
verts = [(x,y,0) for x in range(columns) for y in range(rows)]
faces = [face(x,y) for x in range(columns-1) for y in range(rows -1)]

#Create Mesh Datablock 建立網面數據塊
mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts,[],faces)

#Create Object and link to scene
obj = bpy.data.objects.new(name,mesh)
bpy.context.scene.collection.objects.link(obj)

#Select the Object
bpy.context.view_layer.objects.active = obj
