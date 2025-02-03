from ArbolBinario import ArbolBinario

arbol = ArbolBinario(20)

arbol.agregar(10)
arbol.agregar(5)
arbol.agregar(15)
arbol.agregar(30)
arbol.agregar(35)

# resultado de arbol inorden:
# 5, 10, 15, 20, 30, 35
arbol.inorden()

# resultado arbol preorden:
# 20, 10, 5, 15, 30, 35
arbol.preorden()

# resultado arbol postorden:
# 5, 15, 10, 35, 30, 20
arbol.postorden()




if arbol.buscar(15):
    print("\nEl dato 15 se encuentra en el arbol")

if not arbol.buscar(25):
    print("\nEl dato 25 no se encuentra en el arbol")




