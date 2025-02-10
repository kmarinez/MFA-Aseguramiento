import random
import time

class AuthSystem:
    def __init__(self):
        self.codigos = {}

    def autenticar_biometria(self, usuario, metodo):
        if metodo in ["huella", "rostro"]:
            return "Autenticación exitosa"
        return "Autenticación fallida"

    def generar_codigo_dinamico(self, usuario):
        codigo = random.randint(100000, 999999)  # Código de 6 dígitos
        self.codigos[usuario] = {"codigo": codigo, "timestamp": time.time()}
        return codigo

    def validar_codigo_dinamico(self, usuario, codigo, tiempo_expirado=False):
        if usuario not in self.codigos:
            return "Código incorrecto"

        datos_codigo = self.codigos[usuario]
        if tiempo_expirado or (time.time() - datos_codigo["timestamp"] > 60):
            return "Código expirado"

        if str(datos_codigo["codigo"]) == str(codigo):
            return "Código válido"
        return "Código incorrecto"