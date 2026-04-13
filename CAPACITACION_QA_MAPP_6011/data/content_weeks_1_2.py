"""Training content for Weeks 1 and 2 - CD Quilicura QA.

Based on official procedures:
- PR-QL-QA-AR-00  Auditoría de Recepción
- PR-QL-QA-AA-00  Auditoría de Andén
- PR-QL-QA-APP-00 Auditoría de Preparación de Pedidos
- PR-QL-QA-ARV-00 Auditoría de Reservas Vacías
- Instructivos Ajuste 4, 10 y 11 (GLS Citrix)
"""

WEEK_1 = {
    "semana": 1,
    "titulo": "Fundamentos y Auditorías",
    "descripcion": "Procesos base de auditoría del área QA: recepción, andén, preparación y reservas vacías.",
    "modulos": [
        {
            "id": "aud_recepcion",
            "nombre": "Auditoría de Recepción",
            "procedimiento": "PR-QL-QA-AR-00",
            "objetivos": [
                "Iniciar sesión correctamente en la RF con GLS 2.0 QA Handheld",
                "Seleccionar la opción 'Perform receiving dock' en la RF",
                "Verificar fecha de vencimiento, producto y estiba del pallet",
                "Aplicar códigos de error correctamente y reportar al grupo WhatsApp",
            ],
            "contenido": [
                {
                    "titulo": "Herramientas y acceso al sistema",
                    "texto": "Para iniciar la auditoría de recepción necesitas una RF (Radio Frecuencia).\n\nPasos de ingreso al sistema:\n1. Abrir aplicación 'Remote Desktop' en la RF\n2. Seleccionar: GLS Classic D (connect) \u2192 OK\n3. Seleccionar: GLS 2.0 QA Handheld \u2192 OK\n4. Iniciar sesión con tus credenciales GLS/Citrix\n\nSiempre debes iniciar sesión con TUS propias credenciales.",
                },
                {
                    "titulo": "Selección del tipo de auditoría",
                    "texto": "Dentro del sistema GLS, seleccionar la opción:\n\u2022 'Perform receiving dock' \u2192 Para auditoría de recepción\n\nDirecciones a la zona de recepción. De forma aleatoria, selecciona un pallet armado y escanea su etiqueta SST con la RF.\n\nSST: Etiqueta para ser levantada proveniente de Recepción.",
                },
                {
                    "titulo": "Verificaciones obligatorias por pallet",
            "texto": "En cada pallet auditado debes verificar:\n\n1. Fecha de vencimiento: lo que muestra la etiqueta SST debe coincidir con el sistema\n2. Producto: el producto en el pallet debe ser el que indica la etiqueta\n3. Estiba: correcta distribución de cajas en el pallet\n4. Estado del pallet: sin merma visible\n5. Cantidad de cajas: verificar en opción 'Quantity VNPK' el total de cajas\n6. Fecha del día: ingresar en opción 'Received date 1'\n7. Fecha de Vencimiento: Revisar la fecha de vencimiento mas proxima del pallet, donde en la etiqueta debe de reflejarse la misma, de lo contrario deberiamos revisar nuestra tabla de excepciones. \n\nSi todo está correcto: seleccionar 'no exception'.",
                },
                {
                    "titulo": "Códigos de error y reporte",
                    "texto": "Cuando hay una no conformidad, ingresar el código de error en la RF junto con la cantidad de cajas:\n\nFormato RF: Código + Cantidad de cajas indicada en etiqueta\n\nCaso especial: Código 40 (Impresión >10 / Corbata) no aplica para:\n\u2022 Ways Plátanos\n\u2022 Paltas\n\u2022 Productos de maduración recibidos a camión completo\n\nTodo error debe reportarse con foto al grupo WhatsApp:\n'Grupo Auditoría de Recepción'",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Cuál es la ruta correcta para ingresar al sistema de auditoría en la RF?",
                    "opciones": [
                        "Abrir GLS directamente sin Remote Desktop",
                        "Remote Desktop \u2192 GLS Classic D (connect) \u2192 OK \u2192 GLS 2.0 QA Handheld \u2192 OK",
                        "TELNET \u2192 Surtido Pedido \u2192 F6",
                        "Operations \u2192 Inventory Adjustment \u2192 Create Label",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La ruta oficial es: Remote Desktop \u2192 GLS Classic D (connect) \u2192 OK \u2192 GLS 2.0 QA Handheld \u2192 OK, luego ingresar credenciales propias.",
                },
                {
                    "pregunta": "¿Qué opción seleccionar en la RF para la auditoría de recepción?",
                    "opciones": [
                        "Shipping Container",
                        "Perform cycle count",
                        "Perform receiving dock",
                        "Manual Audit",
                    ],
                    "respuesta_correcta": 2,
                    "explicacion": "'Perform receiving dock' es la opción específica para la auditoría de recepción. 'Shipping Container' es para andén.",
                },
                {
                    "pregunta": "¿Qué es una etiqueta SST?",
                    "opciones": [
                        "Etiqueta de una contenedora preparada por un seleccionador",
                        "Etiqueta para ser levantada proveniente de Recepción",
                        "Etiqueta de una contenedora perdida",
                        "Etiqueta del slot de auditoría virtual",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "SST es la etiqueta para ser levantada proveniente de Recepción, diferente a la DCL que corresponde a contenedoras de preparación de pedidos.",
                },
                {
                    "pregunta": "Si no se encuentra coincidencia en la cantidad de cajas, ¿qué debes hacer?",
                    "opciones": [
                        "Seleccionar 'no exception' y continuar",
                        "Informar al grupo WhatsApp 'Grupo Auditoría de Recepción' con foto e ingresar el código de error en la RF",
                        "Ignorar si la diferencia es de sólo 1 caja",
                        "Hacer ajuste directo en el sistema sin reportar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre reportar al WhatsApp 'Grupo Auditoría de Recepción' con foto de la etiqueta y registrar el código de error en la RF.",
                },
                {
                    "pregunta": "¿A qué productos NO aplica el código de error 40 (Corbata)?",
                    "opciones": [
                        "Productos congelados importados",
                        "Ways Plátanos, Paltas y productos de maduración recibidos a camión completo",
                        "Productos de fiambrería",
                        "Todos los productos válidos aplica el código 40",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El código 40 excluye expresamente: Ways Plátanos, Paltas y cualquier producto de maduración recibido a camión completo.",
                },
            ],
            "practica": "Ir a la zona de recepción, iniciar sesión en la RF con tus credenciales, seleccionar 'Perform receiving dock', auditar 5 pallets de forma aleatoria verificando todos los campos obligatorios y registrar los hallazgos según el procedimiento.",
        },
        {
            "id": "aud_anden",
            "nombre": "Auditoría de Andén",
            "procedimiento": "PR-QL-QA-AA-00",
            "objetivos": [
                "Seleccionar la opción correcta en GLS: 'Shipping Container' \u2192 'Manual Audit'",
                "Identificar errores de cruzamiento (código 9) y marcarlos con bandérn rojo",
                "Verificar coincidencia entre etiqueta DCL y slot (puerta) físico",
                "Reportar no conformidades al grupo WhatsApp correctamente",
            ],
            "contenido": [
                {
                    "titulo": "Inicio de sesión y selección de auditoría",
                    "texto": "Para la auditoría de andén:\n\n1. Acceder a la RF con Remote Desktop \u2192 GLS Classic D \u2192 GLS 2.0 QA Handheld\n2. Iniciar sesión con credenciales GLS/Citrix propias\n3. Seleccionar la opción: 'Shipping Container'\n4. Luego seleccionar: 'Manual Audit'\n5. Dirigirse caminando hacia la zona de Andén",
                },
                {
                    "titulo": "Proceso de auditoría en andén",
                    "texto": "En la zona de andén:\n\n1. Seleccionar un pallet de forma ALEATORIA\n2. Escanear la etiqueta DCL con la RF\n   - DCL: Etiqueta de una contenedora ya preparada por un seleccionador\n3. Verificar que el número de etiqueta y slot (puerta) del sistema coincidan con la información física\n4. Una vez revisado, seleccionar opción 'skip audit'\n5. Confirmar el número de puerta ingresando el código ST seguido del número de puerta\n   Ejemplo: ST004 para la puerta 4",
                },
                {
                    "titulo": "Código 9: Cruzamiento",
                    "texto": "El error más crítico en auditoría de andén es el CRUZAMIENTO (código 9):\n\n\u2022 Cruzamiento = El número de Slot que indica la etiqueta NO coincide con el número de puerta física donde está el pallet\n\nCuando detectas un cruzamiento:\n1. Colocar un BANDÉRÍN ROJO en el pallet con error\n2. Sacar fotografía a la etiqueta y al pallet con el bandérn\n3. Indicar la puerta en la aplicación AIM\n4. Reportar al WhatsApp: 'Grupo de Auditoría Andén' con foto de la etiqueta y el respaldo del error",
                },
                {
                    "titulo": "Fin de jornada",
                    "texto": "Cuando tu jornada esté próxima a finalizar:\n\u2022 Desasignar TODOS tus implementos de trabajo\n\u2022 Dejar la RF cargando para el turno siguiente\n\nCada pallet completado: continuar con otro de forma aleatoria cumpliendo la cantidad de pallets a auditar por día.",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué es una etiqueta DCL?",
                    "opciones": [
                        "Etiqueta para ser levantada proveniente de Recepción",
                        "Etiqueta correspondiente a una contenedora (pallet) ya preparada por un seleccionador de pedidos",
                        "Etiqueta ficticia creada para cada caja dentro de un pallet",
                        "Etiqueta del slot virtual de auditoría",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "DCL es la etiqueta que identifica una contenedora completa ya preparada y lista para despacho. Es diferente a la SST (recepción) y a la PKL (por caja).",
                },
                {
                    "pregunta": "¿Qué significa el código 9 en la auditoría de andén?",
                    "opciones": [
                        "El pallet está en perfectas condiciones",
                        "Cruzamiento: el slot de la etiqueta no coincide con la puerta física donde está el pallet",
                        "El pallet tiene fecha de vencimiento próxima",
                        "El pallet está dañado físicamente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El código 9 indica cruzamiento: la etiqueta indica una puerta diferente a donde está físicamente el pallet. Es el error más crítico en andén.",
                },
                {
                    "pregunta": "¿Qué debes hacer cuando detectas un cruzamiento (código 9)?",
                    "opciones": [
                        "Corregir el slot en el sistema sin reportar",
                        "Colocar bandérn rojo, fotografiar el pallet y la etiqueta, indicar puerta en AIM y reportar al WhatsApp",
                        "Ignorarlo si el pallet va al mismo local",
                        "Mover el pallet a la puerta correcta sin registrar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El protocolo de cruzamiento es: bandérn rojo + foto de etiqueta + foto pallet con bandérn + indicar puerta en AIM + reporte al WhatsApp 'Grupo Auditoría Andén'.",
                },
                {
                    "pregunta": "¿Qué opción del menú GLS se usa para la auditoría de andén?",
                    "opciones": [
                        "Perform receiving dock \u2192 Cycle Count",
                        "Shipping Container \u2192 Manual Audit",
                        "Operations \u2192 Inventory Adjustment",
                        "Maintenance \u2192 Item Details",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "'Shipping Container' \u2192 'Manual Audit' es la ruta correcta para la auditoría de andén en el sistema GLS.",
                },
            ],
            "practica": "Ir a la zona de andén, seleccionar 10 pallets de forma aleatoria, escanear cada DCL, verificar coincidencia con la puerta física, registrar en sistema con 'skip audit', reportar cualquier cruzamiento encontrado con foto al WhatsApp.",
        },
        {
            "id": "aud_preparacion",
            "nombre": "Auditoría de Preparación de Pedidos (SSTK)",
            "procedimiento": "PR-QL-QA-APP-00",
            "objetivos": [
                "Vincular el pallet al slot virtual AUDIT en TELNET",
                "Auditar el contenido de la DCL verificando PKL y UPC",
                "Registrar errores con la nomenclatura F/S/M correctamente",
                "Aplicar las correcciones y cerrar el pallet con film y cinta de auditoría",
            ],
            "contenido": [
                {
                    "titulo": "Inicio y preparación",
                    "texto": "El auditor inicia sesión en la RF tanto en TELNET como en Citrix.\n\nUsa una TRANSPALETA ELÉCTRICA y se dirige a una Buffer. Si no hay pallet en buffer, va a un andén aleatorio del CD.\n\nToma un pallet desde la Buffer o andén (si es del andén, NO debe estar siendo cargado) y lo lleva al sector de auditoría.",
                },
                {
                    "titulo": "Vinculación al slot AUDIT en TELNET",
                    "texto": "Al llegar al sector de auditoría:\n\n1. Vincular el pallet al slot virtual AUDIT en TELNET\n   \u2022 Esto permite que el sistema sepa que el pallet está siendo auditado\n   \u2022 El sistema registra la ubicación del pallet como 'AUDIT'\n\n2. Luego, escanear el código de barras en la DCL con la RF Citrix\n   \u2022 Se mostrarán todas las PKL contenidas en esa DCL\n   \u2022 PKL: Etiqueta ficticia creada para cada caja dentro del pallet",
                },
                {
                    "titulo": "Proceso de revisión por tipo de cámara",
                    "texto": "La revisión depende del tipo de cámara:\n\n• Panadería, Fiambrería, Congelado, Seco: DESARMAR el pallet completo\n• Vegetales: Solo desarmar si tiene productos surtidos por unidad o filete de mango\n• Carnes: Si los descriptivos están hacia afuera NO es necesario desarmar; de lo contrario sí\n\nEscanear cada caja por su código UPC (o validar por descripción si es peso variable).",
                },
                {
                    "titulo": "Nomenclatura de errores y consecuencias",
                    "texto": "Si se detectan errores, registrar en planilla Excel con la nomenclatura:\n\n\u2022 F = Faltante (caja que debería estar pero no está)\n\u2022 S = Sobrante (caja extra que no debería estar)\n\u2022 M = Merma (producto dañado)\n\nFormato: F703020X1-S577434X2 (código del error + item + cantidad)\n\nConsecuencias GDI:\n• 1 a 4 cajas con error \u2192 Proceso de mejora\n• 5 cajas o más \u2192 Carta de amonestación\n\nSiempre enviar evidencia fotográfica al WhatsApp 'Auditoría SSTK'.",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Para qué sirve vincular el pallet al slot virtual AUDIT en TELNET?",
                    "opciones": [
                        "Para hacer el ajuste negativo del pallet",
                        "Para que el sistema registre que ese pallet está siendo auditado y se sepa su ubicación",
                        "Para imprimir la etiqueta de auditoría",
                        "Para bloquear el pallet de despacho permanentemente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El slot AUDIT permite visibilidad sistémica del pallet durante la auditoría; todos saben que está siendo revisado y no se despacha por error.",
                },
                {
                    "pregunta": "¿Qué significa PKL?",
                    "opciones": [
                        "Etiqueta de recepción de pallet",
                        "Etiqueta ficticia creada para cada caja dentro de un pallet",
                        "Etiqueta de contenedora preparada por seleccionador",
                        "Código de error de auditoría",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "PKL es la etiqueta ficticia asignada a cada caja individual dentro de la contenedora DCL. Se escanea para validar el contenido.",
                },
                {
                    "pregunta": "Un pallet de la cámara de Fiambrería, ¿se debe desarmar para la auditoría?",
                    "opciones": [
                        "No, solo se revisa visualmente por fuera",
                        "Sí, se debe desarmar el pallet completo",
                        "Solo si tiene más de 50 cajas",
                        "Depende del supervisor",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Fiambrería es una de las cámaras donde SIEMPRE se debe desarmar el pallet completo para auditar correctamente.",
                },
                {
                    "pregunta": "¿Qué consecuencia tiene encontrar 5 cajas o más con error en una DCL?",
                    "opciones": [
                        "Proceso de mejora en el sistema GDI",
                        "Carta de amonestación en el sistema de Gestión de Desempeño Individual",
                        "Ningún registro, es solo aviso verbal",
                        "Suspensión inmediata del turno",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Según el procedimiento PR-QL-QA-APP-00: 1-4 cajas con error = proceso de mejora; 5 cajas o más = carta de amonestación en el GDI.",
                },
                {
                    "pregunta": "¿Cómo se registra que un pallet de peso variable fue auditado sin error?",
                    "opciones": [
                        "Solo se cierra con film y no se deja registro",
                        "Se escribe 'PVOK: Peso Variable OK' en la observación",
                        "Se usa el código M en la planilla",
                        "Se anota en el grupo WhatsApp 'Auditoría SSTK'",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Para pallets de peso variable sin error, el registro correcto en la observación es 'PVOK: Peso Variable OK'.",
                },
            ],
            "practica": "Tomar 2 pallets desde la buffer, vincularlos al slot AUDIT en TELNET, escanear todas las PKL en Citrix, verificar contenido por tipo de cámara, registrar cualquier hallazgo con la nomenclatura F/S/M y cerrar los pallets con film y cinta de auditoría.",
        },
        {
            "id": "aud_reservas",
            "nombre": "Auditoría de Reservas Vacías",
            "procedimiento": "PR-QL-QA-ARV-00",
            "objetivos": [
                "Seleccionar la opción 'Perform cycle count' en la RF",
                "Revisar reservas vacías siguiendo el calendario del supervisor",
                "Registrar pallets encontrados en reservas vacías en el SharePoint",
                "Utilizar la planilla de reserva Excel para filtrar módulos",
            ],
            "contenido": [
                {
                    "titulo": "Qué es la Auditoría de Reservas Vacías",
                    "texto": "Una reserva vacía es aquella que el sistema indica que tiene producto, pero físicamente está desocupada (o viceversa). La auditoría de reservas vacías detecta estas discrepancias entre el sistema y la realidad física.",
                },
                {
                    "titulo": "Acceso al sistema y selección",
                    "texto": "Inicio:\n1. RF con Remote Desktop \u2192 GLS Classic D \u2192 GLS 2.0 QA Handheld\n2. Iniciar sesión con credenciales propias\n3. Seleccionar: 'Perform cycle count' \u2192 luego 'cycle count'\n\nAlternativamente, el proceso puede realizarse desde un Excel/Planilla de reserva.\n\n**Siempre seguir el calendario establecido por el Supervisor.**",
                },
                {
                    "titulo": "Proceso de revisión física",
                    "texto": "1. Crear trip de Reservas Vacías en GLS\n2. Revisar en Citrix los módulos vacíos\n3. Dirigirse a la cámara respectiva\n4. Hacer INSPECCIÓN VISUAL de los módulos para detectar reservas vacías\n5. Escanear con la RF hasta agotar las reservas vacías del trip\n\nPlanilla de reserva: Macro en Excel que muestra trips creados; permite filtrar por módulo, slot par/impar y cantidad de cajas.",
                },
                {
                    "titulo": "Registro de incidentes",
                    "texto": "Si se detecta un pallet en reserva que figura vacía en el sistema:\n\u2022 Dejar registro en el SharePoint 'Reservas Vacías' con los datos que solicita la plataforma\n\nSi se detecta una reserva que figure vacía en sistema pero tiene mercadería física:\n\u2022 Reportar al supervisor para tomar acciones correctivas",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Qué opción de la RF se usa para la auditoría de reservas vacías?",
                    "opciones": [
                        "Shipping Container \u2192 Manual Audit",
                        "Perform receiving dock",
                        "Perform cycle count \u2192 cycle count",
                        "Operations \u2192 Inventory Adjustment",
                    ],
                    "respuesta_correcta": 2,
                    "explicacion": "'Perform cycle count' \u2192 'cycle count' es la opción en la RF para la auditoría de reservas vacías.",
                },
                {
                    "pregunta": "¿Qué es la Planilla de Reserva?",
                    "opciones": [
                        "Un reporte del sistema GLS de reservas disponibles",
                        "Una macro en Excel que permite visualizar trips creados, filtrar por módulo, slot par/impar y cantidad de cajas",
                        "El formulario de SharePoint para registrar incidentes",
                        "La planilla de sanciones GDI del área QA",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La Planilla de Reserva es una macro Excel que permite visualizar todos los trips creados y filtrar por módulo, slot par/impar y cantidad de cajas.",
                },
                {
                    "pregunta": "¿Si se detecta un pallet en una reserva que figura vacía en el sistema, qué se hace?",
                    "opciones": [
                        "Ignorarlo, el sistema se actualizará solo",
                        "Dejar registro en el SharePoint 'Reservas Vacías' con los datos requeridos",
                        "Hacer un ajuste 28 inmediatamente",
                        "Mover el pallet a otro slot sin registrar",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El incidente debe registrarse en el SharePoint 'Reservas Vacías' con todos los datos que solicita la plataforma para trazabilidad.",
                },
                {
                    "pregunta": "¿Quién define el calendario de auditorías de reservas vacías?",
                    "opciones": [
                        "El auditor lo decide según su disponibilidad",
                        "El supervisor establece el calendario que debe seguirse",
                        "El sistema GLS genera automáticamente el calendario",
                        "Se realiza solo cuando hay tiempo libre",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Según el procedimiento: 'Se rige por calendario establecido por el Supervisor.' El auditor debe seguir ese calendario.",
                },
            ],
            "practica": "Revisar el calendario del supervisor para el día, crear el trip de Reservas Vacías en GLS, dirigirse a la cámara asignada, hacer inspección visual y escanear las reservas vacías. Si hay incidentes, registrar en el SharePoint 'Reservas Vacías'.",
        },
    ],
}

WEEK_2 = {
    "semana": 2,
    "titulo": "Ajustes de Inventario - Parte 1",
    "descripcion": "Ajuste 4 (Transfer), Ajuste 10 (Store Return) y Ajuste 11 (Damages) en GLS Citrix.",
    "modulos": [
        {
            "id": "ajuste_4",
            "nombre": "Ajuste 4 - Transfer (item to item)",
            "procedimiento": "Instructivo PPT Ajuste 4",
            "objetivos": [
                "Entender que el Ajuste 4 transfiere mercadería entre ítems de distintos formatos",
                "Ejecutar el ajuste positivo en Citrix: Operations \u2192 Inventory Adjustment \u2192 Create Label",
                "Ejecutar el ajuste negativo: Operations \u2192 Inventory Adjustment \u2192 Inventory Adjustment",
                "Mover la contenedora al slot correcto después del ajuste",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Ajuste 4?",
                    "texto": "El Ajuste 4 (Transfer - item to item) aplica para mercadería que debe ser transferida de un ítem a otro que pertenecen a distintos formatos.\n\nEjemplo: Express 400 \u2013 Ways \u2013 Hiper\n\nAlgunas razones de uso:\n\u2022 Sobre stock en un formato\n\u2022 Regularización entre formatos\n\nControl de Inventario debe dirigirse al lugar donde está físicamente la mercadería para verificar: cantidad de cajas, fecha de rotación, ítem.",
                },
                {
                    "titulo": "Ajuste Positivo: Create Label",
                    "texto": "Para crear el ajuste positivo en GLS Citrix:\n\n1. Ingresar en Citrix\n2. Seleccionar: Operations \u2192 Inventory Adjustment \u2192 Create Label\n3. Escribir el ítem en el campo 'Item Number'\n4. El sistema solicitará: 'Do you want to create a new label? Yes/No' \u2192 Responder YES\n5. El sistema asigna una reserva disponible (ejemplo: P5937)\n6. En el campo 'To Slot' (amarillo), escribir la ubicación destino\n7. Presionar 'Move'\n\nEl sistema hará 3 preguntas de confirmación (contestar según instruccion).",
                },
                {
                    "titulo": "Preguntas del sistema al presionar 'Move'",
                    "texto": "Al presionar 'Move', el sistema hace 3 preguntas:\n\n1. Are you sure you want to move the pallet? Yes/No\n   (\u00bfEstá seguro de que desea mover el pallet?)\n\n2. Do you want to create the cycle count? Yes/No\n   (\u00bfDesea crear conteo cíclico?)\n\n3. Do you want to send move instruction to the lift driver?\n   (\u00bfDesea enviar instrucción de movimiento al conductor del elevador?)",
                },
                {
                    "titulo": "Ajuste Negativo y pasos finales",
                    "texto": "Para el ajuste tipo 4 NEGATIVO:\n\n1. Ingresar en Citrix: Operations \u2192 Inventory Adjustment \u2192 Inventory Adjustment\n2. Importar las contenedoras en el campo 'Import'. Pinchar '>>' y luego 'Retrieve'\n3. Seleccionar todo. Verificar que sea la contenedora e ítem a ajustar, la cantidad y el slot\n\nPasos finales para AMBOS ajustes (positivo y negativo):\n\u2022 Imprimir las etiquetas ajustadas y pegarlas en los pallets\n\u2022 Usar 'Slot Maintenance' para buscar slots disponibles para almacenar\n\u2022 Si se importan etiquetas: copiar en block de notas \u2192 guardar como archivo \u2192 importar en SSTK",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Para qué se usa el Ajuste 4?",
                    "opciones": [
                        "Para dar de baja productos dañados internamente",
                        "Para transferir mercadería de un ítem a otro entre distintos formatos (Express, Ways, Hiper)",
                        "Para devolver mercadería a un proveedor",
                        "Para registrar una donación",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El Ajuste 4 (Transfer item to item) es específico para transferir mercadería entre ítems de distintos formatos de tienda.",
                },
                {
                    "pregunta": "¿Por qué ruta en Citrix se hace el ajuste positivo del Ajuste 4?",
                    "opciones": [
                        "Operations \u2192 Inventory Adjustment \u2192 Inventory Adjustment",
                        "Operations \u2192 Inventory Adjustment \u2192 Create Label",
                        "Maintenance \u2192 Item Details \u2192 Indicators",
                        "Operations \u2192 Pallet Label Operations \u2192 Shipping Details",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El ajuste positivo del Ajuste 4 usa: Operations \u2192 Inventory Adjustment \u2192 Create Label para crear la nueva etiqueta con el ítem destino.",
                },
                {
                    "pregunta": "Al presionar 'Move' en GLS, ¿cuántas preguntas hace el sistema?",
                    "opciones": [
                        "Una sola",
                        "Dos preguntas",
                        "Tres preguntas",
                        "Ninguna, se ejecuta directo",
                    ],
                    "respuesta_correcta": 2,
                    "explicacion": "Al presionar 'Move' en GLS Citrix, el sistema siempre hace 3 preguntas de confirmación antes de ejecutar el movimiento.",
                },
                {
                    "pregunta": "¿Qué debe hacer Control de Inventario ANTES de ejecutar cualquier ajuste?",
                    "opciones": [
                        "Ejecutar el ajuste directamente desde la oficina",
                        "Dirigirse físicamente al lugar donde está la mercadería para verificar cantidad, fecha y ítem",
                        "Notificar al proveedor del cambio",
                        "Esperar la aprobación automática del sistema",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Siempre verificar físicamente antes de ajustar: cantidad de cajas, fecha de rotación e ítem en la ubicación declarada.",
                },
            ],
            "practica": "Practicar el flujo completo del Ajuste 4: ir a la ubicación física, verificar, ingresar a Citrix con Create Label para el positivo, luego ejecutar el negativo en Inventory Adjustment, responder las 3 preguntas del sistema, imprimir etiquetas y usar Slot Maintenance para almacenar.",
        },
        {
            "id": "ajuste_10",
            "nombre": "Ajuste 10 - Store Return",
            "procedimiento": "Instructivo PPT Ajuste 10",
            "objetivos": [
                "Identificar los casos que generan un Store Return",
                "Ejecutar el proceso de reingreso de mercadería en GLS Citrix",
                "Almacenar correctamente la mercadería devuelta",
                "Entender las diferencias con el Ajuste 4",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Ajuste 10?",
                    "texto": "El Ajuste 10 (Store Return) aplica para mercadería que debe ser REINGRESADA al inventario del CD. La mercadería es devuelta por distintas razones:\n\n\u2022 Local con sobre stock\n\u2022 SIF no autorizado\n\u2022 Daño mecánico\n\nCuando la mercadería arriba al CD, Control de Calidad debe realizar la revisión inicial correspondiente.",
                },
                {
                    "titulo": "Proceso en GLS Citrix",
                    "texto": "El proceso es similar al Ajuste 4:\n\n1. Control de Inventario se dirige a donde está la mercadería físicamente\n2. Verificar: cantidad de cajas, fecha de rotación, ítem\n3. Ingresar en Citrix: Operations \u2192 Inventory Adjustment \u2192 Create Label\n4. Escribir el ítem en campo 'Item Number'\n5. El sistema pregunta: 'Do you want to create a new label?' \u2192 YES\n6. El sistema asigna una reserva disponible\n7. En el campo 'To Slot' (amarillo), escribir la ubicación\n8. Presionar 'Move' (responder las 3 preguntas del sistema)",
                },
                {
                    "titulo": "Almacenaje y cierre del proceso",
                    "texto": "Una vez ejecutado el ajuste:\n\n1. Imprimir las etiquetas ajustadas y pegarlas en los pallets correspondientes\n2. Ingresar en Citrix: Maintenance \u2192 Slot Maintenance\n3. Buscar slots disponibles para almacenar la mercadería devuelta\n4. Presionar 'Move' para ubicar la mercadería\n5. Verificar que el sistema refleja el nuevo stock correctamente",
                },
                {
                    "titulo": "Diferencias clave con Ajuste 4",
                    "texto": "Ajuste 4 vs Ajuste 10:\n\n\u2022 Ajuste 4 (Transfer): Transferencia entre ítems de distintos FORMATOS (Express/Ways/Hiper)\n\u2022 Ajuste 10 (Store Return): Reingreso de mercadería DEVUELTA desde una tienda al CD\n\nAmbos usan el mismo proceso sistémico en Citrix (Create Label), la diferencia está en la RAZÓN del ajuste y el flujo que lo origina.",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Cuál de las siguientes situaciones genera un Ajuste 10?",
                    "opciones": [
                        "Un pallet dañado por el montacarga en la cámara",
                        "Un local devuelve mercadería al CD por sobre stock",
                        "Una contenedora perdida en el andén",
                        "Un producto con fecha de vencimiento próxima a vencer",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El Ajuste 10 (Store Return) aplica cuando una tienda devuelve mercadería al CD, ya sea por sobre stock, SIF no autorizado o daño mecánico.",
                },
                {
                    "pregunta": "¿Cuál es la diferencia principal entre Ajuste 4 y Ajuste 10?",
                    "opciones": [
                        "El Ajuste 10 solo aplica para productos congelados",
                        "El Ajuste 4 transfiere entre formatos; el Ajuste 10 reingresa mercadería devuelta desde una tienda",
                        "El Ajuste 10 usa una ruta diferente en Citrix",
                        "No hay diferencia, ambos son idénticos",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La diferencia es la razón y el flujo: el Ajuste 4 transfiere entre ítems de distintos formatos y el Ajuste 10 reingresa mercadería que fue devuelta por una tienda.",
                },
                {
                    "pregunta": "¿Qué se hace con los pallets después del Ajuste 10?",
                    "opciones": [
                        "Se dejan en el andén hasta el próximo inventario",
                        "Se imprimen etiquetas, se pegan en pallets y se almacenan buscando slot con 'Slot Maintenance'",
                        "Se devuelven al proveedor de inmediato",
                        "Se donan automáticamente",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Tras el Ajuste 10 se imprimen las etiquetas, se pegan en los pallets y se usa Slot Maintenance para encontrar un slot disponible donde almacenar.",
                },
                {
                    "pregunta": "¿Qué verifica Control de Calidad cuando arriba la mercadería devuelta?",
                    "opciones": [
                        "Solo cuenta la cantidad de cajas",
                        "Realiza la revisión inicial de la mercadería devuelta",
                        "Ejecuta el ajuste directamente en el sistema",
                        "Notifica al proveedor antes de cualquier acción",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Cuando la mercadería arriba al CD, Control de Calidad realiza primero la revisión inicial antes de que Control de Inventario ejecute el ajuste.",
                },
            ],
            "practica": "Simular un Store Return: revisar físicamente la mercadería devuelta, ingresar al Citrix con Create Label, ejecutar el ajuste con el ítem correcto, imprimir etiquetas, usar Slot Maintenance y almacenar en la cámara correspondiente.",
        },
        {
            "id": "ajuste_11",
            "nombre": "Ajuste 11 - Damages (Mermas del CD)",
            "procedimiento": "Instructivo PPT Ajuste 11",
            "objetivos": [
                "Reconocer los tipos de merma que aplica el Ajuste 11",
                "Iniciar el proceso a través de la plataforma Máximo con link SharePoint",
                "Ejecutar 'Initiate' en SSTK para separar la caja a ajustar",
                "Mover la etiqueta al gafete del supervisor (ej. MVALE) y ejecutar el ajuste a cero",
            ],
            "contenido": [
                {
                    "titulo": "¿Qué es el Ajuste 11?",
                    "texto": "El Ajuste 11 (Damages) aplica para mercadería que ha sido MERMADA en el CD por distintas razones:\n\n\u2022 Hurto\n\u2022 Consumo\n\u2022 Volcamiento\n\nEl proceso inicia cuando el área solicitante hace una solicitud a través de la plataforma MÁXIMO adjuntando un link de SharePoint con el detalle de las mermas (\u22c4 Link Mermas).",
                },
                {
                    "titulo": "Inicio en SSTK: paso Initiate",
                    "texto": "Una vez recibida la solicitud en Máximo:\n\n1. Ingresar en Citrix: Operations \u2192 Pallet Label Operations \u2192 Receiving Label Management (SSTK)\n2. Copiar el ítem que declara el solicitante y pegarlo en el campo 'Item Number'\n3. El stock disponible se mostrará en pantalla\n\n4. Presionar 'Initiate': este proceso divide el pallet separando EXACTAMENTE la cantidad de cajas a ajustar\n5. En la pantalla Initiate Label: escribir en 'Quantity' la cantidad de cajas a descontar\n6. Pinchar 'Initiate Label' y confirmar 'Do you want to create cycle count?' \u2192 responder según instrucción",
                },
                {
                    "titulo": "Mover al gafete del supervisor",
                    "texto": "Después del Initiate:\n\n1. Seleccionar la etiqueta dividida y presionar 'Move'\n2. Escribir el GAFETE DEL SUPERVISOR según la categoría\n   Ejemplo: MVALE (cada supervisor tiene su gafete identificado)\n3. Presionar 'Move' y responder las 3 preguntas del sistema\n\nEl gafete es la ubicación virtual de ajuste asignada a cada supervisor de cámara.",
                },
                {
                    "titulo": "Ejecución del ajuste y RAZ de respaldo",
                    "texto": "Para ejecutar el ajuste en Citrix:\n\n1. Operations \u2192 Inventory Adjustment \u2192 Inventory Adjustment\n2. Seleccionar: 'Receiving Label Search', habilitar campo 'Slot ID'\n3. Escribir el gafete del supervisor en 'Slot ID' y pinchar 'Retrieve'\n4. Seleccionar etiqueta, mover cursor a cero (0) \u2192 aparecerá el total en negativo\n5. Seleccionar razón de ajuste: Ajuste tipo 11\n6. Pinchar 'Apply to All' \u2192 luego 'Adjust'\n\nSi no hay cajas en prime: hacer primero Ajuste tipo 3 (Quantity Cut) y luego resolver desde RAZ (Operations \u2192 Resolve Requires Attention Zone Freight).",
                },
            ],
            "preguntas": [
                {
                    "pregunta": "¿Cuáles son los tipos de merma que aplica el Ajuste 11?",
                    "opciones": [
                        "Productos vencidos, donación y devolución a proveedor",
                        "Hurto, consumo y volcamiento",
                        "Transferencia entre formatos y sobre stock",
                        "Error de recepción y SIF no autorizado",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El Ajuste 11 (Damages) aplica para mermas del CD: hurto, consumo y volcamiento. No incluye vencimientos ni devoluciones.",
                },
                {
                    "pregunta": "¿Cómo inicia el proceso del Ajuste 11?",
                    "opciones": [
                        "Control de Inventario detecta la merma y ajusta directamente",
                        "El área solicitante hace una solicitud en la plataforma MÁXIMO adjuntando link de SharePoint",
                        "Se inicia automáticamente al final del turno",
                        "El supervisor aprueba verbalmente sin plataforma",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "El proceso siempre inicia con una solicitud formal en la plataforma MÁXIMO adjuntando el link de SharePoint con el detalle de las mermas.",
                },
                {
                    "pregunta": "¿Para qué sirve el paso 'Initiate' en el proceso del Ajuste 11?",
                    "opciones": [
                        "Para confirmar que el ajuste fue autorizado",
                        "Para dividir el pallet y separar exactamente las cajas a ajustar",
                        "Para crear una nueva etiqueta positiva",
                        "Para mover todo el pallet al gafete del supervisor",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "'Initiate' divide el pallet: separa exactamente la cantidad de cajas que se van a ajustar, dejando el resto del pallet intacto en el prime.",
                },
                {
                    "pregunta": "¿A qué ubicación se mueve la etiqueta antes del ajuste final?",
                    "opciones": [
                        "Al slot PERDI",
                        "Al gafete del supervisor asignado por categoría (ej. MVALE)",
                        "Al slot CVT12",
                        "Al slot ficticio QA (ETIQC o ETIQR)",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "La etiqueta se mueve al gafete del supervisor de la cámara correspondiente (ej. MVALE). Cada supervisor tiene su gafete identificado.",
                },
                {
                    "pregunta": "¿Qué hacer si no hay cajas en prime para ejecutar el Ajuste 11?",
                    "opciones": [
                        "Esperar a que haya reposición y luego ajustar",
                        "Hacer primero Ajuste tipo 3 (Quantity Cut) y luego resolver desde la pantalla RAZ",
                        "Cancelar el ajuste y notificar al solicitante",
                        "Ajustar directamente sin el paso Initiate",
                    ],
                    "respuesta_correcta": 1,
                    "explicacion": "Cuando no hay cajas en prime, se debe hacer primero Ajuste 3 (Quantity Cut) y luego resolver la etiqueta desde la pantalla RAZ (Resolve Requires Attention Zone Freight).",
                },
            ],
            "practica": "Simular el flujo completo del Ajuste 11: recibir solicitud de Máximo, ingresar al SSTK con el ítem, hacer Initiate con la cantidad correcta, mover al gafete del supervisor, ejecutar el ajuste a cero con razón 11, 'Apply to All' y 'Adjust'.",
        },
    ],
}
