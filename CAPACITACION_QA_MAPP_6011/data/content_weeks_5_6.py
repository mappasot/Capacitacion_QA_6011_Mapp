"""Training content for Weeks 5 and 6.

Week 5: Traspasos entre Centros
Week 6: Procesos Especiales
"""

WEEK_5 = {
    "semana": 5,
    "titulo": "Traspasos entre Centros",
    "descripcion": "Procesos de traspaso entre Quilicura, Austral Freezer y Frigo Buin.",
    "modulos": [
        {
            "id": "traspaso_af_ql",
            "nombre": "Traspaso Austral Freezer \u2192 Quilicura",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Conocer el flujo de traspaso AF \u2192 QL",
                "Documentar correctamente el envío",
                "Verificar la recepción en destino",
                "Controlar la cadena de frío durante el traslado",
            ],
            "contenido": [
                {
                    "titulo": "Flujo del Traspaso AF \u2192 QL",
                    "texto": "El traspaso desde Austral Freezer a Quilicura se genera cuando se necesita mover mercadería congelada entre los centros de distribución. Requiere coordinación de transporte refrigerado y control estricto de la cadena de frío durante todo el traslado.",
                },
                {
                    "titulo": "Documentación requerida",
                    "texto": "Documentos obligatorios:\n• Guía de traspaso generada por el sistema (con código único)\n• Control de temperatura al momento de carga (en origen)\n• Control de temperatura al momento de descarga (en destino)\n• Verificación de sellos del camión al cerrar y al abrir\n• Conformidad de recepción en destino (firma responsable)\n• Número de precintos y estados",
                },
                {
                    "titulo": "Control de la cadena de frío",
                    "texto": "Para productos congelados:\n• Temperatura de carga: -18\u00b0C o menor\n• Durante traslado: no debe superar -15\u00b0C\n• Temperatura de descarga: verificar que mantiene -18\u00b0C o menor\n• Si temperatura fuera de rango: NO recibir y generar reporte\n• Tiempo máximo de trayecto según distancia establecida",
                },
                {
                    "titulo": "Proceso de recepción en QL",
                    "texto": "En Quilicura, al recibir el traspaso:\n1. Verificar sello del camión (número coincide con guía)\n2. Tomar temperatura antes de abrir\n3. Inspeccionar condiciones del producto\n4. Contar unidades/tarimas vs guía de traspaso\n5. Registrar conformidad o discrepancia en el sistema\n6. Firmar documentos de recepción",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué es crítico verificar en un traspaso de productos congelados?",
                    "opciones": [
                        "El color del camión",
                        "La cadena de frío (temperatura durante todo el traslado)",
                        "El nombre del conductor",
                        "La hora de salida del camión",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La cadena de frío es lo más crítico en traspasos de congelados: una ruptura compromete la inocuidad del producto.",
                },
                {
                    "pregunta": "¿A qué temperatura deben estar los productos congelados durante el traspaso?",
                    "opciones": [
                        "Entre 0\u00b0C y 5\u00b0C",
                        "-18\u00b0C o menor",
                        "Temperatura ambiente",
                        "Entre -5\u00b0C y -10\u00b0C",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los productos congelados deben mantenerse a -18\u00b0C o menor durante todo el traslado para preservar su inocuidad.",
                },
                {
                    "pregunta": "¿Qué se debe hacer si al recibir el traspaso la temperatura está fuera de rango?",
                    "opciones": [
                        "Recibir de todas formas y registrar la observación",
                        "No recibir y generar un reporte de no conformidad",
                        "Esperar a que baje la temperatura y recibir después",
                        "Recibir si la diferencia es menor de 5\u00b0C",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Si la temperatura está fuera de rango, el producto puede estar comprometido. NO se recibe y se genera reporte.",
                },
                {
                    "pregunta": "¿Cuál es el primer paso al recibir un traspaso AF\u2192QL?",
                    "opciones": [
                        "Abrir el camión y descargar",
                        "Verificar el sello del camión y que el número coincida con la guía",
                        "Contar las tarimas primero",
                        "Firmar la guía de recepción",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Verificar el sello primero asegura la integridad de la carga durante el traslado.",
                },
            ],
            "practica": "Revisar la documentación completa de un traspaso reciente AF\u2192QL, validar que todos los campos estén correctos (temperaturas, sellos, firmas) y simular el proceso de recepción paso a paso.",
        },
        {
            "id": "traspaso_ql_af",
            "nombre": "Traspaso Quilicura \u2192 Austral Freezer",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Conocer el flujo inverso QL \u2192 AF",
                "Entender las diferencias con el traspaso AF \u2192 QL",
                "Ejecutar el proceso de envío en el sistema",
                "Documentar correctamente el traspaso",
            ],
            "contenido": [
                {
                    "titulo": "Flujo QL \u2192 AF",
                    "texto": "El traspaso de Quilicura a Austral Freezer se origina en QL y se envía hacia el CD de Austral Freezer. Los mismos controles de temperatura y documentación aplican. El origen y destino cambian, pero el proceso y estándares de control son idénticos.",
                },
                {
                    "titulo": "Proceso de envío desde QL",
                    "texto": "1. Generar guía de traspaso en el sistema QL\n2. Preparar la mercadería: verificar que esté a temperatura correcta\n3. Cargar el camión frigorífico\n4. Tomar temperatura al momento de carga\n5. Colocar y registrar sello del camión\n6. Enviar guía de traspaso a Austral Freezer\n7. Registrar en el sistema la salida de QL",
                },
                {
                    "titulo": "Diferencias clave entre AF\u2192QL y QL\u2192AF",
                    "texto": "Las diferencias son mínimas:\n• El origen y destino se invierten\n• El sistema que genera la guía es el de origen (QL en este caso)\n• Los controles de temperatura, sello y documentación son EXACTAMENTE iguales\n• La responsabilidad del envío queda en QL hasta la recepción en AF",
                },
                {
                    "titulo": "Responsabilidades en el traspaso",
                    "texto": "Durante el traspaso QL\u2192AF:\n• QL es responsable de: correcta carga, temperatura en origen, documentación\n• Transportista es responsable de: cadena de frío durante el traslado\n• AF es responsable de: recepción correcta, verificar condiciones de llegada\n• QA verifica en ambos extremos que el proceso se ejecute correctamente",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿La documentación del traspaso QL\u2192AF es diferente a AF\u2192QL?",
                    "opciones": [
                        "Sí, completamente diferente, cada traspaso tiene su propio sistema",
                        "No, los controles y documentación requerida son los mismos, solo cambia origen/destino",
                        "Solo cambia el formulario de temperatura",
                        "No requiere documentación en el sentido contrario",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los controles son los mismos: temperatura, sellos, documentación y conformidad. Solo cambia quién envía y quién recibe.",
                },
                {
                    "pregunta": "¿Qué sistema genera la guía de traspaso en el flujo QL\u2192AF?",
                    "opciones": [
                        "El sistema de Austral Freezer (destino)",
                        "El sistema de Quilicura (origen)",
                        "Un sistema central independiente",
                        "No se genera en el sistema, es manual",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre es el sistema del CD de origen el que genera la guía de traspaso.",
                },
                {
                    "pregunta": "¿Quién es responsable de la cadena de frío DURANTE el traslado QL\u2192AF?",
                    "opciones": [
                        "Quilicura (origen)",
                        "El transportista",
                        "Austral Freezer (destino)",
                        "Nadie, es responsabilidad compartida sin definición",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Durante el traslado, el transportista es el responsable de mantener las condiciones de temperatura.",
                },
                {
                    "pregunta": "¿Qué se debe hacer en QL antes de cargar el camión para el traspaso a AF?",
                    "opciones": [
                        "Cargar directamente desde el picking",
                        "Verificar que la mercadería ya esté a la temperatura correcta antes de cargar",
                        "Esperar la aprobación de AF",
                        "Generar la guia DESPUÉS de cargar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El producto debe estar ya a la temperatura correcta antes de cargar, no se enfría en el camión.",
                },
            ],
            "practica": "Generar la documentación completa para un traspaso QL\u2192AF ficticio: guía en el sistema, registros de temperatura, número de sello, y simular el proceso de carga y envío.",
        },
        {
            "id": "traspaso_fb_ql",
            "nombre": "Traspaso Frigo Buin \u2194 Quilicura",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Conocer el flujo de traspaso entre FB y QL",
                "Entender las particularidades de productos refrigerados",
                "Diferenciar entre productos refrigerados y congelados",
                "Aplicar los controles correctos para cada tipo",
            ],
            "contenido": [
                {
                    "titulo": "Traspaso Frigo Buin",
                    "texto": "Los traspasos entre Frigo Buin y Quilicura involucran principalmente productos refrigerados (no congelados). Los rangos de temperatura son diferentes a los congelados y los tiempos de tránsito son más críticos por la sensibilidad de los productos.",
                },
                {
                    "titulo": "Diferencias clave: Refrigerado vs Congelado",
                    "texto": "Refrigerado (Frigo Buin):\n• Rango de temperatura: 0\u00b0C a 5\u00b0C\n• Mayor sensibilidad al tiempo de tránsito\n• Verificación de vida útil más estricta\n• No se puede recongelar si rompe la cadena\n\nCongelado (Austral Freezer):\n• Temperatura: -18\u00b0C o menor\n• Menor sensibilidad al tiempo (hasta cierto límite)\n• Mayor margen de vida útil generalmente",
                },
                {
                    "titulo": "Controles en traspaso FB\u2194QL",
                    "texto": "Para traspasos refrigerados:\n• Temperatura de carga: 0\u00b0C a 5\u00b0C\n• Tiempo máximo de tránsito: definido por el procedimiento\n• Camión frigorífico en modo refrigerado (no congelado)\n• Verificación de vida útil al carga: debe cumplir política\n• Control de temperatura al llegar a destino",
                },
                {
                    "titulo": "Documentación específica",
                    "texto": "El traspaso FB\u2194QL requiere los mismos documentos que los congelados:\n• Guía de traspaso del sistema\n• Registros de temperatura (origen y destino)\n• Control de sellos\n• Conformidad de recepción\n\nAdemás: verificación especial de vida útil dado que los refrigerados tienen menor margen.",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Cuál es el rango de temperatura para productos refrigerados?",
                    "opciones": [
                        "-18\u00b0C o menos",
                        "0\u00b0C a 5\u00b0C",
                        "10\u00b0C a 15\u00b0C",
                        "Temperatura ambiente (15-25\u00b0C)",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los refrigerados se mantienen entre 0\u00b0C y 5\u00b0C, a diferencia de los congelados que requieren -18\u00b0C o menos.",
                },
                {
                    "pregunta": "¿Por qué los traspasos de productos refrigerados son más sensibles al tiempo?",
                    "opciones": [
                        "Porque son más caros",
                        "Porque tienen menor vida útil y la ruptura de cadena no se puede revertir",
                        "Porque son más pesados",
                        "No son más sensibles que los congelados",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los refrigerados tienen menor vida útil y si se rompe la cadena de frío, no pueden volver a refrigerarse; deben descartarse.",
                },
                {
                    "pregunta": "¿Se puede usar el mismo camión para transportar congelados (-18\u00b0C) y refrigerados (0-5\u00b0C) al mismo tiempo?",
                    "opciones": [
                        "Sí, si el camión tiene suficiente capacidad",
                        "No, cada tipo requiere su propia temperatura de transporte",
                        "Sí, si la distancia es corta",
                        "Solo con autorización del supervisor",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Congelados y refrigerados requieren temperaturas distintas y no deben transportarse juntos sin túneles separados.",
                },
                {
                    "pregunta": "¿Qué se debe verificar especialmente en el traspaso de refrigerados que quizás es menos crítico en congelados?",
                    "opciones": [
                        "El peso del camión",
                        "La vida útil restante del producto al momento del traspaso",
                        "El nombre del proveedor",
                        "El precio del producto",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los refrigerados tienen menos vida útil, por lo que es crítico verificar que cumplan la política al momento del envío.",
                },
            ],
            "practica": "Comparar la documentación de un traspaso refrigerado vs congelado, identificar las diferencias clave en rangos de temperatura y controles, y simular el proceso de traspaso FB\u2192QL incluyendo verificación de vida útil.",
        },
    ],
}

WEEK_6 = {
    "semana": 6,
    "titulo": "Procesos Especiales",
    "descripcion": "Chase, Problem Freight y resolución de RAZ.",
    "modulos": [
        {
            "id": "chase",
            "nombre": "CHASE",
            "procedimiento": "PR-QL-QA-CHASE-00",
            "objetivos": [
                "Entender qué es un Chase y cuándo se genera",
                "Ejecutar el proceso de resolución de Chase",
                "Registrar y dar seguimiento a los Chases",
                "Analizar patrones para prevención",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es un CHASE?",
                    "texto": "El CHASE es un proceso de seguimiento y resolución de discrepancias en el inventario que requiere acción inmediata. Se genera cuando el sistema detecta inconsistencias durante el picking o despacho que afectan la operación en tiempo real.",
                },
                {
                    "titulo": "Tipos de Chase",
                    "texto": "• Chase por faltante en picking: el preparador va a una ubicación y no encuentra el producto\n• Chase por discrepancia en recepción: cantidad recibida difiere de la factura\n• Chase por ubicación incorrecta: producto en ubicación diferente a la del sistema\n• Chase sistémico por conteo: el sistema detecta diferencia en un conteo",
                },
                {
                    "titulo": "Resolución paso a paso",
                    "texto": "1. Revisar la discrepancia reportada en el sistema\n2. Verificar físicamente en la ubicación indicada\n3. Buscar en ubicaciones alternativas\n4. Investigar causa raíz (qué ocurrió con ese producto)\n5. Resolver según el tipo (ajuste, reubicación, confirmación)\n6. Documentar la resolución en el sistema\n7. Cerrar el Chase con código de resolución",
                },
                {
                    "titulo": "Seguimiento y mejora continua",
                    "texto": "Los Chases son una fuente valiosa de información:\n• Un Chase frecuente en el mismo SKU indica problema sistémico\n• Chases recurrentes en la misma zona indican problema de proceso\n• El análisis mensual de Chases permite identificar y corregir causas raíz\n• Reducir los Chases mejora la productividad del picking",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué genera un CHASE?",
                    "opciones": [
                        "Una solicitud del cliente externo",
                        "Inconsistencias de inventario que requieren acción inmediata",
                        "Un cambio de precio en el sistema",
                        "Una nueva recepción de mercadería",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los Chases se generan por discrepancias en el inventario que necesitan resolución inmediata.",
                },
                {
                    "pregunta": "¿Cuál es el paso final en la resolución de un Chase?",
                    "opciones": [
                        "Verificar físicamente la ubicación",
                        "Documentar la resolución y cerrar el Chase en el sistema",
                        "Notificar al proveedor",
                        "Hacer un conteo general del CD",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre se debe documentar la resolución y cerrar el Chase formalmente para trazabilidad.",
                },
                {
                    "pregunta": "¿Qué indica un Chase frecuente en el mismo SKU?",
                    "opciones": [
                        "Que el producto es popular",
                        "Un problema sistémico o de proceso que debe investigarse",
                        "Que el proveedor está fallando en la entrega",
                        "Que el CD está lleno",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La recurrencia indica una causa raíz no resuelta que afecta ese producto específico.",
                },
                {
                    "pregunta": "Si al ir a resolver un Chase no se encuentra el producto en la ubicación indicada, ¿qué se debe hacer?",
                    "opciones": [
                        "Cerrar el Chase indicando que no existe",
                        "Buscar en ubicaciones alternativas e investigar el historial de movimientos",
                        "Hacer un ajuste negativo inmediatamente",
                        "Reportar al gerente y esperar instrucciones",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Antes de ajustar, se debe buscar en alternativas e investigar qué pasó con el producto.",
                },
            ],
            "practica": "Resolver 5 Chases pendientes siguiendo el procedimiento completo: verificar físicamente, investigar, resolver con el tipo de acción correcta y documentar cada paso con código de resolución.",
        },
        {
            "id": "problem_freight",
            "nombre": "Problem Freight",
            "procedimiento": "Instructivo PPT",
            "objetivos": [
                "Identificar qué es Problem Freight",
                "Conocer los criterios de clasificación",
                "Ejecutar el proceso de resolución",
                "Documentar y dar seguimiento al PF",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es Problem Freight?",
                    "texto": "Problem Freight (PF) se refiere a mercadería que presenta problemas que impiden su procesamiento normal en el sistema o su comercialización directa: etiquetado incorrecto, sin código de barras, embalaje inadecuado, sin documentación, etc.",
                },
                {
                    "titulo": "Tipos de Problem Freight",
                    "texto": "• Sin código de barras legible (etiqueta dañada, mal impresa)\n• Información de producto incorrecta en la etiqueta\n• Embalaje inadecuado para el tipo de producto\n• Sin documentación de origen o sanitaria\n• Producto no identificable (marca, SKU, descripción ilegible)\n• Mercadería sin fecha de vencimiento visible",
                },
                {
                    "titulo": "Proceso de gestión del PF",
                    "texto": "1. Identificar el problema específico del PF\n2. Segregar la mercadería en área de PF designada\n3. Clasificar el tipo de problem freight\n4. Resolver según el tipo:\n   - Re-etiquetar (si tiene todos los datos)\n   - Re-embalar (si es problema de embalaje)\n   - Devolver al proveedor (si no tiene solución en el CD)\n5. Registrar en el sistema\n6. Documentar tiempo de resolución",
                },
                {
                    "titulo": "Indicadores de PF",
                    "texto": "El PF tiene sus propios indicadores:\n• Cantidad de PF por periodo\n• Tiempo promedio de resolución\n• Tipo de problema más frecuente\n• Proveedor con más PF (puede indicar problema sistémico con ese proveedor)",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué es Problem Freight?",
                    "opciones": [
                        "Mercadería en perfecto estado",
                        "Mercadería con problemas que impiden su procesamiento o comercialización normal",
                        "Productos de alto valor",
                        "Mercadería en tránsito entre CDs",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Problem Freight es toda mercadería que no puede procesarse normalmente por problemas de identificación, embalaje u otros.",
                },
                {
                    "pregunta": "¿Donde debe segregarse el Problem Freight?",
                    "opciones": [
                        "En la misma ubicación donde fue encontrado",
                        "En el área de PF designada para este fin",
                        "En el área de merma",
                        "En cualquier espacio disponible",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El PF tiene un área específica de segregación para poder gestionarlo correctamente.",
                },
                {
                    "pregunta": "Si un producto de Problem Freight no tiene código de barras pero sí tiene todos los datos del producto, ¿qué acción se toma?",
                    "opciones": [
                        "Devolverlo al proveedor inmediatamente",
                        "Re-etiquetar con el código de barras correcto",
                        "Ajustarlo como merma",
                        "Dejarlo en el área de PF indefinidamente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Si el producto tiene todos los datos necesarios, se puede re-etiquetar y devolver al inventario normal.",
                },
                {
                    "pregunta": "¿Qué indicador ayuda a identificar si un proveedor específico tiene problemas de calidad de etiquetado?",
                    "opciones": [
                        "El precio de sus productos",
                        "La cantidad de PF asociada a ese proveedor en un período",
                        "El peso de sus entregas",
                        "El tiempo de entrega",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Un proveedor con alta frecuencia de PF indica un problema sistémico que debe comunicarse al área comercial.",
                },
            ],
            "practica": "Clasificar 5 casos de Problem Freight de ejemplo, proponer la solución para cada uno (re-etiquetar, re-embalar o devolver), documentar en el sistema y calcular el tiempo de resolución de cada caso.",
        },
        {
            "id": "raz",
            "nombre": "Resolución de RAZ",
            "procedimiento": "PR-QL-QA-RAZ-00",
            "objetivos": [
                "Entender qué es un RAZ y su importancia",
                "Ejecutar el proceso de resolución",
                "Documentar y dar seguimiento",
                "Implementar acciones correctivas efectivas",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es RAZ?",
                    "texto": "RAZ es un mecanismo de reporte y resolución de problemas operacionales que afectan la cadena de suministro. Funciona como un sistema de alertas formales que requieren investigación, acción correctiva y cierre documentado.",
                },
                {
                    "titulo": "Tipos de RAZ más comunes",
                    "texto": "• RAZ por discrepancia de inventario entre sistemas\n• RAZ por producto no encontrado\n• RAZ por error en recepciones\n• RAZ por diferencias en despacho\n• RAZ por incumplimiento de procedimientos\n• RAZ por problemas de calidad recurrentes",
                },
                {
                    "titulo": "Proceso de resolución",
                    "texto": "1. Recibir el reporte RAZ con todos los detalles\n2. Analizar la discrepancia reportada\n3. Investigar la causa raíz (5 Por qués si es necesario)\n4. Implementar acción inmediata (contención)\n5. Definir e implementar acción correctiva definitiva\n6. Documentar todo el proceso\n7. Cerrar el RAZ con evidencia de resolución\n8. Dar seguimiento para verificar que no se repite",
                },
                {
                    "titulo": "Herramienta: Los 5 Por qués",
                    "texto": "Para encontrar la causa raíz:\nEjemplo:\n¿Por qué? Hay faltante en inventario\n¿Por qué? No se registró un movimiento\n¿Por qué? El equipo RF falló\n¿Por qué? La batería estaba agotada\n¿Por qué? No hay procedimiento de control de carga de baterías\n\nAcción correctiva: Implementar control de carga de baterías.",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué se debe hacer después de implementar la acción correctiva en un RAZ?",
                    "opciones": [
                        "Nada más, el RAZ se cierra automáticamente",
                        "Documentar, cerrar el RAZ y dar seguimiento para verificar que no se repite",
                        "Esperar a que se repita el problema",
                        "Notificar solo verbalmente al equipo",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Todo RAZ debe documentarse y cerrarse formalmente, y luego verificarse que la acción fue efectiva.",
                },
                {
                    "pregunta": "¿Para qué sirve la metodología de los '5 Por qués' en un RAZ?",
                    "opciones": [
                        "Para calcular el costo del problema",
                        "Para encontrar la causa raíz y no solo resolver el síntoma",
                        "Para determinar quién tiene la culpa",
                        "Para escribir el informe más rápido",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Los 5 Por qués permiten profundizar hasta la causa raíz real, logrando que el problema no se repita.",
                },
                {
                    "pregunta": "¿Cuál es la diferencia entre acción inmediata y acción correctiva en un RAZ?",
                    "opciones": [
                        "Son lo mismo",
                        "La acción inmediata contiene el problema hoy; la correctiva evita que se repita",
                        "La inmediata es más importante que la correctiva",
                        "Solo se implementa una de las dos, nunca ambas",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La acción inmediata resuelve el problema del momento; la correctiva ataca la causa raíz para evitar recurrencia.",
                },
                {
                    "pregunta": "¿Qué evidencia debe incluirse al cerrar un RAZ?",
                    "opciones": [
                        "Solo el texto de la acción tomada",
                        "Evidencia de que la acción correctiva fue implementada y el problema resuelto",
                        "La firma del gerente es suficiente",
                        "No requiere evidencia, basta el reporte verbal",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El cierre del RAZ debe incluir evidencia concreta (fotos, registros, datos) de que el problema fue resuelto.",
                },
            ],
            "practica": "Resolver 2 RAZ de ejemplo usando la metodología completa: recibir reporte, aplicar 5 Por qués para causa raíz, definir acción inmediata y correctiva, documentar y cerrar con evidencia.",
        },
    ],
}
