import tensorflow as tf
import serial

# Configuración de la comunicación serial
arduino_port = 'COM6'  # Cambiar esto al puerto correspondiente de Arduino
arduino_baud = 9600
ser = serial.Serial(arduino_port, arduino_baud)

# Función para recibir datos del Arduino
def recibir_datos_serial():
    dato = ser.readline().decode().strip()
    try:
        distancia = float(dato)
        return distancia
    except ValueError:
        return None

# Cargar los datos para entrenar la neurona
datos_entrenamiento = []

# Leer datos del Arduino y almacenarlos en la lista de entrenamiento
while len(datos_entrenamiento) < 100:  # Por ejemplo, recoger 100 muestras para entrenar
    distancia = recibir_datos_serial()
    if distancia is not None:
        datos_entrenamiento.append(distancia)

# Normalizar los datos en el rango [0, 1]
datos_entrenamiento = [(dato - 5) / (30 - 5) for dato in datos_entrenamiento]

# Crear los datos de entrada y salida esperados
entrada_entrenamiento = datos_entrenamiento[:-1]
salida_entrenamiento = datos_entrenamiento[1:]

# Definir el modelo de la neurona
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilar el modelo
modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Entrenar el modelo
modelo.fit(entrada_entrenamiento, salida_entrenamiento, epochs=100)

# Obtener el último valor del entrenamiento
ultimo_dato = datos_entrenamiento[-1]

# Realizar una predicción con el modelo entrenado
siguiente_valor = modelo.predict([[ultimo_dato]])

# Escalar la predicción al rango [0, 180] para controlar el servo
siguiente_valor = int(siguiente_valor[0][0] * 180)

# Enviar el valor al Arduino para controlar el servo
ser.write(str(siguiente_valor).encode())

# Cerrar la comunicación serial
ser.close()