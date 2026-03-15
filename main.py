def main():

    productos = [
        {"nombre": "C4 Azul", "tipo": "Pre-entreno", "proveedor": "Cellucor", "vencimiento": "12/2026", "cantidad": 10},
        {"nombre": "C4 Rojo", "tipo": "Pre-entreno", "proveedor": "Cellucor", "vencimiento": "12/2026", "cantidad": 10},
        {"nombre": "Monster Energy Mango Loco", "tipo": "Energética", "proveedor": "Monster", "vencimiento": "10/2025",
         "cantidad": 24},
        {"nombre": "Monster Energy Pipeline Punch", "tipo": "Energética", "proveedor": "Monster",
         "vencimiento": "10/2025", "cantidad": 24},
        {"nombre": "Monster Energy Azul", "tipo": "Energética", "proveedor": "Monster", "vencimiento": "10/2025",
         "cantidad": 24},
        {"nombre": "Monster Energy Juice Naranja", "tipo": "Energética", "proveedor": "Monster",
         "vencimiento": "11/2025", "cantidad": 24},
        {"nombre": "Monster Energy Blanca Ultra", "tipo": "Energética", "proveedor": "Monster",
         "vencimiento": "11/2025", "cantidad": 24},
        {"nombre": "Monster Energy Original", "tipo": "Energética", "proveedor": "Monster", "vencimiento": "12/2025",
         "cantidad": 24},
        {"nombre": "Monster Energy Original Zero Azúcar", "tipo": "Energética", "proveedor": "Monster",
         "vencimiento": "12/2025", "cantidad": 24},
        {"nombre": "Sobre Proteína Personal", "tipo": "Proteína", "proveedor": "Genérico", "vencimiento": "05/2026",
         "cantidad": 50},
        {"nombre": "Electrolit Uva", "tipo": "Hidratante", "proveedor": "PiSA", "vencimiento": "08/2026",
         "cantidad": 20},
        {"nombre": "Electrolit Maracuyá", "tipo": "Hidratante", "proveedor": "PiSA", "vencimiento": "08/2026",
         "cantidad": 20},
        {"nombre": "Electrolit Fresa Kiwi", "tipo": "Hidratante", "proveedor": "PiSA", "vencimiento": "08/2026",
         "cantidad": 20},
        {"nombre": "Gatorade Azul", "tipo": "Hidratante", "proveedor": "PepsiCo", "vencimiento": "09/2026",
         "cantidad": 30},
        {"nombre": "Gatorade Morado", "tipo": "Hidratante", "proveedor": "PepsiCo", "vencimiento": "09/2026",
         "cantidad": 30},
        {"nombre": "Gatorade Rojo", "tipo": "Hidratante", "proveedor": "PepsiCo", "vencimiento": "09/2026",
         "cantidad": 30},
        {"nombre": "Gatorade Naranja", "tipo": "Hidratante", "proveedor": "PepsiCo", "vencimiento": "09/2026",
         "cantidad": 30},
        {"nombre": "Leche Proteína Chocolate", "tipo": "Proteína", "proveedor": "Dos Pinos", "vencimiento": "06/2026",
         "cantidad": 15},
        {"nombre": "Leche Proteína Vainilla", "tipo": "Proteína", "proveedor": "Dos Pinos", "vencimiento": "06/2026",
         "cantidad": 15},
        {"nombre": "Leche Proteína Fresa", "tipo": "Proteína", "proveedor": "Dos Pinos", "vencimiento": "06/2026",
         "cantidad": 15}
    ]

    while True:
        print("\n" + "=" * 50)
        print("   SISTEMA DE INVENTARIO - BENESSERE GYM")
        print("=" * 50)
        print("1. Registrar nuevo suplemento")
        print("2. Registrar entrada de stock (Sumar a inventario)")
        print("3. Registrar salida/Facturación [En desarrollo]")
        print("4. Mostrar inventario actual")
        print("5. Salir del sistema")
        print("=" * 50)

        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("\n[ERROR] Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            print("\n--- REGISTRAR NUEVO SUPLEMENTO ---")
            nombre = input("Nombre del producto: ").strip().title()
            tipo = input("Tipo (ej. Proteína, Pre-entreno): ").strip()
            proveedor = input("Proveedor: ").strip()
            vencimiento = input("Fecha de vencimiento (DD/MM/AAAA): ").strip()

            try:
                cantidad = int(input("Cantidad inicial a ingresar: "))
                if cantidad < 0:
                    print("[ERROR] La cantidad no puede ser negativa.")
                    continue
            except ValueError:
                print("[ERROR] La cantidad debe ser un número entero.")
                continue

            nuevo_producto = {
                "nombre": nombre,
                "tipo": tipo,
                "proveedor": proveedor,
                "vencimiento": vencimiento,
                "cantidad": cantidad
            }
            productos.append(nuevo_producto)
            print(f"\n¡Éxito! El producto '{nombre}' ha sido registrado.")

        elif opcion == 2:
            print("\n--- ENTRADA DE PRODUCTO (ACTUALIZAR STOCK) ---")
            buscar_nombre = input("Ingrese el nombre exacto del producto (ej. C4 Azul): ").strip().title()
            encontrado = False

            for producto in productos:

                if producto["nombre"].lower() == buscar_nombre.lower():
                    encontrado = True
                    print(f"Stock actual de {producto['nombre']}: {producto['cantidad']} unidades.")
                    try:
                        cantidad_entrada = int(input("Ingrese la cantidad a sumar: "))
                        if cantidad_entrada < 0:
                            print("[ERROR] No puede ingresar cantidades negativas.")
                            break

                        producto["cantidad"] += cantidad_entrada
                        print(f"¡Éxito! Nuevo stock de {producto['nombre']}: {producto['cantidad']}")
                    except ValueError:
                        print("[ERROR] Debe ingresar un número entero.")
                    break

            if not encontrado:
                print(f"[ERROR] El producto '{buscar_nombre}' no existe en el inventario.")

        elif opcion == 3:
            print("\n[Aviso: Módulo de facturación en desarrollo para entrega final...]")

        elif opcion == 4:
            print("\n--- INVENTARIO ACTUAL DE BENESSERE GYM ---")

            print(f"{'NOMBRE':<35} | {'TIPO':<15} | {'CANTIDAD':<10} | {'VENCIMIENTO'}")
            print("-" * 80)
            for p in productos:
                print(f"{p['nombre']:<35} | {p['tipo']:<15} | {p['cantidad']:<10} | {p['vencimiento']}")

        elif opcion == 5:
            print("\nCerrando el sistema de inventario... ¡Hasta luego!")
            break

        else:
            print("\n[ERROR] Opción no válida. Por favor seleccione un número del 1 al 5.")


if __name__ == "__main__":
    main()