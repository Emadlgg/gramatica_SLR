class ItemLR0:
    def __init__(self, lhs, rhs, pos_punto):
        self.lhs = lhs
        self.rhs = rhs
        self.pos_punto = pos_punto
    
    def __eq__(self, otro):
        return (self.lhs == otro.lhs and 
                self.rhs == otro.rhs and 
                self.pos_punto == otro.pos_punto)
    
    def __hash__(self):
        return hash((self.lhs, tuple(self.rhs), self.pos_punto))
    
    def __repr__(self):
        rhs_mostrar = self.rhs[:]
        rhs_mostrar.insert(self.pos_punto, "•")
        return f"{self.lhs} → {' '.join(rhs_mostrar)}"
    
    def simbolo_despues_punto(self):
        if self.pos_punto < len(self.rhs):
            return self.rhs[self.pos_punto]
        return None


class Gramatica:
    def __init__(self, producciones):
        self.producciones = producciones
        self.no_terminales = set(producciones.keys())
    
    def obtener_producciones(self, nt):
        return self.producciones.get(nt, [])


def cerradura(items, gramatica):
    conjunto_cerradura = set(items)
    cambiado = True
    
    print("\n  Calculando cerradura...")
    print("  Items iniciales:")
    for item in items:
        print(f"    {item}")
    
    iteracion = 1
    while cambiado:
        cambiado = False
        actual = list(conjunto_cerradura)
        
        for item in actual:
            simbolo = item.simbolo_despues_punto()
            
            if simbolo and simbolo in gramatica.no_terminales:
                for prod in gramatica.obtener_producciones(simbolo):
                    if prod == [] or prod == ["ε"]:
                        nuevo_item = ItemLR0(simbolo, [], 0)
                    else:
                        nuevo_item = ItemLR0(simbolo, list(prod), 0)
                    
                    if nuevo_item not in conjunto_cerradura:
                        print(f"\n  Iteración {iteracion}: Agregando {nuevo_item}")
                        print(f"    desde {item}")
                        conjunto_cerradura.add(nuevo_item)
                        cambiado = True
        iteracion += 1
    
    print(f"\n  Tamaño de cerradura: {len(conjunto_cerradura)} items")
    return sorted(conjunto_cerradura, key=lambda x: (x.lhs, str(x.rhs), x.pos_punto))


def mostrar_cerradura(items, gramatica, titulo=""):
    if titulo:
        print("\n" + "=" * 60)
        print(f"  {titulo}")
        print("=" * 60)
    
    print("\nItems de entrada:")
    for item in items:
        print(f"  {item}")
    
    resultado = cerradura(items, gramatica)
    
    print("\nCerradura completa:")
    for item in resultado:
        marca = "  ← núcleo" if item in items else ""
        print(f"  {item}{marca}")
    
    return resultado


# ============================================================================
# Casos de prueba
# ============================================================================

def probar_gramatica1():
    print("\n" + "=" * 70)
    print("GRAMÁTICA 1: S → SS+ | SS* | a")
    print("=" * 70)
    
    g = Gramatica({
        "S'": [["S"]],
        "S":  [["S", "S", "+"], ["S", "S", "*"], ["a"]]
    })
    
    I0 = [ItemLR0("S'", ["S"], 0)]
    mostrar_cerradura(I0, g, "I0 = CERRADURA({S' → •S})")
    
    I1 = [
        ItemLR0("S'", ["S"], 1),
        ItemLR0("S", ["S", "S", "+"], 1),
        ItemLR0("S", ["S", "S", "*"], 1)
    ]
    mostrar_cerradura(I1, g, "I1 = CERRADURA({S' → S•, S → S•S+, S → S•S*})")
    
    I3 = [
        ItemLR0("S", ["S", "S", "+"], 2),
        ItemLR0("S", ["S", "S", "*"], 2)
    ]
    mostrar_cerradura(I3, g, "I3 = CERRADURA({S → SS•+, S → SS•*})")


def probar_gramatica2():
    print("\n" + "=" * 70)
    print("GRAMÁTICA 2: S → (S) | ε")
    print("=" * 70)
    
    g = Gramatica({
        "S'": [["S"]],
        "S":  [["(", "S", ")"], []]
    })
    
    I0 = [ItemLR0("S'", ["S"], 0)]
    mostrar_cerradura(I0, g, "I0 = CERRADURA({S' → •S})")
    
    I1 = [ItemLR0("S", ["(", "S", ")"], 1)]
    mostrar_cerradura(I1, g, "I1 = CERRADURA({S → (•S)})")


def probar_gramatica3():
    print("\n" + "=" * 70)
    print("GRAMÁTICA 3: S → L, L → aL | a")
    print("=" * 70)
    
    g = Gramatica({
        "S'": [["S"]],
        "S":  [["L"]],
        "L":  [["a", "L"], ["a"]]
    })
    
    I0 = [ItemLR0("S'", ["S"], 0)]
    mostrar_cerradura(I0, g, "I0 = CERRADURA({S' → •S})")
    
    I3 = [
        ItemLR0("L", ["a", "L"], 1),
        ItemLR0("L", ["a"], 1)
    ]
    mostrar_cerradura(I3, g, "I3 = CERRADURA({L → a•L, L → a•})")


def probar_ejemplo_clase():
    print("\n" + "=" * 70)
    print("EJEMPLO DE CLASE: E → E+T | T, T → T*F | F, F → (E) | id")
    print("=" * 70)
    
    g = Gramatica({
        "E'": [["E"]],
        "E":  [["E", "+", "T"], ["T"]],
        "T":  [["T", "*", "F"], ["F"]],
        "F":  [["(", "E", ")"], ["id"]]
    })
    
    I0 = [ItemLR0("E'", ["E"], 0)]
    mostrar_cerradura(I0, g, "I0 = CERRADURA({E' → •E})")


if __name__ == "__main__":
    probar_gramatica1()
    probar_gramatica2()
    probar_gramatica3()
    probar_ejemplo_clase()