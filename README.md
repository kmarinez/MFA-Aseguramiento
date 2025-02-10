# Documentación de Pruebas Unitarias

## Casos de Uso Cubiertos
1. **Autenticación biométrica** (huella digital y reconocimiento facial).
2. **Autenticación con código dinámico** (generación y validación de códigos temporales).

## Descripción de las Pruebas Unitarias

### 1. Prueba de Autenticación Biométrica Exitosa
- **Propósito:** Verificar que la autenticación mediante huella digital o reconocimiento facial funcione correctamente.
- **Relación con el caso de uso:** Asegura que los usuarios puedan acceder a sus cuentas utilizando autenticación biométrica sin necesidad de contraseñas.
- **Entrada esperada:** Usuario válido y método biométrico correcto.
- **Resultado esperado:** `"Autenticación exitosa"`.

### 2. Prueba de Autenticación Biométrica Fallida
- **Propósito:** Validar que el sistema rechace una autenticación biométrica incorrecta.
- **Relación con el caso de uso:** Simula un intento fallido para verificar la robustez del sistema.
- **Entrada esperada:** Usuario válido con un método biométrico incorrecto.
- **Resultado esperado:** `"Autenticación fallida"`.

### 3. Prueba de Generación de Código Dinámico
- **Propósito:** Comprobar que el sistema genera un código aleatorio de 6 dígitos correctamente.
- **Relación con el caso de uso:** Asegura que los usuarios reciban códigos únicos para la autenticación.
- **Entrada esperada:** Solicitud de código dinámico por un usuario registrado.
- **Resultado esperado:** `Código de 6 dígitos generado correctamente`.

### 4. Prueba de Código Dinámico Expirado
- **Propósito:** Validar que el sistema rechace códigos dinámicos expirados.
- **Relación con el caso de uso:** Asegura que los códigos no puedan ser reutilizados después de su tiempo de validez.
- **Entrada esperada:** Código dinámico generado pero ya expirado.
- **Resultado esperado:** `"Código expirado"`.

### 5. Prueba de Código Dinámico Incorrecto
- **Propósito:** Verificar que el sistema rechace códigos incorrectos.
- **Relación con el caso de uso:** Garantiza que solo los códigos generados sean aceptados.
- **Entrada esperada:** Código dinámico incorrecto ingresado.
- **Resultado esperado:** `"Código incorrecto"`.

Katerin Mariñez 22-1131

