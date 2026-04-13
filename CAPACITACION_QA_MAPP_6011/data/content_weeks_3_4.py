"""Training content for Weeks 3 and 4.

Week 3: Ajustes de Inventario - Parte 2
Week 4: Gestión de Inventario
"""

WEEK_3 = {
    "semana": 3,
    "titulo": "Ajustes de Inventario - Parte 2",
    "descripcion": "Ajustes avanzados: devoluciones y ajustes especiales de inventario.",
    "modulos": [
        {
            "id": "ajuste_12",
            "nombre": "Ajuste 12 - Devolución a Proveedor",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Conocer el proceso de devolución al proveedor",
                "Documentar correctamente la devolución",
                "Ejecutar el Ajuste 12 en el sistema",
                "Coordinar la logística inversa correctamente",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Ajuste 12?",
                    "texto": "El Ajuste 12 se utiliza cuando la mercadería se devuelve al proveedor por problemas de calidad, error en el despacho, o acuerdos comerciales previos. Es un ajuste negativo que registra la salida del inventario hacia el proveedor de origen.",
                },
                {
                    "titulo": "Causas de devolución",
                    "texto": "Se aplica Ajuste 12 cuando:\n• Producto recibido con defectos de calidad\n• Proveedor despacha producto diferente al pedido\n• Exceso de stock por error de orden de compra\n• Producto sin autoridad sanitaria o fuera de especificación\n• Acuerdo comercial de devolución pactado con el proveedor",
                },
                {
                    "titulo": "Proceso de devolución",
                    "texto": "1. Identificar y segregar el producto a devolver\n2. Generar nota de crédito o acuerdo de devolución con el proveedor\n3. Coordinar logística inversa (transporte de retorno)\n4. Preparar documentación: guía de despacho, acta de devolución\n5. Registrar Ajuste 12 en el sistema antes del despacho\n6. Despachar la mercadería y archivar documentación",
                },
                {
                    "titulo": "Diferencias con otros ajustes",
                    "texto": "Comparación:\n• Ajuste 4: Daño interno, sin devolución al proveedor\n• Ajuste 10: Vencimiento, producto se destruye o dona\n• Ajuste 12: Devolución al proveedor, genera nota de crédito\n\nEl Ajuste 12 es el único que permite recuperar el valor del producto.",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿En qué caso se aplica el Ajuste 12?",
                    "opciones": [
                        "Producto dañado internamente",
                        "Devolución de mercadería al proveedor",
                        "Donación de productos",
                        "Traspaso entre CDs",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El Ajuste 12 es para la logística inversa: devolver mercadería al proveedor.",
                },
                {
                    "pregunta": "¿Qué documento financiero se genera asociado al Ajuste 12?",
                    "opciones": [
                        "Una factura de venta",
                        "Una nota de crédito del proveedor",
                        "Un bono de descuento",
                        "No genera documentos financieros",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La devolución al proveedor genera una nota de crédito que permite recuperar el valor del producto.",
                },
                {
                    "pregunta": "¿Cuál es la diferencia clave entre Ajuste 4 y Ajuste 12?",
                    "opciones": [
                        "El Ajuste 4 es para secos y el 12 para refrigerados",
                        "El Ajuste 4 registra daño interno; el 12 registra devolución al proveedor",
                        "No hay diferencia, son iguales",
                        "El Ajuste 12 aumenta el stock",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El Ajuste 4 da de baja por daño interno sin recuperación; el 12 devuelve al proveedor y genera nota de crédito.",
                },
                {
                    "pregunta": "¿Cuándo se debe registrar el Ajuste 12 en el sistema?",
                    "opciones": [
                        "Después de que el proveedor confirme la recepción",
                        "Antes de despachar la mercadería al proveedor",
                        "Solo cuando el proveedor emite la nota de crédito",
                        "Al final del mes en el cierre de inventario",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El ajuste debe registrarse antes del despacho para que el sistema refleje correctamente la salida del inventario.",
                },
            ],
            "practica": "Simular una devolución al proveedor: preparar el acta de devolución, la guía de despacho, registrar el Ajuste 12 en sistema de práctica y completar toda la documentación requerida.",
        },
        {
            "id": "ajuste_27",
            "nombre": "Ajuste 27 - Ajuste de Inventario Positivo",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Entender cuándo se genera un ajuste positivo",
                "Ejecutar el Ajuste 27 con evidencia",
                "Comprender el impacto en el inventario",
                "Investigar la causa raíz del sobrante",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Ajuste 27?",
                    "texto": "El Ajuste 27 se aplica cuando se encuentra mercadería que no estaba registrada en el sistema (sobrante). Aumenta el inventario sistémico para reflejar la realidad física. Aunque parece positivo, siempre debe investigarse la causa raíz.",
                },
                {
                    "titulo": "Causas comunes de sobrante",
                    "texto": "Los sobrantes pueden tener diversas causas:\n• Error en recepción previa (se recibió de más sin registrar)\n• Devolución no registrada al inventario\n• Error en picking (se dejó más de lo que se debió despachar)\n• Producto de otro CD que llegó sin traspaso\n• Error en conteo anterior",
                },
                {
                    "titulo": "Proceso de aplicación",
                    "texto": "1. Identificar el sobrante durante un conteo o revisión\n2. Verificar que realmente no está registrado en el sistema\n3. Investigar la causa raíz del sobrante\n4. Documentar hallazgo con fotos\n5. Aplicar Ajuste 27 con la cantidad exacta encontrada\n6. Obtener autorización del supervisor\n7. Registrar en informe de ajustes de inventario",
                },
                {
                    "titulo": "Controles necesarios",
                    "texto": "Los ajustes positivos también requieren control:\n• Documentación de la fuente del producto (de dónde viene)\n• Autorización supervisora requerida\n• Investigación de causa raíz para evitar recurrencia\n• Para montos significativos, requiere aprobación adicional\n• Registro de todos los casos para análisis mensual",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué efecto tiene el Ajuste 27 en el inventario?",
                    "opciones": [
                        "Lo disminuye",
                        "Lo aumenta para reflejar sobrante encontrado",
                        "No lo modifica",
                        "Lo bloquea temporalmente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El Ajuste 27 es positivo: se agrega al sistema lo que se encontró físicamente de más.",
                },
                {
                    "pregunta": "¿Siempre que hay un sobrante es una buena noticia para el inventario?",
                    "opciones": [
                        "Sí, más stock siempre es positivo",
                        "No, siempre debe investigarse la causa raíz del sobrante",
                        "Depende del valor del producto",
                        "Sí, si el valor es bajo no importa investigar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Un sobrante indica que algo falló en un proceso anterior. Investigar evita que se repita.",
                },
                {
                    "pregunta": "¿Cuál puede ser la causa de un sobrante de inventario?",
                    "opciones": [
                        "Personal altamente capacitado",
                        "Devolución no registrada al inventario previamente",
                        "Uso correcto del sistema WMS",
                        "Control estricto de recepciones",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Una devolución que no se registró puede generar sobrante visible en el próximo conteo.",
                },
                {
                    "pregunta": "¿Qué se debe hacer ANTES de aplicar el Ajuste 27?",
                    "opciones": [
                        "Aplicar directamente sin investigar",
                        "Verificar que el producto no esté registrado e investigar la causa raíz",
                        "Donar el sobrante inmediatamente",
                        "Devolver al proveedor sin documentar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre verificar en el sistema y entender el origen del sobrante antes de hacer el ajuste.",
                },
            ],
            "practica": "Durante un conteo, identificar sobrantes en al menos 3 ubicaciones, investigar posibles causas, documentar con fotos y practicar el registro del ajuste positivo con todos los campos requeridos.",
        },
        {
            "id": "ajuste_28",
            "nombre": "Ajuste 28 - Ajuste de Inventario Negativo",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Entender cuándo se genera un ajuste negativo",
                "Ejecutar el Ajuste 28 con la documentación requerida",
                "Conocer los controles y autorizaciones necesarias",
                "Analizar la causa raíz de los faltantes",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Ajuste 28?",
                    "texto": "El Ajuste 28 se aplica cuando el inventario físico es menor que el sistémico (faltante). Disminuye el inventario del sistema para reflejar la realidad. Es el ajuste que más atención y control requiere, ya que representa una pérdida para la empresa.",
                },
                {
                    "titulo": "Causas comunes de faltante",
                    "texto": "Los faltantes pueden originarse por:\n• Pérdida desconocida (robo, merma no registrada)\n• Error en conteos anteriores\n• Despacho mayor al registrado\n• Diferencias en recepción no detectadas en el momento\n• Movimientos sin registro en el sistema",
                },
                {
                    "titulo": "Controles y autorizaciones",
                    "texto": "Los ajustes negativos requieren mayor control ya que representan una pérdida:\n• Investigación obligatoria de causa raíz\n• Doble verificación física del faltante\n• Autorización del supervisor de turno\n• Para montos altos: aprobación del jefe de área\n• Registro detallado en informe de merma desconocida",
                },
                {
                    "titulo": "Análisis y seguimiento",
                    "texto": "Después del ajuste:\n• Registrar en el informe de merma desconocida\n• Analizar el patrón de faltantes (tipo de producto, horario, zona)\n• Implementar controles preventivos si hay recurrencia\n• Reportar a seguridad si se sospecha robo\n• Presentar análisis mensual de ajustes negativos a la jefatura",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Por qué los ajustes negativos requieren mayor control?",
                    "opciones": [
                        "Porque son más frecuentes",
                        "Porque representan una pérdida económica para la empresa",
                        "Porque son más fáciles de hacer",
                        "No requieren mayor control que los positivos",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los faltantes representan pérdida económica real y deben ser investigados para identificar la causa.",
                },
                {
                    "pregunta": "¿Qué se debe hacer ANTES de aplicar un Ajuste 28?",
                    "opciones": [
                        "Aplicar el ajuste directamente para cuadrar el inventario",
                        "Hacer doble verificación física e investigar la causa del faltante",
                        "Notificar al proveedor inmediatamente",
                        "Esperar hasta el próximo inventario anual",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Antes de ajustar, siempre verificar dos veces que el producto realmente no existe en el CD.",
                },
                {
                    "pregunta": "Si se detectan faltantes recurrentes en el mismo producto/zona, ¿qué se debe hacer?",
                    "opciones": [
                        "Solo seguir haciendo ajustes 28 cada vez",
                        "Analizar el patrón, reportar a seguridad si se sospecha robo e implementar controles",
                        "Ignorarlos si el monto es bajo",
                        "Cambiar el código del producto",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los faltantes recurrentes indican un problema sistémico que debe investigarse y resolverse.",
                },
                {
                    "pregunta": "¿Dónde se registran los faltantes de causa desconocida?",
                    "opciones": [
                        "No se registran, se manejan de forma verbal",
                        "En el informe de merma desconocida con análisis mensual",
                        "Solo en el ajuste del sistema",
                        "Solo si el supervisor lo pide explícitamente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los faltantes desconocidos deben registrarse en el informe de merma para análisis y control mensual.",
                },
            ],
            "practica": "Analizar un caso de faltante de inventario en 3 ubicaciones, investigar las posibles causas, documentar el Ajuste 28 con evidencia requerida y preparar un mini-informe de merma desconocida.",
        },
    ],
}

WEEK_4 = {
    "semana": 4,
    "titulo": "Gestión de Inventario",
    "descripcion": "Conteo cíclico, pallet perdido y movimiento de tarimas.",
    "modulos": [
        {
            "id": "conteo_ciclico",
            "nombre": "Conteo Cíclico",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Comprender la metodología de conteo cíclico",
                "Ejecutar conteos de acuerdo al plan",
                "Registrar resultados y resolver discrepancias",
                "Analizar resultados y proponer mejoras",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Conteo Cíclico?",
                    "texto": "Es un método de verificación de inventario que cuenta un grupo específico de productos de forma periódica y rotativa, sin necesidad de detener la operación. Permite mantener alta precisión de inventario durante todo el año.",
                },
                {
                    "titulo": "Tipos de conteo cíclico",
                    "texto": "• Conteo por ABC: Según valor del producto (A=alto, B=medio, C=bajo)\n  - Clase A: se cuenta mensualmente\n  - Clase B: se cuenta trimestralmente\n  - Clase C: se cuenta semestralmente\n• Conteo por ubicación: por zonas del CD\n• Conteo por discrepancia: cuando hay alertas del sistema",
                },
                {
                    "titulo": "Proceso de ejecución",
                    "texto": "1. Recibir la lista de ubicaciones a contar del sistema\n2. Ir a cada ubicación sin conocer el stock sistémico (conteo ciego)\n3. Contar físicamente cada SKU presente\n4. Ingresar el conteo en el sistema\n5. El sistema detecta discrepancias automáticamente\n6. Para discrepancias: realizar segundo conteo de confirmación\n7. Si persiste: aplicar ajuste con autorización",
                },
                {
                    "titulo": "Análisis de resultados",
                    "texto": "Indicadores del conteo cíclico:\n• Exactitud de inventario = (Ubicaciones sin diferencia / Total ubicaciones) × 100\n• Meta típica: >98% de exactitud\n• Los resultados se analizan mensualmente\n• Se identifican áreas problemáticas para investigación",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Cuál es la ventaja del conteo cíclico vs inventario total?",
                    "opciones": [
                        "Es más preciso en todos los casos",
                        "No requiere detener la operación",
                        "Es más barato en recursos",
                        "Se hace una sola vez al año",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El conteo cíclico permite verificar inventario continuamente sin parar la operación del CD.",
                },
                {
                    "pregunta": "En la clasificación ABC, ¿los productos clase A con qué frecuencia se cuentan?",
                    "opciones": [
                        "Una vez al año",
                        "Mensualmente",
                        "Solo cuando hay problemas",
                        "Cada 2 años",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los productos de alto valor (Clase A) requieren conteo mensual por su impacto financiero.",
                },
                {
                    "pregunta": "¿Qué es el conteo ciego?",
                    "opciones": [
                        "Contar con los ojos cerrados",
                        "Contar sin conocer el stock sistémico previo para evitar sesgo",
                        "Contar solo los productos que no se ven bien",
                        "Un tipo de conteo nocturno",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El conteo ciego elimina el sesgo de que el operador ajuste su conteo al stock del sistema.",
                },
                {
                    "pregunta": "¿Qué se debe hacer cuando el conteo cíclico muestra una discrepancia?",
                    "opciones": [
                        "Ajustar inmediatamente al número del sistema",
                        "Realizar un segundo conteo de confirmación antes de ajustar",
                        "Ignorar la discrepancia si es menor a 5 unidades",
                        "Reportar al proveedor",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Antes de hacer un ajuste, se debe confirmar la discrepancia con un segundo conteo.",
                },
            ],
            "practica": "Ejecutar un conteo cíclico de 20 ubicaciones asignadas usando conteo ciego, registrar en el sistema, identificar discrepancias, realizar segundo conteo de confirmación y calcular la exactitud de inventario del ejercicio.",
        },
        {
            "id": "pallet_perdido",
            "nombre": "Pallet Perdido",
            "procedimiento": "PR-QL-QA-PP-00",
            "objetivos": [
                "Entender qué es un pallet perdido y cómo se genera",
                "Ejecutar el proceso de búsqueda y resolución",
                "Registrar correctamente en el sistema",
                "Aplicar el ajuste correspondiente si no se encuentra",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es un Pallet Perdido?",
                    "texto": "Un pallet perdido es aquel que el sistema indica en una ubicación pero que físicamente no se encuentra ahí. Puede deberse a movimientos no registrados, errores de ubicación, problemas de RF o despachos sin confirmación sistémica.",
                },
                {
                    "titulo": "Causas frecuentes",
                    "texto": "• Movimiento manual sin actualización en el sistema\n• Error de escaneo al ubicar la tarima\n• Tarima enviada a otra ubicación por error\n• Pallet despachado sin confirmación sistémica\n• Problema de comunicación del equipo RF durante el movimiento",
                },
                {
                    "titulo": "Proceso de resolución",
                    "texto": "1. Verificar la ubicación indicada por el sistema\n2. Buscar en ubicaciones cercanas (radio de 5 ubicaciones)\n3. Revisar historial de movimientos del pallet en el sistema\n4. Verificar si fue despachado sin confirmación\n5. Buscar en andenes y áreas de despacho\n6. Si no se encuentra: generar ajuste negativo (Ajuste 28) con autorización\n7. Registrar en informe de pallets perdidos",
                },
                {
                    "titulo": "Prevención",
                    "texto": "Para evitar pallets perdidos:\n• Confirmar siempre el movimiento en el sistema RF\n• Nunca mover tarimas manualmente sin registro\n• Verificar que el escaneo fue exitoso al reubicar\n• Ante falla de RF: anotar manualmente y registrar apenas vuelva el sistema\n• Reportar problemas de RF inmediatamente a soporte",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué es lo primero que se debe hacer ante un pallet perdido?",
                    "opciones": [
                        "Hacer el ajuste inmediatamente",
                        "Verificar la ubicación indicada por el sistema",
                        "Notificar al gerente",
                        "Ignorar la discrepancia",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre verificar primero en la ubicación indicada antes de buscar en otro lugar o ajustar.",
                },
                {
                    "pregunta": "Después de verificar la ubicación y no encontrar el pallet, ¿qué se debe hacer?",
                    "opciones": [
                        "Ajustar directamente",
                        "Buscar en ubicaciones cercanas y revisar el historial de movimientos",
                        "Llamar al proveedor",
                        "Esperar a que aparezca solo",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El proceso de búsqueda incluye ubicaciones cercanas e historial de movimientos antes de ajustar.",
                },
                {
                    "pregunta": "¿Qué ajuste se aplica si definitivamente no se encuentra el pallet?",
                    "opciones": [
                        "Ajuste 27 (positivo)",
                        "Ajuste 28 (negativo) con autorización",
                        "Ajuste 12 (devolución proveedor)",
                        "No se aplica ningún ajuste",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Si el pallet no se encuentra, es un faltante y se aplica Ajuste 28 negativo con autorización del supervisor.",
                },
                {
                    "pregunta": "¿Cuál es la mejor forma de prevenir pallets perdidos?",
                    "opciones": [
                        "Hacer más inventarios anuales",
                        "Confirmar siempre el movimiento en el sistema RF y nunca mover sin registro",
                        "Tener más personal en el turno",
                        "Reducir los movimientos de tarimas",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La prevención principal es el registro correcto y oportuno de todos los movimientos en el sistema.",
                },
            ],
            "practica": "Resolver 3 casos de pallet perdido: verificar ubicación, buscar en zonas cercanas, revisar historial, documentar la búsqueda y aplicar el ajuste correspondiente si no se encuentra.",
        },
        {
            "id": "mov_tarimas",
            "nombre": "Movimiento Manual de Tarimas",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Conocer cuándo se requiere un movimiento manual",
                "Ejecutar el movimiento en el sistema correctamente",
                "Entender el impacto de movimientos no registrados",
                "Seguir el proceso correcto para evitar discrepancias",
            ],
            "contenido": [
                {
                    "titulo": "Movimiento Manual de Tarimas",
                    "texto": "El movimiento manual de tarimas se realiza cuando es necesario reubicar mercadería y el sistema no genera la instrucción automáticamente. Debe quedar registrado en el sistema para mantener la exactitud del inventario.",
                },
                {
                    "titulo": "¿Cuándo se realiza un movimiento manual?",
                    "texto": "Se requiere movimiento manual cuando:\n• Se necesita despejar una zona sin orden del sistema\n• Un producto debe cambiarse de temperatura (zona fría a seca)\n• Reubicación por reorganización del CD\n• Tarima parcial que debe consolidarse\n• Corrección de una ubicación incorrecta",
                },
                {
                    "titulo": "Proceso correcto",
                    "texto": "1. Identificar la tarima a mover (escanear etiqueta)\n2. Registrar en el sistema el movimiento ANTES de mover físicamente\n3. Mover físicamente la tarima a la nueva ubicación\n4. Confirmar en el sistema la llegada a la nueva ubicación\n5. Si el sistema falla: anotar en planilla manual e ingresar al recuperar\n6. Verificar que el sistema refleje la nueva ubicación correctamente",
                },
                {
                    "titulo": "Consecuencias de no registrar",
                    "texto": "Un movimiento no registrado genera:\n• Reserva vacía en la ubicación origen\n• Stock 'fantasma' en el sistema\n• Fallas en picking (el sistema envía a la ubicación incorrecta)\n• Discrepancias en el próximo conteo cíclico\n• Posible pallet perdido si no se encuentra en ninguna parte",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Por qué es importante registrar los movimientos manuales?",
                    "opciones": [
                        "Para cumplir un requisito administrativo solamente",
                        "Para mantener la exactitud del inventario y evitar discrepancias",
                        "No es importante registrarlos si se mueve poco",
                        "Solo para productos de alto valor",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Todo movimiento debe registrarse para que el sistema refleje la realidad física y el picking sea correcto.",
                },
                {
                    "pregunta": "¿Cuándo se debe registrar el movimiento en el sistema?",
                    "opciones": [
                        "Después de terminar el turno",
                        "Antes o durante el movimiento físico de la tarima",
                        "Al final de la semana en el cierre",
                        "Solo si el supervisor lo requiere",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El registro debe ser oportuno: antes o durante el movimiento, nunca después del turno.",
                },
                {
                    "pregunta": "¿Qué se debe hacer si el sistema RF falla durante un movimiento?",
                    "opciones": [
                        "Cancelar el movimiento y esperar que vuelva el sistema",
                        "Anotar en planilla manual e ingresar en el sistema cuando se recupere",
                        "Mover igual sin registrar y olvidarlo",
                        "Llamar al proveedor del sistema",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Ante falla del sistema, el registro manual temporal evita perder el movimiento y genera trazabilidad.",
                },
                {
                    "pregunta": "¿Qué problema genera un movimiento de tarima no registrado?",
                    "opciones": [
                        "Ningún problema, el sistema se actualiza solo",
                        "Reserva vacía en origen y fallas en picking",
                        "Solo aumenta el tiempo de despacho",
                        "Problema solo si es un producto clase A",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Un movimiento no registrado crea una reserva vacía que afecta directamente el picking.",
                },
            ],
            "practica": "Realizar 5 movimientos manuales en ambiente de práctica: registrar en el sistema, mover físicamente, confirmar en sistema y verificar que las ubicaciones queden correctas tanto en el sistema como físicamente.",
        },
    ],
}
