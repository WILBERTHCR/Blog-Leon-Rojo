"""Fuente de las fichas de producto. Correr: python3 tools/fichas_src.py  -> escribe fichas/<id>.json (no toca las que ya existen).
Reglas: solo datos de productos.md/catalogo.json; cantidades, diluciones y tiempos siempre "lo que indica la etiqueta"."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ETQ = 'Seguí las cantidades y el modo de uso que indica la etiqueta.'
GEN = 'Leé la etiqueta antes de usar. Usá guantes, no lo mezclés con otros productos químicos y mantenelo fuera del alcance de niños y mascotas.'
SOLV = 'Producto inflamable. Usalo lejos de llamas, chispas y cigarros, en un lugar bien ventilado. Usá guantes y lentes, no respirés los vapores y mantenelo bien cerrado y fuera del alcance de niños. No lo mezclés con otros productos.'
PRES_MAD = 'Usá guantes, lentes y ropa que cubra la piel. Aplicalo en un lugar ventilado y no respirés los vapores. No lo usés en utensilios de cocina, comederos ni bebederos. Mantenelo cerrado, fuera del alcance de niños y mascotas, y leé siempre la etiqueta.'
PISC = 'Producto químico para tratamiento de agua. Usá guantes y lentes, no lo mezclés con otros químicos de piscina ni con ácidos, agregalo siempre al agua (nunca agua sobre el producto) y guardalo cerrado, en un lugar fresco y seco, fuera del alcance de niños.'

F = {
 'desengrasante': dict(
  intro='El Desengrasante Industrial León Rojo es el producto estrella de los talleres: remueve grasa, aceite y carbonilla de motores, piezas, maquinaria y pisos de taller. Viene listo para trabajar y rinde porque se diluye según el trabajo.',
  pasos=['Con el motor o la pieza fríos, protegé las partes eléctricas.', 'Diluilo según lo que indica la etiqueta para el tipo de suciedad.', 'Aplicalo con atomizador o brocha y dejalo actuar unos minutos.', 'Restregá las zonas más sucias con un cepillo.', 'Enjuagá con agua a baja presión y dejá secar.'],
  seguridad='Usá guantes y lentes de protección y trabajá en un lugar ventilado. No lo apliqués sobre el motor caliente ni lo mezclés con otros productos. Mantenelo fuera del alcance de niños y leé siempre la etiqueta.',
  faq=[['¿Sirve para pisos de taller?', 'Sí. Además de motores y piezas, se usa para quitar manchas de grasa y aceite en pisos de taller y en maquinaria.'], ['¿Hay que diluirlo?', 'Se puede diluir según el trabajo. La proporción correcta para cada uso viene en la etiqueta.']],
  blog='como-limpiar-el-motor-del-carro'),
 'quitagrasa': dict(
  intro='La Crema Quita Grasa León Rojo está hecha para mecánicos y gente de taller: quita la grasa, el aceite y la suciedad de las manos después del trabajo, sin necesidad de usar solventes.',
  pasos=['Aplicá un poco de crema sobre las manos secas.', 'Frotá bien, entre los dedos y alrededor de las uñas, hasta aflojar la grasa.', 'Enjuagá con abundante agua.', 'Secate bien las manos.'],
  seguridad='Uso externo. Evitá el contacto con los ojos; si sucede, enjuagá con abundante agua. Mantenela fuera del alcance de niños y leé la etiqueta.',
  faq=[['¿Es para manos o para piezas?', 'Es para las manos. Para piezas, motores y pisos de taller está el Desengrasante Industrial.'], ['¿Quiénes la usan?', 'Mecánicos, talleres e industria: todo el que termina el día con grasa y aceite en las manos.']]),
 'shampoo': dict(
  intro='El Shampoo para Autos León Rojo hace espuma para lavar la carrocería: quita el polvo y el barro sin opacar la pintura. Sirve para lavado en casa, lavacar y flotillas.',
  pasos=['Estacioná el carro a la sombra, con la carrocería fría.', 'Mezclá el shampoo con agua en un balde según la etiqueta.', 'Mojá el carro y lavá de arriba hacia abajo con esponja o guante de lavado.', 'Enjuagá bien con agua limpia.', 'Secá con un paño de microfibra para evitar manchas de agua.'],
  seguridad=GEN,
  faq=[['¿Le quita la cera al carro?', 'Está hecho para limpiar sin opacar la pintura. Si querés más brillo y protección, después del lavado aplicá la Cera en Pasta o la Cera Líquida para Autos León Rojo.'], ['¿Lo puedo usar en lavacar?', 'Sí, viene en galón justamente para lavacar y flotillas.']]),
 'polish': dict(
  intro='El Polish en Pasta León Rojo es una pasta pulidora para pintura automotriz: restaura el brillo de la pintura opaca y elimina microarañazos. Lo usan talleres de enderezado y pintura, detallado y lavacar.',
  pasos=['Lavá y secá bien la zona a pulir.', 'Trabajá a la sombra, con la pintura fría.', 'Aplicá un poco de pasta con un paño, esponja o pulidora.', 'Puli con movimientos circulares hasta que salga el brillo.', 'Retirá el residuo con un paño de microfibra limpio.'],
  seguridad=GEN,
  faq=[['¿Cuál es la diferencia entre polish y cera?', 'El polish pule y corrige la superficie (brillo y microarañazos). La cera se aplica después y deja una capa de protección y brillo.'], ['¿Sirve para quitar rayones profundos?', 'Está hecho para microarañazos y pintura opaca. Un rayón que llegó a la base o al metal necesita trabajo de pintura.']]),
 'cerapasta': dict(
  intro='La Cera en Pasta para Autos León Rojo deja una capa de brillo y protección sobre la pintura del carro. Es ideal para terminar el lavado o el pulido.',
  pasos=['Lavá y secá bien el carro.', 'Aplicá una capa delgada con un aplicador o paño suave, por secciones.', 'Dejá que la cera opaque un poco.', 'Retirá y dale brillo con un paño de microfibra limpio.'],
  seguridad=GEN,
  faq=[['¿La aplico antes o después del polish?', 'Después. Primero se pule con el Polish en Pasta y luego se protege con la cera.'], ['¿Se puede aplicar al sol?', 'Es mejor aplicarla a la sombra y con la pintura fría para que no se seque demasiado rápido.']]),
 'ceraliquidaauto': dict(
  intro='La Cera Líquida para Autos León Rojo viene en atomizador para dar brillo rápido a la carrocería. Es práctica para lavacar y para un detallado rápido en casa.',
  pasos=['Lavá y secá el carro.', 'Rociá la cera sobre una sección o sobre un paño de microfibra.', 'Distribuila de forma pareja.', 'Repasá con otro paño seco hasta que quede brillante.'],
  seguridad=GEN,
  faq=[['¿Qué diferencia tiene con la cera en pasta?', 'La líquida es más rápida de aplicar; la de pasta deja una capa más trabajada. Las dos dan brillo y protección.'], ['¿En qué presentación viene?', 'Viene en litro atomizador.']]),
 'restaurador': dict(
  intro='El Restaurador de Partes Negras León Rojo devuelve el color negro a los plásticos, molduras, bumpers y hules del carro que se ven opacos o grisáceos por el sol.',
  pasos=['Lavá y secá bien la pieza.', 'Aplicá una pequeña cantidad con un aplicador o paño.', 'Distribuilo de forma pareja sobre el plástico o el hule.', 'Retirá el exceso con un paño limpio.'],
  seguridad=GEN,
  faq=[['¿Sirve para las llantas?', 'Para llantas tenemos el Llantilux-80 y el Llantilux-1000, hechos especialmente para eso.'], ['¿Dónde se aplica?', 'En bumpers, molduras, plásticos exteriores y hules del carro.']]),
 'llantilux80': dict(
  intro='El Llantilux-80 León Rojo deja las llantas negras y brillantes, con acabado de recién lavado. Es el abrillantador de llantas para el día a día en lavacar, detallado o en casa.',
  pasos=['Lavá la llanta y dejala secar.', 'Aplicá el producto con aplicador, esponja o atomizador.', 'Distribuilo de forma pareja por toda la llanta.', 'Dejá secar antes de rodar.'],
  seguridad=GEN,
  faq=[['¿Cuál es la diferencia con el Llantilux-1000?', 'El Llantilux-1000 es la versión de alto poder para lavacar y detallado profesional. El 80 es ideal para el uso diario.'], ['¿Se aplica en los aros?', 'Se aplica en el hule de la llanta. Para aros de aluminio está el ALUX-500.']]),
 'llantilux1000': dict(
  intro='El Llantilux-1000 León Rojo es el abrillantador de llantas de alto rendimiento, pensado para lavacar y detallado profesional. Deja la llanta negra y brillante.',
  pasos=['Lavá la llanta y dejala secar.', 'Aplicá el producto con aplicador o esponja.', 'Distribuilo de forma pareja.', 'Dejá secar antes de rodar.'],
  seguridad=GEN,
  faq=[['¿Cuál es la diferencia con el Llantilux-80?', 'El 1000 es la versión de alto poder para trabajo profesional; el 80 es para el uso diario.'], ['¿En qué presentaciones viene?', 'Viene en litro y galón.']]),
 'abrillantador': dict(
  intro='El Abrillantador de Superficies León Rojo da brillo y renueva tableros, asientos, vinil y plásticos interiores del carro. Es un básico en cualquier lavacar.',
  pasos=['Limpiá el polvo de la superficie.', 'Aplicá el producto sobre un paño o directo en la superficie.', 'Distribuilo de forma pareja.', 'Repasá con un paño limpio y seco.'],
  seguridad=GEN,
  faq=[['¿Se puede usar en el volante y los pedales?', 'Mejor no: el brillo puede dejar esas superficies resbalosas.'], ['¿Sirve para asientos de vinil?', 'Sí, está hecho para tableros, asientos, vinil y plásticos interiores.']]),
 'alux': dict(
  intro='El ALUX-500 León Rojo es un limpiador de aluminio que devuelve el brillo a aros, perfiles, cajones de camión y tanques. Lo usan lavacar, transportistas y talleres.',
  pasos=['Ponete guantes y lentes y trabajá con la pieza fría y a la sombra.', 'Aplicá el producto según la etiqueta (diluido o directo).', 'Dejalo actuar el tiempo que indica la etiqueta, sin que se seque.', 'Restregá con un cepillo.', 'Enjuagá con abundante agua.'],
  seguridad='Usá guantes y lentes de protección y trabajá en un lugar ventilado. No lo apliqués sobre superficies calientes, pintura ni vidrio, y no lo mezclés con otros productos. Mantenelo fuera del alcance de niños y leé siempre la etiqueta.',
  faq=[['¿En qué superficies se usa?', 'En aluminio: aros, perfiles, cajones de camión y tanques.'], ['¿Viene listo para usar?', 'Revisá la etiqueta: ahí indica si se usa directo o diluido según el trabajo.']]),
 'coolant': dict(
  intro='El Coolant León Rojo es un refrigerante para el sistema de enfriamiento del motor. Se usa en radiadores de carros, talleres y flotillas.',
  pasos=['Revisá siempre con el motor frío: nunca abrás el radiador caliente.', 'Verificá el nivel en el radiador o en el depósito.', 'Agregá el coolant hasta el nivel que indica el vehículo.', 'Cerrá bien la tapa y revisá que no haya fugas.'],
  seguridad='Nunca abrás el radiador con el motor caliente. No es para tomar: mantenelo fuera del alcance de niños y mascotas. Leé la etiqueta antes de usar.',
  faq=[['¿Se puede usar agua en vez de coolant?', 'El coolant está hecho para el sistema de enfriamiento del motor. Para el tipo que pide tu carro, revisá el manual del vehículo.'], ['¿En qué presentación viene?', 'Viene en galón.']]),
 'grasa': dict(
  intro='La Grasa Multiusos León Rojo lubrica piezas, bisagras, rodamientos y mecanismos. Es la grasa roja que se usa en talleres, en maquinaria y en la casa.',
  pasos=['Limpiá la pieza y retirá la grasa vieja y la suciedad.', 'Aplicá una capa de grasa en la zona de roce.', 'Mové la pieza para que la grasa se distribuya.', 'Retirá el exceso con un trapo.'],
  seguridad=GEN,
  faq=[['¿En qué presentaciones viene?', 'Viene en potes de 1/32, 1/16, 1/8 y 1/4 de galón.'], ['¿Para qué se usa?', 'Para lubricar piezas, bisagras, rodamientos y mecanismos en talleres, maquinaria y en la casa.']]),
 'desoxidante': dict(
  intro='El Desoxidante de Metales León Rojo elimina el óxido de herramientas, piezas y superficies metálicas. Es el paso previo ideal antes de pintar.',
  pasos=['Ponete guantes y lentes y trabajá en un lugar ventilado.', 'Quitá el óxido suelto con cepillo de alambre o lija.', 'Aplicá el producto según la etiqueta.', 'Dejalo actuar el tiempo que indica la etiqueta.', 'Limpiá y secá bien la pieza antes de pintarla.'],
  seguridad='Producto químico. Usá guantes, lentes y buena ventilación. No lo mezclés con cloro ni con otros productos. Mantenelo cerrado y fuera del alcance de niños, y leé siempre la etiqueta.',
  faq=[['¿Sirve antes de pintar?', 'Sí, es para dejar el metal sin óxido antes de pintar.'], ['¿En qué presentaciones viene?', 'En 1/2 litro, litro y galón.']]),
 'aromatizante': dict(
  intro='El Aromatizante para Carro León Rojo viene en atomizador y deja el carro con olor agradable por días. Hay 10 aromas para escoger, y es muy usado en lavacar, taxis y busetas.',
  pasos=['Agitá el atomizador.', 'Rociá en alfombras, tapicería o el ambiente del carro.', 'Evitá rociar directo en el tablero, el vidrio o la cara.', 'Dejá ventilar un momento antes de cerrar el carro.'],
  seguridad='No lo rociés hacia la cara ni cerca de llamas. Mantenelo fuera del alcance de niños y leé la etiqueta.',
  faq=[['¿Qué aromas hay?', 'Fresa, Fresita, Manzana Canela, Cherry, Tuttifrutti, Fresa Mora, Herbal Fruit, Vainilla, Coco y New Car.'], ['¿Sirve para lavacar?', 'Sí, es uno de los productos que más se usan para entregar el carro con buen olor.']]),
 'desinfectante': dict(
  intro='El Desinfectante León Rojo es para uso doméstico e industrial: viviendas, comercios, oficinas, plantas empacadoras, lecherías, establos y áreas en general. Viene en 9 aromas y se puede diluir.',
  pasos=['Barré o retirá la suciedad suelta.', 'Diluilo en agua según lo que indica la etiqueta.', 'Aplicalo con trapeador, paño o atomizador.', 'Dejá secar al aire.'],
  seguridad='No lo mezclés con cloro, vinagre, ácidos ni otros productos de limpieza. No es para tomar. Mantenelo fuera del alcance de niños y mascotas y leé la etiqueta.',
  faq=[['¿Qué aromas hay?', 'Violeta, Lavanda, Pino, Floral, Limón, Frutos Rojos, Bebé, Manzana y Bouquet.'], ['¿Se puede diluir?', 'Sí. La proporción para cada uso viene en la etiqueta.'], ['¿Sirve para establos y lecherías?', 'Sí, se usa en viviendas, plantas empacadoras, lecherías, establos y áreas en general.']]),
 'creolina': dict(
  intro='La Creolina León Rojo es un desinfectante de ágil acción para corrales, establos, desagües y áreas exteriores. Es un producto tradicional de finca y de patio.',
  pasos=['Ponete guantes y trabajá con buena ventilación.', 'Diluila en agua según la etiqueta.', 'Aplicala en el área a desinfectar.', 'Lavá los utensilios con agua después de usarla.'],
  seguridad='Producto de uso externo para áreas y superficies. Usá guantes y lentes, no lo apliqués sobre la piel ni en utensilios de cocina, y no lo mezclés con otros productos. Mantenela fuera del alcance de niños y mascotas y leé la etiqueta.',
  faq=[['¿Dónde se usa?', 'En corrales, establos, desagües y áreas exteriores.'], ['¿En qué presentaciones viene?', 'En 240 ml, 1/2 litro, litro y galón.']]),
 'cloro': dict(
  intro='El Cloro León Rojo es hipoclorito de sodio para desinfectar superficies, pisos y blanquear la ropa. Viene en versión doméstica al 3% y 4% y en versión industrial al 12%.',
  pasos=['Ventilá el lugar y ponete guantes.', 'Diluilo en agua según lo que indica la etiqueta para cada uso.', 'Aplicalo en pisos y superficies, o agregalo al lavado de ropa blanca.', 'Enjuagá con agua cuando la etiqueta lo indique.'],
  seguridad='Nunca lo mezclés con ácidos, vinagre, amoníaco, desatoradores ni otros productos: se forman gases tóxicos. Usá guantes y ventilación, no lo uses en ropa de color y mantenelo fuera del alcance de niños. Leé siempre la etiqueta.',
  faq=[['¿Qué diferencia hay entre el 3%, 4% y 12%?', 'El 3% y el 4% son de uso doméstico. El 12% es industrial, de mayor concentración, y requiere más cuidado al manipularlo.'], ['¿Lo puedo mezclar con vinagre o desinfectante?', 'No. El cloro nunca se mezcla con otros productos de limpieza.']],
  blog='usos-del-vinagre-de-limpieza'),
 'azulejos': dict(
  intro='El Limpiador de Azulejos León Rojo limpia azulejos y enchapes de baño y cocina, y elimina bacterias y moho de las juntas.',
  pasos=['Ponete guantes y ventilá el baño o la cocina.', 'Aplicá el producto según la etiqueta.', 'Dejalo actuar el tiempo que indica la etiqueta.', 'Restregá las juntas con un cepillo.', 'Enjuagá con abundante agua.'],
  seguridad='No lo mezclés con cloro ni con otros productos. Usá guantes y buena ventilación y mantenelo fuera del alcance de niños. Leé la etiqueta antes de usar.',
  faq=[['¿Sirve para el moho de las juntas?', 'Sí, está hecho para eliminar bacterias y moho en azulejos y enchapes.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'cristales': dict(
  intro='El Limpiador de Cristales León Rojo deja vidrios, ventanas, espejos, vitrinas y parabrisas limpios y sin marcas.',
  pasos=['Rociá el producto sobre el vidrio.', 'Limpiá con un paño de microfibra o papel.', 'Terminá con un paño seco para que no queden marcas.'],
  seguridad=GEN,
  faq=[['¿Sirve para el parabrisas?', 'Sí, para vidrios de casa, espejos, vitrinas y parabrisas.'], ['¿Por qué viene en litro repuesto?', 'Para rellenar tu atomizador y ahorrar. También viene en litro atomizador y galón.']]),
 'ceramica': dict(
  intro='El Abrillantador de Cerámica León Rojo da un brillo superior a pisos y enchapes de cerámica. Se aplica sobre la superficie limpia y seca.',
  pasos=['Limpiá el piso y dejalo secar por completo.', 'Aplicá el producto con un trapeador limpio, en capa delgada.', 'Dejá secar sin pisar.'],
  seguridad=GEN,
  faq=[['¿Se aplica sobre el piso sucio?', 'No. Siempre sobre la cerámica limpia y seca para que el brillo quede parejo.'], ['¿En qué presentación viene?', 'En galón.']]),
 'cerapisos': dict(
  intro='La Cera Líquida para Pisos León Rojo es para encerar pisos de mosaico, terrazo, granito y madera. Viene en color blanco y rojo y se puede diluir.',
  pasos=['Barré y lavá el piso, y dejalo secar.', 'Diluila si hace falta, según la etiqueta.', 'Aplicá una capa delgada con un trapeador limpio.', 'Dejá secar y lujá si querés más brillo.'],
  seguridad=GEN,
  faq=[['¿Qué colores hay?', 'Blanca y roja.'], ['¿Para qué pisos sirve?', 'Mosaico, terrazo, granito y madera.']]),
 'jabonmanos': dict(
  intro='El Jabón Líquido para Manos León Rojo tiene glicerina y fragancia fresca, para el lavado frecuente de manos en baños, oficinas, restaurantes y la casa.',
  pasos=['Mojate las manos.', 'Aplicá el jabón.', 'Frotá todas las partes de las manos.', 'Enjuagá y secate bien.'],
  seguridad='Uso externo. Evitá el contacto con los ojos y mantenelo fuera del alcance de niños.',
  faq=[['¿Sirve para dispensadores?', 'Sí. El galón es ideal para rellenar dispensadores de oficinas, restaurantes y comercios.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'jabonvajillas': dict(
  intro='El Jabón Líquido para Vajillas León Rojo corta la grasa de platos, ollas y utensilios de cocina. Viene en galón, ideal para casas, sodas y restaurantes.',
  pasos=['Aplicá un poco de jabón en la esponja o diluido en agua.', 'Lavá platos, ollas y utensilios.', 'Enjuagá con abundante agua.'],
  seguridad='Evitá el contacto con los ojos. No es para tomar: mantenelo fuera del alcance de niños. No lo mezclés con cloro.',
  faq=[['¿En qué presentación viene?', 'En galón.'], ['¿Sirve para restaurantes?', 'Sí, se usa en cocinas, sodas y restaurantes.']]),
 'detergente': dict(
  intro='El Detergente Líquido para Ropa León Rojo sirve para lavadora o lavado a mano. Remueve manchas, grasa y sudor y protege los colores.',
  pasos=['Separá la ropa blanca de la de color.', 'Agregá la cantidad que indica la etiqueta según la carga.', 'Lavá normalmente.', 'Para un acabado suave, usá el Suavizante de Telas en el último enjuague.'],
  seguridad='Evitá el contacto con los ojos y mantenelo fuera del alcance de niños. No lo mezclés con cloro ni con otros productos.',
  faq=[['¿Sirve para lavar a mano?', 'Sí, para lavadora y lavado a mano.'], ['¿Cuánto le echo?', 'La cantidad depende de la carga: seguí lo que indica la etiqueta.']]),
 'suavizante': dict(
  intro='El Suavizante de Telas León Rojo se usa en el último enjuague y deja la ropa suave y con aroma agradable. Viene en azul, rosado y morado.',
  pasos=['Lavá la ropa con detergente.', 'En el último enjuague, agregá el suavizante según la etiqueta.', 'Tendé o secá la ropa como siempre.'],
  seguridad='Evitá el contacto con los ojos y mantenelo fuera del alcance de niños. No lo mezclés con cloro.',
  faq=[['¿Qué variedades hay?', 'Azul, rosado y morado.'], ['¿Sirve para lavanderías y hoteles?', 'Sí, viene en galón para uso en casa, lavanderías y hoteles.']]),
 'desatoradornc': dict(
  intro='El Desatorador de Cañerías NC León Rojo es soda cáustica líquida al 50%. Destapa cañerías, desagües de cocina y trampas de grasa, donde la grasa es la principal causa del taqueo.',
  pasos=['Retirá el agua estancada que puedas.', 'Ponete guantes y lentes y ventilá el lugar.', 'Aplicá la cantidad que indica la etiqueta, despacio y directo en el desagüe.', 'Dejalo actuar el tiempo que indica la etiqueta sin usar la pila.', 'Enjuagá con abundante agua.'],
  seguridad='Producto corrosivo. No lo mezclés con ácidos, cloro, otros desatoradores ni productos de limpieza. Usá guantes y lentes, no lo dejés al alcance de niños y leé siempre la etiqueta.',
  faq=[['¿Cuál es la diferencia con el Super Desatorador?', 'El NC es a base de soda cáustica; el Super Desatorador es a base de ácido sulfúrico. Son químicos distintos y nunca se deben mezclar ni usar uno detrás del otro.'], ['¿Sirve para trampas de grasa?', 'Sí, es muy usado en desagües de cocina y trampas de grasa.']],
  blog='como-destapar-una-caneria'),
 'potasa': dict(
  intro='La Super Potasa León Rojo viene en escamas para destapar y limpiar cañerías, inodoros, coladeras y desagües.',
  pasos=['Retirá el agua estancada que puedas.', 'Ponete guantes y lentes y ventilá el lugar.', 'Echá la cantidad que indica la etiqueta directo en el desagüe.', 'Seguí las indicaciones de la etiqueta para agregar agua y el tiempo de espera.', 'Enjuagá con abundante agua.'],
  seguridad='Producto corrosivo. No toqués las escamas con las manos, usá guantes y lentes y no la mezclés con ácidos, cloro ni otros desatoradores. Guardala cerrada, en lugar seco y fuera del alcance de niños.',
  faq=[['¿En qué presentación viene?', 'En 300 g.'], ['¿La puedo usar después de otro desatorador?', 'No. Nunca combinés desatoradores distintos: pueden reaccionar de forma peligrosa.']],
  blog='como-destapar-una-caneria'),
 'muriatico29': dict(
  intro='El Ácido Muriático 29% León Rojo es una solución de ácido clorhídrico que elimina sarro, restos de cemento y manchas en pisos, enchapes, ladrillo y piedra.',
  pasos=['Ponete guantes, lentes y ropa que cubra la piel. Trabajá con buena ventilación.', 'Probá primero en una zona pequeña y poco visible.', 'Si la etiqueta indica diluir, echá siempre el ácido sobre el agua, nunca el agua sobre el ácido.', 'Aplicá con cepillo y frotá.', 'Enjuagá muy bien con abundante agua.'],
  seguridad='Producto peligroso y corrosivo. Nunca lo mezclés con cloro ni con otros químicos: puede liberar gases tóxicos. No respirés los vapores y no lo usés en mármol, piedra caliza, metales ni superficies pintadas. Guardalo cerrado y fuera del alcance de niños.',
  faq=[['¿Cuál es la diferencia con el Super Ácido Muriático 36%?', 'El 36% es la versión de máxima concentración para manchas y sarro más difíciles. El 29% es para los trabajos de limpieza habituales.'], ['¿Sirve para quitar restos de cemento?', 'Sí, es uno de sus usos principales en pisos, ladrillo y piedra.']],
  blog='acido-muriatico-para-que-sirve'),
 'detergentepolvo': dict(
  intro='El Detergente en Polvo Industrial León Rojo es para lavar talleres mecánicos, aceras, patios, granjas y porquerizas. Viene desde 1 kg hasta sacos de 25 kg.',
  pasos=['Barré la suciedad suelta.', 'Disolvé el detergente en agua según la etiqueta.', 'Aplicalo y restregá con cepillo o escoba.', 'Enjuagá con abundante agua.'],
  seguridad='Usá guantes y evitá el contacto con ojos y piel. No lo mezclés con cloro ni con otros productos. Guardalo seco y fuera del alcance de niños.',
  faq=[['¿Es para lavar ropa?', 'No, es un detergente industrial para pisos de taller, aceras, patios y granjas. Para ropa está el Detergente Líquido para Ropa.'], ['¿En qué presentaciones viene?', '1 kg, 2 kg, 5 kg, 10 kg y 25 kg.']]),
 'thinner': dict(
  intro='El Thinner Industrial NC León Rojo es un diluyente para lacas nitrocelulosa y para limpiar pistolas y equipo de pintura. Lo usan talleres de pintura y carpinterías.',
  pasos=['Trabajá en un lugar ventilado y lejos de cualquier llama.', 'Diluí la laca en la proporción que indica el fabricante de la pintura.', 'Para limpiar la pistola, hacé pasar thinner limpio hasta que salga sin color.', 'Cerrá bien el envase después de usarlo.'],
  seguridad=SOLV,
  faq=[['¿Sirve para pintura de aceite?', 'El thinner NC es para lacas nitrocelulosa. Para pintura de aceite se usa Aguarrás o Espíritu Mineral.'], ['¿En qué presentaciones viene?', 'En 1/2 litro, litro y galón.']]),
 'aguarras': dict(
  intro='El Aguarrás León Rojo es un diluyente para pinturas y esmaltes base aceite y para limpiar brochas y rodillos.',
  pasos=['Trabajá en un lugar ventilado y lejos de cualquier llama.', 'Diluí la pintura en la proporción que indica el fabricante de la pintura.', 'Para limpiar brochas, sumergilas en aguarrás y escurrilas varias veces.', 'Cerrá bien el envase después de usarlo.'],
  seguridad=SOLV,
  faq=[['¿Sirve para lacas?', 'Para lacas nitrocelulosa se usa el Thinner Industrial NC. El aguarrás es para pintura y esmalte de aceite.'], ['¿En qué presentaciones viene?', 'En 1/2 litro, litro y galón.']]),
 'espiritu': dict(
  intro='El Espíritu Mineral León Rojo es un solvente para diluir pinturas y barnices y para limpiar herramientas de pintura.',
  pasos=['Trabajá en un lugar ventilado y lejos de cualquier llama.', 'Diluí la pintura o el barniz en la proporción que indica su fabricante.', 'Limpiá brochas y herramientas al terminar.', 'Cerrá bien el envase.'],
  seguridad=SOLV,
  faq=[['¿Cuál es la diferencia con el aguarrás?', 'Los dos son solventes para pinturas; el tipo correcto depende de lo que indique el fabricante de tu pintura o barniz.'], ['¿En qué presentaciones viene?', 'En 1/2 litro, litro y galón.']]),
 'removedor': dict(
  intro='El Removedor de Pintura León Rojo ablanda y levanta la pintura base aceite para retirarla con espátula de muebles, puertas, ventanas y metal.',
  pasos=['Trabajá en un lugar ventilado, con guantes y lentes.', 'Aplicá una capa gruesa con brocha sobre la pintura.', 'Esperá el tiempo que indica la etiqueta hasta que la pintura se arrugue.', 'Retirá con espátula.', 'Limpiá la superficie antes de volver a pintar.'],
  seguridad='Producto químico fuerte. Usá guantes, lentes y buena ventilación, no respirés los vapores, evitá el contacto con la piel y mantenelo lejos de llamas y fuera del alcance de niños. Leé siempre la etiqueta.',
  faq=[['¿Sirve para pintura de agua?', 'Está hecho para pintura base aceite.'], ['¿En qué presentaciones viene?', 'En 1/16, 1/8 y 1/4 de galón.']]),
 'canfin': dict(
  intro='El Canfín León Rojo es keroseno para encendido, lámparas y limpieza de piezas.',
  pasos=['Usalo en un lugar ventilado y lejos de llamas abiertas.', 'Para limpiar piezas, sumergilas o frotalas con una brocha.', 'Dejá secar bien las piezas antes de usarlas.', 'Cerrá bien el envase.'],
  seguridad=SOLV + ' Nunca lo guardés en botellas de bebidas.',
  faq=[['¿Canfín es lo mismo que keroseno?', 'Sí, canfín es como se le dice al keroseno en Costa Rica.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'arjibond': dict(
  intro='El Arji Bond León Rojo es un aditivo acrílico para repellos, morteros y concretos. Mejora la adherencia y la durabilidad, y se usa como puente de adherencia.',
  pasos=['Limpiá la superficie de polvo, grasa y partes sueltas.', 'Usalo según la proporción que indica la etiqueta para cada trabajo.', 'Aplicá la mezcla o el puente de adherencia.', 'Seguí los tiempos de la etiqueta antes de continuar.'],
  seguridad='Usá guantes y lentes al mezclar. Evitá el contacto con ojos y mantenelo fuera del alcance de niños. Leé la etiqueta.',
  faq=[['¿Para qué sirve el puente de adherencia?', 'Ayuda a que el repello o el concreto nuevo se pegue bien a la superficie existente.'], ['¿En qué presentaciones viene?', 'En 1/4 de galón y galón.']]),
 'acril800': dict(
  intro='El Super Acril-800 León Rojo es un aditivo acrílico para repellos, estucos y concretos. También sirve como sellador y para resanes.',
  pasos=['Limpiá la superficie de polvo y partes sueltas.', 'Usalo según la proporción que indica la etiqueta para cada trabajo.', 'Aplicá la mezcla o el sellador.', 'Respetá los tiempos de secado de la etiqueta.'],
  seguridad='Usá guantes y lentes al mezclar. Evitá el contacto con ojos y mantenelo fuera del alcance de niños. Leé la etiqueta.',
  faq=[['¿Sirve como sellador?', 'Sí, además de aditivo para repellos, estucos y concretos.'], ['¿En qué presentaciones viene?', 'En 1/4 de galón y galón.']]),
 'tapagoteras': dict(
  intro='El Tapagoteras en Pasta León Rojo sella goteras en techos, canoas y uniones de lámina. Es de fácil aplicación, rápido y efectivo.',
  pasos=['Trabajá en seco: limpiá y secá la zona de la gotera.', 'Retirá óxido y partes sueltas.', 'Aplicá la pasta con espátula o brocha, cubriendo bien la unión o el hueco.', 'Dejá secar según la etiqueta antes de que llueva.'],
  seguridad='Usá guantes. Tené cuidado al trabajar en techos: usá escalera firme y no subás solo ni con lluvia. Mantenelo fuera del alcance de niños.',
  faq=[['¿Se puede aplicar con lluvia?', 'No, la superficie debe estar limpia y seca.'], ['¿En qué presentaciones viene?', 'En 1/16 y 1/4 de galón.']]),
 'masilla': dict(
  intro='La Masilla Acrílica León Rojo rellena grietas y fisuras en paredes antes de pintar, y sirve para resanes.',
  pasos=['Limpiá la grieta de polvo y partes sueltas.', 'Rellená con espátula, presionando bien.', 'Dejá secar según la etiqueta.', 'Lijá suave y pintá.'],
  seguridad='Evitá el contacto con los ojos y mantenela fuera del alcance de niños. Leé la etiqueta.',
  faq=[['¿Se puede pintar encima?', 'Sí, se usa justamente para dejar la pared lista para pintar.'], ['¿En qué presentaciones viene?', 'En 1/16, 1/8 y 1/4 de galón.']]),
 'ocre': dict(
  intro='El Ocre León Rojo es un pigmento para dar color a pisos, pilas, paredes y posteos de concreto. Viene en rojo, azul, verde y negro.',
  pasos=['Medí el pigmento según la etiqueta y el tono que buscás.', 'Mezclalo bien con los materiales secos antes de agregar agua.', 'Prepará la mezcla de una sola vez para que el color quede parejo.', 'Aplicá y dejá curar como de costumbre.'],
  seguridad='Usá guantes y mascarilla al manipular el polvo y evitá el contacto con los ojos. Mantenelo fuera del alcance de niños.',
  faq=[['¿Qué colores hay?', 'Rojo, azul, verde y negro.'], ['¿En qué presentación viene?', 'En bolsa de 1 kilo.']]),
 'alquitran': dict(
  intro='El Alquitrán León Rojo protege postes, cercas, corrales y madera a la intemperie contra el sol, la lluvia y los insectos.',
  pasos=['La madera debe estar limpia y seca.', 'Aplicá con brocha, cubriendo bien la parte que va enterrada y la que queda expuesta.', 'Dejá secar antes de instalar.', 'Limpiá las herramientas con el solvente que indica la etiqueta.'],
  seguridad='Usá guantes, lentes y ropa de trabajo. Aplicalo al aire libre, lejos de llamas, y no respirés los vapores. Mantenelo fuera del alcance de niños y animales.',
  faq=[['¿Para qué se usa?', 'Para proteger postes de cerca, corrales y madera a la intemperie.'], ['¿En qué presentación viene?', 'En galón.']]),
 'cemento': dict(
  intro='El Cemento de Contacto León Rojo es un adhesivo de fácil aplicación y adhesión inmediata para madera, formica, cuero, hule y tapicería. Lo usan carpinteros, tapiceros y zapateros.',
  pasos=['Las superficies deben estar limpias, secas y sin polvo.', 'Aplicá una capa delgada en las dos superficies.', 'Esperá el tiempo que indica la etiqueta hasta que esté seco al tacto.', 'Uní las piezas con cuidado (se pegan al instante) y presioná firme.'],
  seguridad=SOLV,
  faq=[['¿Por qué se aplica en las dos superficies?', 'El cemento de contacto pega cuando las dos capas se tocan; por eso va en ambas caras.'], ['¿En qué presentaciones viene?', 'En 1/48, 1/32, 1/16, 1/8 y 1/4 de galón.']]),
 'cola': dict(
  intro='La Cola Blanca León Rojo es un pegamento blanco para uniones firmes en madera y aglomerado. Se usa en carpintería, muebles y manualidades.',
  pasos=['Las piezas deben estar limpias y secas.', 'Aplicá la cola en una de las caras.', 'Uní las piezas y presioná con prensas o peso.', 'Limpiá el exceso con un paño húmedo y dejá secar según la etiqueta.'],
  seguridad='Evitá el contacto con los ojos y mantenela fuera del alcance de niños.',
  faq=[['¿Sirve para aglomerado?', 'Sí, para madera y aglomerado.'], ['¿En qué presentaciones viene?', 'En 1/16, 1/8 y 1/4 de galón.']]),
 'ebonol': dict(
  intro='El Ebonol León Rojo es un tinte para maderas en color clásico antiguo, para muebles, puertas y acabados de madera.',
  pasos=['Lijá la madera y quitá el polvo.', 'Aplicá el tinte con brocha o paño, a favor de la veta.', 'Retirá el exceso para emparejar el tono.', 'Dejá secar según la etiqueta antes de sellar o barnizar.'],
  seguridad='Usá guantes y trabajá en un lugar ventilado. Mantenelo lejos de llamas y fuera del alcance de niños. Leé la etiqueta.',
  faq=[['¿Qué color da?', 'Color clásico antiguo.'], ['¿En qué presentaciones viene?', 'En 1/8, 1/4 de galón y galón.']]),
 'pentacellagua': dict(
  intro='El Pentacell León Rojo es un preservante para maderas soluble en agua. Protege contra polilla, comején y hongos en casas de madera, vigas y cercas.',
  pasos=['Usá guantes, lentes y ropa de trabajo.', 'Prepará el producto según la etiqueta.', 'Aplicalo con brocha o por inmersión sobre madera limpia.', 'Dejá secar antes de pintar o instalar.'],
  seguridad=PRES_MAD,
  faq=[['¿Contra qué protege?', 'Contra polilla, comején y hongos.'], ['¿Cuál es la diferencia con el Pentacell Concentrado?', 'Este es soluble en agua; el Concentrado es soluble en solvente y de uso industrial.']]),
 'pentacellsolvente': dict(
  intro='El Pentacell Concentrado León Rojo es un preservante para maderas soluble en solvente, de uso industrial, para aserraderos y construcción en madera.',
  pasos=['Usá equipo de protección completo.', 'Prepará el producto según la etiqueta.', 'Aplicalo sobre madera limpia con brocha o por inmersión.', 'Dejá secar en un lugar ventilado.'],
  seguridad=PRES_MAD + ' Producto inflamable: mantenelo lejos de llamas.',
  faq=[['¿Es para uso casero?', 'Es de uso industrial. Para uso en casa está el Pentacell soluble en agua.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'kontrolwood': dict(
  intro='El Kontrol Wood León Rojo es un preservante concentrado para maderas de uso industrial, para aserraderos y madera estructural.',
  pasos=['Usá equipo de protección completo.', 'Prepará el producto según la etiqueta.', 'Aplicalo sobre madera limpia.', 'Dejá secar en un lugar ventilado.'],
  seguridad=PRES_MAD,
  faq=[['¿Es para uso casero?', 'Es de uso industrial, para aserraderos y madera estructural.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'arjibor': dict(
  intro='El Arjibor León Rojo es un preservante que protege la madera contra insectos y hongos. Es ideal para decks, terrazas y muebles de exterior.',
  pasos=['Usá guantes y lentes.', 'Prepará el producto según la etiqueta.', 'Aplicalo con brocha sobre madera limpia y seca.', 'Dejá secar antes de pintar o barnizar.'],
  seguridad=PRES_MAD,
  faq=[['¿Dónde se usa?', 'En decks, terrazas y muebles de exterior.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'arjicromo': dict(
  intro='El Arjicromo León Rojo es un preservante para madera de exteriores y construcción, como fachadas de madera.',
  pasos=['Usá guantes, lentes y ropa de trabajo.', 'Prepará el producto según la etiqueta.', 'Aplicalo con brocha o por inmersión sobre madera limpia.', 'Dejá secar antes de instalar.'],
  seguridad=PRES_MAD,
  faq=[['¿Dónde se usa?', 'En madera de exteriores, fachadas y construcción.'], ['¿En qué presentaciones viene?', 'En litro y galón.']]),
 'clorogranulado': dict(
  intro='El Cloro Granulado León Rojo mantiene el agua de la piscina limpia y libre de bacterias y algas. Se usa en piscinas de casa, hoteles, condominios y jacuzzis.',
  pasos=['Medí el pH y el cloro del agua antes de aplicar.', 'Calculá la cantidad según el volumen de la piscina y lo que indica la etiqueta.', 'Disolvelo primero en un balde con agua (siempre el producto sobre el agua).', 'Repartilo por la piscina con el filtro encendido.', 'Esperá el tiempo que indica la etiqueta antes de bañarse.'],
  seguridad=PISC,
  faq=[['¿Qué diferencia hay con el cloro en pastilla?', 'El granulado se disuelve rápido; la pastilla se disuelve poco a poco y sirve para el mantenimiento continuo.'], ['¿En qué presentaciones viene?', 'En frasco de 1 kg y bolsa de 1 kg.']],
  blog='como-mantener-la-piscina-limpia'),
 'cloropastilla': dict(
  intro='El Cloro en Pastilla León Rojo es ácido tricloroisocianúrico al 90% para la cloración y el mantenimiento de piscinas. Se disuelve poco a poco y mantiene el cloro estable.',
  pasos=['Medí el pH y el cloro del agua.', 'Colocá las pastillas en el clorador, flotador o skimmer, nunca sueltas en el fondo.', 'Usá la cantidad que indica la etiqueta según el volumen de la piscina.', 'Revisá el nivel de cloro con regularidad.'],
  seguridad=PISC,
  faq=[['¿Las puedo tirar directo a la piscina?', 'No es lo recomendable: van en clorador, flotador o skimmer para que se disuelvan de forma pareja.'], ['¿En qué presentaciones viene?', 'Pastilla de 200 g y frasco de 1 kg.']],
  blog='como-mantener-la-piscina-limpia'),
 'alguiacid': dict(
  intro='El Algui-Acid León Rojo es un alguicida que previene y elimina las algas en el agua de la piscina, para el tratamiento inicial y el mantenimiento semanal.',
  pasos=['Cepillá paredes y fondo.', 'Aplicá la cantidad que indica la etiqueta según el volumen de la piscina.', 'Repartilo con el filtro encendido.', 'Esperá el tiempo que indica la etiqueta antes de bañarse.'],
  seguridad=PISC,
  faq=[['¿Reemplaza al cloro?', 'No. El alguicida complementa al cloro: ayuda a prevenir y eliminar algas.'], ['¿En qué presentación viene?', 'En galón.']],
  blog='como-mantener-la-piscina-limpia'),
 'sodaash': dict(
  intro='El Soda Ash León Rojo es carbonato de sodio para ajustar el pH y la alcalinidad del agua. Es de uso técnico, en piscinas y tratamiento de agua.',
  pasos=['Medí el pH del agua antes de aplicar.', 'Calculá la cantidad según la etiqueta y el volumen de agua.', 'Disolvelo en un balde con agua (siempre el producto sobre el agua).', 'Repartilo con el filtro encendido y volvé a medir después.'],
  seguridad=PISC,
  faq=[['¿Para qué sirve en la piscina?', 'Para subir el pH y la alcalinidad cuando están bajos.'], ['¿En qué presentación viene?', 'En bolsa de 1 kilo.']]),
 'sulfatoaluminio': dict(
  intro='El Sulfato de Aluminio León Rojo es un clarificante para tratamiento de agua, de uso técnico e industrial.',
  pasos=['Usá guantes, lentes y mascarilla.', 'Calculá la cantidad según la etiqueta y el volumen de agua.', 'Disolvelo en agua antes de aplicarlo.', 'Seguí las indicaciones de la etiqueta para la filtración o el asentamiento.'],
  seguridad=PISC,
  faq=[['¿Para qué sirve?', 'Para clarificar agua turbia en procesos de tratamiento de agua.'], ['¿En qué presentación viene?', 'En bolsa de 1 kilo.']]),
 'sulfatocobre': dict(
  intro='El Sulfato de Cobre León Rojo se usa para el control de algas en estanques y reservorios. Es de uso técnico.',
  pasos=['Usá guantes, lentes y mascarilla.', 'Calculá la cantidad según la etiqueta y el volumen de agua.', 'Disolvelo en agua antes de aplicarlo.', 'Seguí las indicaciones de la etiqueta.'],
  seguridad='Producto tóxico si se ingiere y dañino para peces y vida acuática si se usa en exceso. Usá guantes, lentes y mascarilla, seguí al pie de la letra la etiqueta y guardalo cerrado, fuera del alcance de niños y animales.',
  faq=[['¿Dónde se usa?', 'En estanques y reservorios, para controlar algas.'], ['¿En qué presentación viene?', 'En bolsa de 1 kilo.']]),
 'envases': dict(
  intro='Vendemos galones y botellas plásticas vacías con tapa, en color blanco y natural. Son ideales para envasar y vender por cuenta propia, o para bodegas.',
  pasos=['Escogé la presentación: botella litro o galón.', 'Escogé el color: blanco o natural.', 'Escribinos al WhatsApp con la cantidad que necesitás.'],
  seguridad='',
  faq=[['¿Qué colores hay?', 'Blanco y natural.'], ['¿Venden por cantidad?', 'Sí. Escribinos al WhatsApp 8994-4763 con la cantidad que necesitás.']]),
 'atomizadores': dict(
  intro='Vendemos botellas atomizadoras vacías de litro, con gatillo azul industrial o gatillo transparente, para envasar productos de limpieza, lavacar o reenvasado.',
  pasos=['Escogé el tipo de gatillo: azul industrial o transparente.', 'Escribinos al WhatsApp con la cantidad que necesitás.', 'Rotulá cada botella con el producto que contiene.'],
  seguridad='',
  faq=[['¿Qué gatillos hay?', 'Gatillo azul industrial y gatillo transparente.'], ['¿Por qué rotular las botellas?', 'Para no confundir productos: nunca reutilicés una botella de un químico para otro distinto.']]),
}

if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'fichas'), exist_ok=True)
    n = 0
    for k, v in F.items():
        p = os.path.join(ROOT, 'fichas', k + '.json')
        if os.path.exists(p): continue
        json.dump(v, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); n += 1
    print('fichas nuevas:', n)
