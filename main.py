import os
ruta_carpeta = r"c:\Users\meuge\OneDrive\Escritorio\TuModelodeClientes_Robles"
if os.path.exists (ruta_carpeta) : 
     os.system(f'explorer "{ruta_carpeta}"')
else : 
    print ("la carpeta no existe")