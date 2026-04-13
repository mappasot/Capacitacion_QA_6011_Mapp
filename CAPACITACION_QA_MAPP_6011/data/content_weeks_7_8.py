"""Training content for Weeks 7 and 8.

Week 7: Control de Calidad y Mermas
Week 8: Operaciones Complementarias y Evaluación Final
"""

WEEK_7 = {
    "semana": 7,
    "titulo": "Control de Calidad y Mermas",
    "descripcion": "Control de permanencias, manejo de mermas y donaciones.",
    "modulos": [
        {
            "id": "ctrl_permanencias",
            "nombre": "Control de Permanencias",
            "procedimiento": "PR-QL-QA-CP-00",
            "objetivos": [
                "Entender la política de permanencias del CD",
                "Identificar productos fuera de política",
                "Gestionar acciones correctivas según nivel de alerta",
                "Generar reportes y escalamientos oportunos",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Control de Permanencias?",
                    "texto": "Controla el tiempo que la mercadería permanece en el CD. Productos que exceden el tiempo máximo de permanencia deben ser gestionados para evitar vencimientos y pérdidas. Es un proceso preventivo que reduce la merma desconocida.",
                },
                {
                    "titulo": "Niveles de alerta",
                    "texto": "El control de permanencias funciona con 3 niveles:\n• Verde: Dentro del plazo → Sin acción requerida\n• Amarillo: Cerca del límite (70-90% del plazo) → Alerta temprana, priorizar despacho\n• Rojo: En o superando el límite → Acción urgente, escalar a jefatura",
                },
                {
                    "titulo": "Acciones por nivel de alerta",
                    "texto": "Por nivel de alerta:\n• Alerta Amarilla:\n  - Priorizar el producto en el picking\n  - Notificar al área comercial para acelerar salida\n  - Registrar en el reporte de permanencias\n• Alerta Roja:\n  - Acción inmediata\n  - Escalamiento a jefatura\n  - Evaluar donación, promoción o ajuste si ya no es viable",
                },
                {
                    "titulo": "Generación de reportes",
                    "texto": "El reporte de permanencias debe incluir:\n• Lista de productos con su antigüedad en el CD\n• Nivel de alerta de cada producto\n• Acción propuesta o ya tomada\n• Responsable de la acción\n• Fecha límite de resolución\n\nFrecuencia del reporte: según procedimiento (diaria/semanal)",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Por qué es importante controlar las permanencias?",
                    "opciones": [
                        "Para organizar mejor el CD y liberar espacios",
                        "Para evitar vencimientos y pérdidas de producto en el CD",
                        "Para cumplir un KPI de gestión solamente",
                        "No es importante si el CD tiene espacio",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El control de permanencias previene que productos se venzan o pierdan dentro del CD, reduciendo mermas.",
                },
                {
                    "pregunta": "¿Qué acción corresponde ante una alerta Amarilla de permanencia?",
                    "opciones": [
                        "Escalar inmediatamente a jefatura y ajustar el producto",
                        "Priorizar el producto en picking y notificar al área comercial",
                        "Ignorar por ahora, todavía no es urgente",
                        "Donarlo inmediatamente sin investigar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "En alerta amarilla, el objetivo es acelerar la salida del producto antes de que llegue a rojo.",
                },
                {
                    "pregunta": "¿Qué se debe hacer cuando un producto llega a alerta ROJA de permanencia?",
                    "opciones": [
                        "Esperar hasta que el sistema lo baje automáticamente",
                        "Acción inmediata y escalamiento a jefatura para evaluar opciones",
                        "Solo registrar en el reporte semanal",
                        "Continuar normal, es solo un indicador",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La alerta roja requiere acción inmediata y escalamiento para evitar la pérdida del producto.",
                },
                {
                    "pregunta": "¿Qué debe incluir el reporte de permanencias?",
                    "opciones": [
                        "Solo los productos en alerta roja",
                        "Lista completa con antigüedad, nivel de alerta, acción y responsable",
                        "Solo el nombre del producto y la fecha de ingreso",
                        "Solo los productos clase A según ABC",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El reporte debe ser completo para permitir una gestión efectiva de todos los productos con permanencia elevada.",
                },
            ],
            "practica": "Generar un reporte de permanencias de un ejemplo, identificar los 10 productos más antiguos, clasificarlos por nivel de alerta y proponer una acción específica para cada uno.",
        },
        {
            "id": "mermas",
            "nombre": "Manejo y Registro de Mermas",
            "procedimiento": "PR-QL-QA-MRM-00",
            "objetivos": [
                "Comprender los tipos de merma",
                "Registrar correctamente cada tipo de merma",
                "Analizar indicadores de merma",
                "Implementar acciones de reducción de merma",
            ],
            "contenido": [
                {
                    "titulo": "Tipos de Merma",
                    "texto": "Las mermas se clasifican en:\n• Merma conocida: Se sabe la causa (daño, vencimiento, donación)\n• Merma desconocida: Faltantes sin causa identificada (robo, errores)\n• Merma operacional: Pérdidas inevitables por la operación normal\n\nLa clasificación correcta es fundamental para el análisis y control.",
                },
                {
                    "titulo": "Proceso de registro por tipo",
                    "texto": "Merma Conocida:\n• Documentar causa específica\n• Aplicar ajuste correspondiente (4, 10 u 11)\n• Tomar evidencia fotográfica\n\nMerma Desconocida:\n• Registrar como Ajuste 28\n• Investigar causa raíz\n• Reportar en informe mensual con análisis\n• Implementar controles si hay patrón",
                },
                {
                    "titulo": "Indicadores de merma",
                    "texto": "Los principales KPIs de merma son:\n• % de Merma Total = (Merma $ / Venta $) × 100\n• % de Merma Conocida vs Desconocida\n• Merma por categoría de producto\n• Merma por causa (daño, vencimiento, desconocida)\n\nMetas típicas: merma total < 0.5% sobre venta",
                },
                {
                    "titulo": "Reducción de merma",
                    "texto": "Estrategias para reducir merma:\n• FEFO estricto en almacenaje y picking\n• Control de permanencias proactivo\n• Capacitación en manejo de productos frágiles\n• Mejora de embalaje en recepciones dañadas\n• Análisis mensual de causa raíz y acciones correctivas\n• Control de acceso a zonas de alto valor",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Cuál es la diferencia entre merma conocida y desconocida?",
                    "opciones": [
                        "La merma conocida siempre es mayor en valor",
                        "En la merma conocida se identifica la causa; en la desconocida no se sabe por qué falta",
                        "No hay diferencia, ambas se registran igual",
                        "La merma desconocida nunca se registra en el sistema",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La clave es si se puede identificar la causa: daño, vencimiento (conocida) vs faltante sin causa clara (desconocida).",
                },
                {
                    "pregunta": "¿Con qué ajuste se registra la merma desconocida?",
                    "opciones": [
                        "Ajuste 4 (daño)",
                        "Ajuste 28 (negativo)",
                        "Ajuste 11 (donación)",
                        "Ajuste 27 (positivo)",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La merma desconocida es un faltante sin causa identificada, por lo que se registra con Ajuste 28 negativo.",
                },
                {
                    "pregunta": "¿Cómo se calcula el % de merma total?",
                    "opciones": [
                        "(Cantidad perdida / Cantidad total) × 100",
                        "(Merma en $ / Venta en $) × 100",
                        "Solo se mide en unidades físicas",
                        "(Ajustes negativos / Ajustes positivos) × 100",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El % de merma se calcula sobre el valor económico ($ de merma / $ de venta) para tener perspectiva de impacto real.",
                },
                {
                    "pregunta": "¿Cuál es una estrategia efectiva para reducir merma por vencimiento?",
                    "opciones": [
                        "Comprar menos productos",
                        "Aplicar FEFO estricto y control proactivo de permanencias",
                        "Revisar el inventario solo una vez al año",
                        "Vender productos próximos a vencer sin informar al cliente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "FEFO (First Expired, First Out) combinado con control de permanencias es la estrategia más efectiva para reducir vencimientos.",
                },
            ],
            "practica": "Clasificar 10 casos de merma por tipo (conocida/desconocida), registrar cada uno con el ajuste correcto, calcular el indicador de merma del período y proponer 2 acciones de mejora basadas en el análisis.",
        },
        {
            "id": "donaciones",
            "nombre": "Donaciones",
            "procedimiento": "PR-QL-QA-DON-00",
            "objetivos": [
                "Conocer el proceso completo de donaciones",
                "Identificar productos aptos para donación",
                "Gestionar la documentación legal requerida",
                "Ejecutar el registro en el sistema correctamente",
            ],
            "contenido": [
                {
                    "titulo": "Proceso de Donaciones",
                    "texto": "Las donaciones son parte de la responsabilidad social de Walmart Chile. Productos que no pueden ser comercializados pero que están en condiciones de consumo se donan a instituciones autorizadas. Es un proceso que requiere rigor documental.",
                },
                {
                    "titulo": "Criterios de aptitud para donación",
                    "texto": "Para donar, el producto DEBE:\n• Estar dentro de fecha de vencimiento\n• Tener embalaje íntegro (sin rotura que comprometa el producto)\n• No haber sufrido ruptura de cadena de frío (si aplica)\n• Tener etiqueta legible con fecha de vencimiento\n• Ser apto para consumo humano según criterio QA",
                },
                {
                    "titulo": "Documentación obligatoria",
                    "texto": "Para completar una donación:\n• Acta de donación: describe productos, cantidades, destino\n• Listado detallado: código, descripción, cantidad, fecha de vencimiento\n• Firma del representante de la institución receptora\n• Registro fotográfico de la entrega\n• Registro en el sistema con Ajuste 11\n• Archivado de toda la documentación",
                },
                {
                    "titulo": "Frecuencia y planificación",
                    "texto": "Las donaciones deben planificarse con antelación:\n• Coordinar con la institución la fecha y hora de retiro\n• Verificar que la institución está en la lista de autorizados (RSE)\n• Preparar la mercadería antes de la visita de la institución\n• Tener toda la documentación lista para firma en el momento\n• Registrar el Ajuste 11 el mismo día de la donación",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué documentación se requiere para una donación?",
                    "opciones": [
                        "Solo un correo de aviso interno",
                        "Acta de donación, listado de productos, firma y registro fotográfico",
                        "Solo el Ajuste 11 en el sistema",
                        "Solo la aprobación verbal del jefe de área",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La donación requiere documentación completa para cumplir requisitos legales, tributarios y de auditoría.",
                },
                {
                    "pregunta": "¿Cuándo se debe registrar el Ajuste 11 en el sistema?",
                    "opciones": [
                        "Al final del mes",
                        "El mismo día que se realiza la donación",
                        "Cuando la institución confirme que recibió el producto",
                        "Solo si el supervisor lo solicita explícitamente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El ajuste debe realizarse el mismo día de la donación para mantener la exactitud del inventario.",
                },
                {
                    "pregunta": "¿Qué sucede si un producto apto para donación tiene la etiqueta de fecha ilegible?",
                    "opciones": [
                        "Se dona igual, el producto visualmente parece bueno",
                        "No puede donarse: debe tener fecha de vencimiento legible obligatoriamente",
                        "Se cambia la etiqueta con la fecha que uno cree que es",
                        "Solo importa la fecha si es un producto refrigerado",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Sin fecha legible no se puede garantizar la aptitud del producto. No se debe donar si no hay trazabilidad completa.",
                },
                {
                    "pregunta": "¿Qué debe verificarse sobre la institución antes de realizar una donación?",
                    "opciones": [
                        "Solo que sea una organización sin fines de lucro",
                        "Que esté en la lista de instituciones autorizadas por el área de RSE",
                        "Que tenga camiones propios para retirar",
                        "No se verifica nada, cualquier institución puede recibir",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Solo se dona a instituciones previamente autorizadas por RSE para garantizar el cumplimiento legal y la trazabilidad.",
                },
            ],
            "practica": "Preparar la documentación completa para una donación ficticia de 5 productos: verificar aptitud de cada producto, completar el acta de donación, preparar el listado detallado y simular el registro del Ajuste 11.",
        },
    ],
}

WEEK_8 = {
    "semana": 8,
    "titulo": "Operaciones Complementarias y Evaluación Final",
    "descripcion": "Asignación de Prime, etiquetado, medidas logísticas y evaluación integral.",
    "modulos": [
        {
            "id": "prime",
            "nombre": "Asignación de Prime",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Entender qué es la asignación de Prime",
                "Ejecutar el proceso en el sistema",
                "Verificar correcta asignación",
                "Optimizar las ubicaciones para mejorar la productividad",
            ],
            "contenido": [
                {
                    "titulo": "Asignación de Prime",
                    "texto": "La asignación de Prime define las ubicaciones principales (prime) para el picking de productos. Una correcta asignación optimiza los tiempos de preparación de pedidos al colocar los productos de mayor rotación en las mejores ubicaciones.",
                },
                {
                    "titulo": "¿Qué es una ubicación Prime?",
                    "texto": "Una ubicación Prime es la ubicación principal asignada a un SKU en el CD. Características:\n• Accesible a nivel de suelo o bajo andamio (fácil picking)\n• Cerca de la zona de despacho (menor distancia de recorrido)\n• Tamaño adecuado para el volumen del producto\n• El sistema dirige al preparador a esta ubicación primero",
                },
                {
                    "titulo": "Proceso de asignación",
                    "texto": "Para asignar o cambiar una ubicación Prime:\n1. Analizar la rotación del producto (ventas últimos 30 días)\n2. Identificar la mejor ubicación disponible\n3. Registrar el cambio en el sistema\n4. Reubicar físicamente el producto si es necesario\n5. Verificar que el sistema dirija el picking correctamente\n6. Monitorear la productividad después del cambio",
                },
                {
                    "titulo": "Impacto en la productividad",
                    "texto": "Una buena asignación de Prime:\n• Reduce el recorrido del preparador (metros caminados)\n• Disminuye el tiempo por línea de picking\n• Mejora el rendimiento general del turno\n• Reduce errores al tener el producto bien ubicado\n• Un producto clase A mal ubicado puede costar miles de líneas lentas al mes",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Para qué sirve la asignación de Prime?",
                    "opciones": [
                        "Para almacenar productos de alto valor económico",
                        "Para optimizar las ubicaciones de picking y mejorar productividad",
                        "Para clasificar proveedores por importancia",
                        "Para gestionar devoluciones al proveedor",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Prime define las ubicaciones óptimas para picking, reduciendo recorrido y mejorando la productividad del CD.",
                },
                {
                    "pregunta": "¿Qué característica tiene una buena ubicación Prime?",
                    "opciones": [
                        "Estar en el nivel más alto del rack",
                        "Ser accesible, cerca de despacho y de tamaño adecuado para el producto",
                        "Estar lejos del área de tráfico de montacargas",
                        "Ser la más grande disponible sin importar ubicación",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Las ubicaciones Prime deben ser accesibles, cercanas al despacho y del tamaño correcto para el producto.",
                },
                {
                    "pregunta": "¿Qué dato es más importante para definir si un producto necesita ubicación Prime prioritaria?",
                    "opciones": [
                        "El peso del producto",
                        "La rotación del producto (ventas recientes)",
                        "El precio unitario",
                        "El tamaño del embalaje",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los productos de alta rotación son los que más se benefician de una ubicación Prime porque se pickean muchas veces al día.",
                },
                {
                    "pregunta": "¿Qué debe verificarse después de cambiar una asignación Prime en el sistema?",
                    "opciones": [
                        "Nada, el sistema se actualiza automáticamente en todo",
                        "Que el sistema dirija el picking a la nueva ubicación correctamente",
                        "Solo notificar al supervisor del cambio",
                        "Hacer un inventario completo del CD",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre validar que el sistema dirija correctamente el picking después de un cambio de Prime.",
                },
            ],
            "practica": "Revisar las asignaciones Prime actuales de 10 productos de alta rotación, verificar si están en ubicaciones óptimas, proponer mejoras fundamentadas en la rotación y simular el cambio en el sistema.",
        },
        {
            "id": "etiquetado",
            "nombre": "Etiquetado Macroservice",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Conocer los estándares de etiquetado del CD",
                "Ejecutar el proceso de etiquetado correctamente",
                "Verificar la calidad del etiquetado",
                "Identificar y corregir etiquetado incorrecto",
            ],
            "contenido": [
                {
                    "titulo": "Etiquetado Macroservice",
                    "texto": "El etiquetado correcto es fundamental para la trazabilidad y el correcto procesamiento de la mercadería. Incluye información de producto, lote, vencimiento y código de barras. Sin etiqueta correcta, el producto no puede procesarse en el sistema.",
                },
                {
                    "titulo": "Información obligatoria en la etiqueta",
                    "texto": "Toda etiqueta debe contener:\n• Código de barras legible (EAN/UPC)\n• Nombre o descripción del producto\n• Número de lote de fabricación\n• Fecha de vencimiento (formato definido)\n• Nombre del proveedor/fabricante\n• Peso neto (si aplica)",
                },
                {
                    "titulo": "Proceso de etiquetado",
                    "texto": "1. Imprimir la etiqueta según el sistema Macroservice\n2. Verificar que la información impresa es correcta\n3. Aplicar la etiqueta en la ubicación definida del producto\n4. Verificar legibilidad del código de barras con el lector\n5. Registrar el etiquetado en el sistema\n6. Si la etiqueta no pasa el control de lector: reemplazar",
                },
                {
                    "titulo": "Errores de etiquetado y consecuencias",
                    "texto": "Errores comunes y sus consecuencias:\n• Código de barras ilegible: No puede procesarse, se convierte en Problem Freight\n• Fecha incorrecta: Riesgo de vender producto fuera de política\n• Producto equivocado: Genera error de despacho\n• Etiqueta sobre otra: Puede causar confusión y error de precio",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué información debe contener la etiqueta?",
                    "opciones": [
                        "Solo el nombre del producto",
                        "Código de barras, descripción, lote y fecha de vencimiento",
                        "Solo el código de barras",
                        "Solo la fecha de vencimiento y el precio",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La etiqueta debe contener toda la información necesaria para trazabilidad completa del producto.",
                },
                {
                    "pregunta": "¿Qué sucede si el código de barras de la etiqueta no pasa el control de lector?",
                    "opciones": [
                        "Se usa de todas formas y se registra manual",
                        "Se reemplaza la etiqueta por una que sí sea legible",
                        "Se cambia el código en el sistema para que coincida",
                        "Se dona el producto inmediatamente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Un código ilegible impide el procesamiento correcto; debe reemplazarse la etiqueta antes de ingresar al inventario.",
                },
                {
                    "pregunta": "¿Qué problema genera poner una etiqueta sobre otra existente?",
                    "opciones": [
                        "Ningún problema, es la forma estándar de re-etiquetar",
                        "Puede causar confusión y error de precio o producto si la primera etiqueta es visible",
                        "Solo es problema si los productos son refrigerados",
                        "Es aceptable si la primera etiqueta está dañada",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Superponer etiquetas puede causar que el lector detecte la etiqueta incorrecta, generando errores.",
                },
                {
                    "pregunta": "¿Cuándo un producto con etiqueta incorrecta se convierte en Problem Freight?",
                    "opciones": [
                        "Nunca, el etiquetado siempre se puede corregir en el sistema",
                        "Cuando el código de barras es ilegible y no puede procesarse normalmente",
                        "Solo si es un producto importado",
                        "Si el producto tiene más de 6 meses de vigencia",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Un código de barras ilegible impide el procesamiento normal y clasifica al producto como Problem Freight.",
                },
            ],
            "practica": "Etiquetar 10 productos de ejemplo con el sistema Macroservice: imprimir, verificar información, aplicar, verificar legibilidad con lector y registrar en el sistema. Identificar al menos un error intencional en los ejemplos.",
        },
        {
            "id": "medidas_logisticas",
            "nombre": "Captura de Medidas Logísticas",
            "procedimiento": "PR-QL-QA-CML-00",
            "objetivos": [
                "Entender la importancia de las medidas logísticas",
                "Capturar correctamente las dimensiones y peso",
                "Registrar en el sistema master de productos",
                "Identificar consecuencias de medidas incorrectas",
            ],
            "contenido": [
                {
                    "titulo": "Medidas Logísticas",
                    "texto": "Las medidas logísticas (largo, ancho, alto, peso) son fundamentales para la optimización del almacenamiento y transporte. Una medida incorrecta afecta la asignación de ubicaciones en el CD y la cubicación de camiones.",
                },
                {
                    "titulo": "¿Qué medidas se capturan?",
                    "texto": "Se capturan las medidas de:\n• Unidad de venta (unidad individual)\n• Unidad logistica (caja, master, pallet)\n\nDatos requeridos por cada unidad:\n• Largo (cm)\n• Ancho (cm)\n• Alto (cm)\n• Peso bruto (kg)\n• Peso neto (kg)\n• Unidades por caja, cajas por pallet",
                },
                {
                    "titulo": "Proceso de captura",
                    "texto": "1. Identificar el producto a medir (código, descripción)\n2. Medir con cinta métrica: largo, ancho y alto (incluyendo embalaje)\n3. Pesar en balanza calibrada: peso bruto y neto\n4. Verificar unidades por caja y cajas por tarima\n5. Ingresar datos en el formulario de medidas\n6. Ingresar en el sistema master de productos\n7. Validar que el sistema calcule correctamente el volumen",
                },
                {
                    "titulo": "Impacto de medidas incorrectas",
                    "texto": "Consecuencias de medidas mal registradas:\n• Asignación incorrecta de ubicaciones en el CD (espacios sobra/falta)\n• Errores de cubicación de camiones (sobre/sub-utilización)\n• Problemas en el reabastecimiento automático\n• Discrepancias en el peso del pedido\n• Ajustes de inventario incorrectos por unidad de medida mal definida",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Por qué son importantes las medidas logísticas?",
                    "opciones": [
                        "Solo para el etiquetado del producto",
                        "Para optimizar el almacenamiento en el CD y la cubicación de camiones",
                        "Para calcular el precio de venta",
                        "No son importantes si el CD tiene espacio suficiente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Medidas correctas permiten optimizar el uso del espacio en el CD y maximizar la carga de los camiones.",
                },
                {
                    "pregunta": "¿Qué medidas deben capturarse de cada producto?",
                    "opciones": [
                        "Solo el peso",
                        "Largo, ancho, alto y peso (bruto y neto) de unidad de venta y logística",
                        "Solo largo y ancho",
                        "Peso y precio unitario",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Se requieren todas las dimensiones y pesos tanto de la unidad individual como de la unidad logística (caja/pallet).",
                },
                {
                    "pregunta": "¿Qué consecuencia tiene una medida de alto incorrecta en el sistema?",
                    "opciones": [
                        "Ningún impacto real en la operación",
                        "Puede asignarse una ubicación que no tenga altura suficiente para el producto real",
                        "Solo afecta el precio del producto",
                        "Solo importa si el CD usa racks altos",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Un alto incorrecto puede asignar el producto a una ubicación donde físicamente no entra, generando problemas operacionales.",
                },
                {
                    "pregunta": "¿Cuál es el instrumento correcto para medir el peso?",
                    "opciones": [
                        "Una cinta métrica",
                        "Una balanza calibrada",
                        "Una estimación visual",
                        "El peso indicado en la etiqueta (siempre exacto)",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre se debe usar una balanza calibrada para garantizar la exactitud del peso registrado en el sistema.",
                },
            ],
            "practica": "Medir 5 productos nuevos o con medidas no confiables en el sistema: registrar todas las dimensiones y pesos, ingresar en el formulario de medidas, comparar con lo que indica el sistema actual e identificar diferencias.",
        },
    ],
}
