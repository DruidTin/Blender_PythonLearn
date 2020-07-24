import bpy

# Setting 設定
name = 'Gridtasric'
rows = 5
columns = 10
verts = [(x,0,0) for x in range(columns)]
faces = []

#Create Mesh Datablock
mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts,[],faces)

#Create Object and link to scene
obj = bpy.data.objects.new(name,mesh)
bpy.context.scene.collection.objects.link(obj)

#Select the Object
bpy.context.view_layer.objects.active = obj
#obj.select_get = True
