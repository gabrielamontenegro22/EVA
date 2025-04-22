def calcular_pago(tipo_contrato, horas_normales, horas_nocturnas, horas_dominicales):
    try:
        horas_normales = int(horas_normales)
        horas_nocturnas = int(horas_nocturnas)
        horas_dominicales = int(horas_dominicales)

        if tipo_contrato not in ["Tiempo Completo", "Medio Tiempo"]:
            return None

        # Nueva validación importante:
        if horas_normales + horas_nocturnas + horas_dominicales > 192:
            return None

        if any(h < 0 or h > 720 for h in [horas_normales, horas_nocturnas, horas_dominicales]):
            return None

        tarifa_hora = 1423500 / 192
        pago_bruto = (horas_normales * tarifa_hora) + (horas_nocturnas * tarifa_hora * 1.35) + (horas_dominicales * tarifa_hora * 1.75)

        descuento_salud = pago_bruto * 0.04
        descuento_pension = pago_bruto * 0.04
        descuento_arl = pago_bruto * 0.0522 if tipo_contrato == "Tiempo Completo" else 0

        total_descuentos = descuento_salud + descuento_pension + descuento_arl
        pago_neto = pago_bruto - total_descuentos

        return {
            "pago_bruto": pago_bruto,
            "descuento_salud": descuento_salud,
            "descuento_pension": descuento_pension,
            "descuento_arl": descuento_arl,
            "total_descuentos": total_descuentos,
            "pago_neto": pago_neto
        }

    except ValueError:
        return None


def solicitar_datos():
    tipo_contrato = input("Ingresa el tipo de contrato (Tiempo Completo o Medio Tiempo): ")
    horas_normales = input("Ingresa las horas normales trabajadas: ")
    horas_nocturnas = input("Ingresa las horas nocturnas trabajadas: ")
    horas_dominicales = input("Ingresa las horas dominicales trabajadas: ")

    resultado = calcular_pago(tipo_contrato, horas_normales, horas_nocturnas, horas_dominicales)

    if resultado:
        resultado_texto = f"""
        Pago Bruto: ${resultado['pago_bruto']:,.2f} COP
        Descuento Salud: ${resultado['descuento_salud']:,.2f} COP
        Descuento Pensión: ${resultado['descuento_pension']:,.2f} COP
        Descuento ARL: ${resultado['descuento_arl']:,.2f} COP
        Total Descuentos: ${resultado['total_descuentos']:,.2f} COP
        Pago Neto: ${resultado['pago_neto']:,.2f} COP
        """
        print("Sueldo del Docente Calculado:")
        print(resultado_texto)
    else:
        print("Error: Por favor, ingrese valores válidos.")


# Ejecutar la función
if __name__ == "__main__":
    solicitar_datos()
