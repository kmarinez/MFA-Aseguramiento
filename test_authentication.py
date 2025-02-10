import pytest
from authentication import AuthSystem

@pytest.fixture
def auth_system():
    return AuthSystem()

# Prueba 1: Autenticación biométrica exitosa
def test_auth_biometrica_exitosa(auth_system):
    resultado = auth_system.autenticar_biometria(usuario='usuario_prueba', metodo='huella')
    assert resultado == "Autenticación exitosa", "La autenticación biométrica debería ser exitosa."

# Prueba 2: Autenticación biométrica fallida
def test_auth_biometrica_fallida(auth_system):
    resultado = auth_system.autenticar_biometria(usuario='usuario_prueba', metodo='huella_incorrecta')
    assert resultado == "Autenticación fallida", "El sistema debería rechazar huellas incorrectas."

# Prueba 3: Código dinámico generado correctamente
def test_codigo_dinamico_generado(auth_system):
    codigo = auth_system.generar_codigo_dinamico(usuario='usuario_prueba')
    assert len(str(codigo)) == 6, "El código dinámico debe tener 6 dígitos."

# Prueba 4: Código dinámico expirado
def test_codigo_dinamico_expirado(auth_system):
    auth_system.generar_codigo_dinamico(usuario='usuario_prueba')
    resultado = auth_system.validar_codigo_dinamico(usuario='usuario_prueba', codigo='123456', tiempo_expirado=True)
    assert resultado == "Código expirado", "El sistema debe rechazar códigos expirados."

# Prueba 5: Código dinámico incorrecto
def test_codigo_dinamico_incorrecto(auth_system):
    auth_system.generar_codigo_dinamico(usuario='usuario_prueba')
    resultado = auth_system.validar_codigo_dinamico(usuario='usuario_prueba', codigo='000000')
    assert resultado == "Código incorrecto", "El sistema debe rechazar códigos incorrectos."

if __name__ == "__main__":
    pytest.main()