
from datetime import datetime
import math

class AnalizadorNumericoAvanzado:

    def __init__(self):
        self.ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"
        self.VOCALES = "aeiou"

    def evaluar_signo(self, numero: int) -> str:
        if numero > 0:
            return "Positivo"
        elif numero < 0:
            return "Negativo"
        return "Cero"

    def evaluar_paridad(self, numero: int) -> str:
        return "Par" if numero % 2 == 0 else "Impar"

    def es_fibonacci(self, numero: int) -> bool:
        if numero < 0:
            return False
        
        def es_cuadrado_perfecto(x):
            s = int(math.isqrt(x))
            return s * s == x
        
        return es_cuadrado_perfecto(5 * numero**2 + 4) or es_cuadrado_perfecto(5 * numero**2 - 4)

    def es_primo(self, numero: int) -> bool:
        if numero <= 1:
            return False
        for i in range(2, int(math.isqrt(numero)) + 1):
            if numero % i == 0:
                return False
        return True

    def sumar_intermedios(self, a: int, b: int) -> int:
        inicio, fin = min(a, b), max(a, b)
        return sum(range(inicio + 1, fin))

    def transformar_segun_paridad(self, numero: int) -> int:
        if numero % 2 == 0:
            return numero ** 3
        else:
            return numero ** 2

    def analizar_mes(self, mes: str):
        mes_clean = mes.lower()
        vocales_encontradas = [c for c in mes_clean if c in self.VOCALES]
        consonantes_encontradas = [c for c in mes_clean if c in self.ABECEDARIO and c not in self.VOCALES]
        
        posiciones = {char: self.ABECEDARIO.index(char) + 1 for char in mes_clean if char in self.ABECEDARIO}
        
        return vocales_encontradas, consonantes_encontradas, posiciones

    def procesar_cadena_estudiante(self, cadena: str):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        
        cadena_lower = cadena.lower()
        mes_detectado = None
        
        for mes in meses:
            if mes in cadena_lower:
                mes_detectado = mes
                break
        
        if not mes_detectado:
            return None, "No se encontró un mes válido en la cadena."

        partes_numericas = cadena_lower.split(mes_detectado)
        cadena_solonumeros = "".join(partes_numericas)
        
        try:
            numero_extraido = int(cadena_solonumeros)
        except ValueError:
            numero_extraido = 0

        return mes_detectado, numero_extraido

    def ejecutar_analisis_completo(self):
        print("=" * 65)
        print(" SISTEMA INTEGRADO DE ANÁLISIS NUMÉRICO Y LÉXICO ")
        print("=" * 65)
        
        print("\n¡Un cordial saludo! Le damos la bienvenida al sistema de evaluación.")
        cadena_input = input("¿Tendría la amabilidad de ingresar la cadena (ejemplo: 1enero2000100032300)?: ")

        mes, numero_principal = self.procesar_cadena_estudiante(cadena_input)

        if not mes:
            print(f"\nDisculpe las molestias. Error de procesamiento: {numero_principal}")
            return

        print("\n" + "-" * 65)
        print(f" RESULTADOS DE EXTRACCIÓN ")
        print("-" * 65)
        print(f"• Mes extraído: {mes.capitalize()}")
        print(f"• Número resultante evaluado: {numero_principal}")

        print("\n" + "-" * 65)
        print(f" EVALUACIÓN MATEMÁTICA DEL NÚMERO ({numero_principal}) ")
        print("-" * 65)
        print(f"1. Determinación de Signo: {self.evaluar_signo(numero_principal)}")
        print(f"2. Determinación de Paridad: {self.evaluar_paridad(numero_principal)}")
        print(f"3. ¿Pertenece a Fibonacci?: {'Sí' if self.es_fibonacci(numero_principal) else 'No'}")
        print(f"4. ¿Es Número Primo?: {'Sí' if self.es_primo(numero_principal) else 'No'}")

        segundo_numero = 10
        suma_int = self.sumar_intermedios(numero_principal, segundo_numero)
        print(f"5. Suma intermedios (con {segundo_numero}): {suma_int}")

        potencia = self.transformar_segun_paridad(numero_principal)
        print(f"6. Transformación exponencial: {potencia}")

        vocales, consonantes, posiciones = self.analizar_mes(mes)
        
        print("\n" + "-" * 65)
        print(f" ANÁLISIS LÉXICO DEL MES ({mes.upper()}) ")
        print("-" * 65)
        print(f"9a. Vocales presentes: {', '.join(set(vocales))}")
        print(f"9b. Consonantes presentes: {', '.join(set(consonantes))}")
        print("10. Posición de las letras en el abecedario:")
        for letra, pos in posiciones.items():
            print(f" - Letra '{letra.upper()}': posición {pos}")

        print("\n" + "=" * 65)
        print("El análisis ha finalizado exitosamente. ¡Que tenga un excelente día!")
        print("=" * 65)


if __name__ == "__main__":
    app = AnalizadorNumericoAvanzado()
    app.ejecutar_analisis_completo()

    
    
