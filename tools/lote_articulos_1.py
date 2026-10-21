"""Lote de 12 artículos (21-10-2026). Escribe posts/<slug>.html y agrega las entradas a posts.json."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FECHA = '2026-10-21'
SEG_GEN = '<div class="warn"><b>⚠ Seguridad:</b> {}</div>'

A = []

A.append(dict(slug='como-quitar-el-sarro-del-bano', img='b5_18', kw='quitar sarro baño, sarro en azulejos, moho en juntas, limpiar baño Costa Rica',
 title='Cómo quitar el sarro y el moho del baño',
 desc='Paso a paso para quitar el sarro, las manchas y el moho de azulejos, juntas y enchapes del baño, con los productos correctos y sin dañar las superficies.',
 cta=['b5_18', 'Limpiador de Azulejos León Rojo', 'Elimina bacterias y moho de azulejos y enchapes. En litro y galón.'],
 html='''<p class="lead">Las manchas blancas en la ducha, las juntas negras entre los azulejos y ese tono opaco que no se quita con jabón tienen nombre: sarro y moho. En Costa Rica, con tanta humedad y agua dura en muchas zonas, son el problema número uno de cualquier baño. La buena noticia es que se quitan, y sin rayar ni dañar el enchape.</p>
<h2>Sarro y moho no son lo mismo</h2>
<p>Antes de escoger producto conviene saber qué estamos limpiando:</p>
<ul><li><b>Sarro:</b> son los minerales del agua que se van pegando con el tiempo. Se ve como manchas blancas o amarillentas en la grifería, la mampara y las paredes de la ducha.</li><li><b>Moho:</b> es un hongo que aparece donde hay humedad y poca ventilación. Se ve como puntos o manchas negras o verdosas, sobre todo en las juntas y en las esquinas.</li><li><b>Grasa y jabón:</b> la capa gris que deja el jabón con el uso diario.</li></ul>
<h2>Lo que vas a necesitar</h2>
<ul><li>Limpiador de Azulejos León Rojo.</li><li>Un cepillo de cerdas firmes o un cepillo de dientes viejo para las juntas.</li><li>Guantes de hule y un trapo o esponja.</li><li>Buena ventilación: ventana abierta o extractor encendido.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Ventilá el baño.</b> Abrí la ventana y la puerta antes de empezar.</li><li><b>Quitá lo suelto.</b> Retirá champús, jabones y alfombras, y pasá agua para quitar el polvo y los pelos.</li><li><b>Aplicá el Limpiador de Azulejos</b> sobre las zonas con sarro o moho, siguiendo la cantidad y la forma de uso que indica la etiqueta.</li><li><b>Dejalo actuar</b> el tiempo que indica la etiqueta, sin dejar que se seque.</li><li><b>Restregá</b> con el cepillo, sobre todo en las juntas y alrededor de la grifería.</li><li><b>Enjuagá con abundante agua</b> y secá con un trapo para que no queden marcas.</li></ol>
''' + SEG_GEN.format('No mezclés el limpiador de azulejos con cloro, vinagre ni otros productos de limpieza: algunas combinaciones liberan gases peligrosos. Usá guantes, mantené el baño ventilado y guardá el producto fuera del alcance de los niños. Leé siempre la etiqueta.') + '''
<h2>¿Y para la limpieza de todos los días?</h2>
<p>Una vez que el baño quedó limpio, mantenerlo es mucho más fácil. Para el día a día, el <b>Vinagre de Limpieza 3.5% León Rojo</b> limpia, desengrasa y quita malos olores en lavatorios, grifería y espejos. Para los vidrios y la mampara, el <b>Limpiador de Cristales</b> los deja sin marcas.</p>
<h2>Cómo evitar que el moho vuelva</h2>
<ul><li>Después de bañarte, dejá la ventana abierta o el extractor encendido un rato.</li><li>Secá la mampara y las paredes de la ducha con un jalador de hule.</li><li>Lavá las cortinas de baño y las alfombras con frecuencia.</li><li>Limpiá las juntas una vez por semana antes de que el moho se pegue.</li></ul>
<h2>¿Y si el sarro es muy viejo?</h2>
<p>En baños que llevan años sin una limpieza profunda, puede que haga falta repetir el proceso. Si se trata de restos de cemento o mortero después de una remodelación, ese es otro trabajo: lo explicamos en nuestra guía de <a href="/productos/acido-muriatico/">ácido muriático</a>. Nunca uses ácido sobre mármol, piedra caliza ni griferías sin probar primero en una zona pequeña.</p>
<p>¿Tenés dudas sobre qué producto usar? Escribinos al WhatsApp 8994-4763 o pedí la marca León Rojo en tu ferretería de confianza.</p>'''))

A.append(dict(slug='piscina-verde-que-hacer', img='b5_15', kw='piscina verde, agua verde piscina, algas piscina, alguicida Costa Rica',
 title='Piscina verde: qué hacer para recuperar el agua',
 desc='Por qué se pone verde el agua de la piscina y los pasos para recuperarla: limpieza, alguicida, cloro y control del pH, con productos León Rojo.',
 cta=['b5_15', 'Algui-Acid León Rojo', 'Previene y elimina las algas de la piscina. En galón.'],
 html='''<p class="lead">Unos días de lluvia, poco cloro o el filtro apagado, y de repente el agua de la piscina amanece verde. Es uno de los problemas más comunes en Costa Rica, sobre todo en temporada de lluvias o después de vacaciones. Tiene arreglo, pero hay que hacerlo en orden.</p>
<h2>¿Por qué se pone verde el agua?</h2>
<p>El color verde son algas. Crecen muy rápido cuando se juntan tres cosas: poco cloro en el agua, calor y sol, y agua que no circula bien por el filtro. La lluvia también diluye el cloro y arrastra tierra y hojas que alimentan las algas.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li><b>Algui-Acid León Rojo</b>, el alguicida.</li><li><b>Cloro Granulado León Rojo</b> para la cloración.</li><li><b>Soda Ash</b>, si el pH está bajo.</li><li>Cepillo de piscina, red recogehojas y un medidor de pH y cloro.</li></ul>
<h2>Paso a paso para recuperar la piscina</h2>
<ol><li><b>Sacá la basura.</b> Retirá hojas, ramas e insectos con la red. Mientras más materia orgánica quede, más cloro se gasta.</li><li><b>Cepillá paredes y fondo.</b> Las algas se pegan a las superficies; cepillar las suelta para que los químicos las alcancen.</li><li><b>Medí el pH.</b> Si está bajo, ajustalo con Soda Ash según la etiqueta. El cloro trabaja mejor con el pH en su punto.</li><li><b>Aplicá el Algui-Acid</b> en la cantidad que indica la etiqueta según el volumen de tu piscina, con el filtro encendido.</li><li><b>Clorá con Cloro Granulado</b>, disolviéndolo primero en un balde con agua y repartiéndolo por la piscina, siguiendo la etiqueta.</li><li><b>Dejá el filtro trabajando</b> y limpiá o retrolavá el filtro según su manual.</li><li><b>Volvé a medir</b> y repetí lo necesario hasta que el agua esté clara. No te bañés hasta que pase el tiempo que indica la etiqueta.</li></ol>
''' + SEG_GEN.format('Usá guantes y lentes. Nunca mezclés químicos de piscina entre sí ni con ácidos: agregá cada uno por separado al agua, nunca agua sobre el producto. Guardalos cerrados, en un lugar fresco y seco, lejos de los niños. Seguí siempre las cantidades de la etiqueta.') + '''
<h2>Cómo evitar que vuelva a pasar</h2>
<ul><li>Mantené el cloro estable con <b>Cloro en Pastilla</b> en el clorador, flotador o skimmer.</li><li>Aplicá Algui-Acid de mantenimiento cada semana, según la etiqueta.</li><li>Medí pH y cloro con regularidad, sobre todo después de lluvias fuertes o de mucho uso.</li><li>Dejá que el filtro trabaje todos los días el tiempo que recomienda su fabricante.</li></ul>
<p>Si querés la rutina completa de mantenimiento, leé nuestra guía <a href="/blog/como-mantener-la-piscina-limpia/">Cómo mantener la piscina limpia</a> o revisá todos los <a href="/productos/quimicos-para-piscinas/">químicos para piscinas León Rojo</a>.</p>'''))

A.append(dict(slug='como-quitar-el-oxido-de-herramientas', img='b6_13', kw='quitar óxido, óxido herramientas, desoxidante, preparar metal para pintar',
 title='Cómo quitar el óxido de herramientas y metal',
 desc='Cómo quitar el óxido de herramientas, piezas y portones antes de pintar, y cómo evitar que vuelva a aparecer. Paso a paso con Desoxidante de Metales León Rojo.',
 cta=['b6_13', 'Desoxidante de Metales León Rojo', 'Quita el óxido de herramientas y piezas. En 1/2 litro, litro y galón.'],
 html='''<p class="lead">Con la humedad de Costa Rica, el óxido aparece en todo: herramientas guardadas, portones, verjas, piezas del carro y maquinaria. Si se deja, el metal se debilita y la pintura nueva se cae al poco tiempo. Quitarlo bien es el paso que hace la diferencia.</p>
<h2>¿Por qué hay que quitar el óxido antes de pintar?</h2>
<p>Pintar sobre óxido es tapar el problema: el óxido sigue avanzando debajo de la pintura, la levanta y en pocos meses aparecen burbujas y descascarado. Por eso cualquier pintor o taller empieza siempre dejando el metal limpio.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li>Desoxidante de Metales León Rojo.</li><li>Cepillo de alambre o lija.</li><li>Guantes, lentes de protección y trapos limpios.</li><li>Un lugar ventilado para trabajar.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Protegete.</b> Ponete guantes y lentes y trabajá con buena ventilación.</li><li><b>Quitá el óxido suelto</b> con el cepillo de alambre o la lija. No hace falta llegar al metal brillante, solo retirar las costras.</li><li><b>Aplicá el Desoxidante</b> sobre la superficie siguiendo la forma de uso y la cantidad que indica la etiqueta.</li><li><b>Dejalo actuar</b> el tiempo que indica la etiqueta.</li><li><b>Limpiá y secá muy bien</b> la pieza. El metal debe quedar seco antes del siguiente paso.</li><li><b>Pintá o protegé</b> el metal lo antes posible, para que no se vuelva a oxidar.</li></ol>
''' + SEG_GEN.format('El Desoxidante de Metales es un producto químico. Usá guantes, lentes y buena ventilación, evitá el contacto con la piel y los ojos, no lo mezclés con cloro ni con otros productos y mantenelo fuera del alcance de los niños. Leé siempre la etiqueta.') + '''
<h2>Herramientas: cómo guardarlas para que no se oxiden</h2>
<ul><li>Secalas bien después de usarlas, sobre todo si se mojaron.</li><li>Guardalas en un lugar seco, no en el piso ni contra paredes húmedas.</li><li>Lubricá las partes móviles con <b>Grasa Multiusos León Rojo</b>: bisagras, mecanismos y roscas.</li></ul>
<h2>Portones y verjas</h2>
<p>En portones grandes, trabajá por secciones: cepillá, aplicá el desoxidante, limpiá y pintá una parte antes de pasar a la siguiente. Así no dejás metal desnudo expuesto a la lluvia de la tarde.</p>
<p>¿Tenés un trabajo grande o para un taller? Escribinos al WhatsApp 8994-4763 y te ayudamos a escoger la presentación que te conviene. Ver la <a href="/productos/desoxidante-de-metales/">ficha completa del Desoxidante</a>.</p>'''))

A.append(dict(slug='como-eliminar-el-comejen-de-la-madera', img='b5_08', kw='comején, eliminar comején, polilla madera, preservante madera Costa Rica',
 title='Cómo proteger la madera del comején y la polilla',
 desc='Cómo detectar el comején y la polilla en la madera y cómo protegerla con un preservante. Guía para casas de madera, vigas, muebles y cercas.',
 cta=['b5_08', 'Pentacell León Rojo', 'Preservante soluble en agua contra polilla, comején y hongos. En litro y galón.'],
 html='''<p class="lead">El comején y la polilla son de los enemigos más caros de cualquier casa en Costa Rica. Trabajan por dentro, sin hacer ruido, y cuando se notan ya se comieron parte de una viga, un marco o un mueble. La mejor defensa es proteger la madera antes de que lleguen.</p>
<h2>Señales de que hay comején o polilla</h2>
<ul><li>Montoncitos de polvo fino o "aserrín" cerca de muebles, marcos o vigas.</li><li>Agujeros pequeños en la superficie de la madera.</li><li>Madera que suena hueca al golpearla.</li><li>Caminitos de tierra en paredes o columnas.</li><li>Alitas sueltas cerca de ventanas, sobre todo al inicio de las lluvias.</li></ul>
<p>Si el daño es grande o estructural, como vigas de techo comidas, lo correcto es consultar con un profesional: puede que haya que cambiar piezas.</p>
<h2>Prevenir es mucho más barato que reparar</h2>
<p>La madera tratada con un preservante resiste mucho mejor el ataque de insectos y hongos. Lo ideal es tratarla <b>antes de instalarla</b>, pero también se puede aplicar a madera ya colocada, siempre que esté limpia, seca y sin pintura ni barniz que impida que el producto penetre.</p>
<h2>¿Qué preservante usar?</h2>
<ul><li><b>Pentacell</b> (soluble en agua): para casas de madera, vigas y cercas.</li><li><b>Arjibor:</b> para decks, terrazas y muebles de exterior.</li><li><b>Arjicromo:</b> para fachadas de madera y construcción.</li><li><b>Pentacell Concentrado y Kontrol Wood:</b> de uso industrial, para aserraderos y madera estructural.</li></ul>
<h2>Paso a paso para aplicarlo</h2>
<ol><li><b>Protegete:</b> guantes, lentes y ropa que cubra la piel. Trabajá en un lugar ventilado.</li><li><b>Prepará la madera:</b> limpia, seca y sin polvo.</li><li><b>Prepará el producto</b> siguiendo exactamente lo que indica la etiqueta.</li><li><b>Aplicalo</b> con brocha o por inmersión, cubriendo bien todas las caras y los cortes, que es por donde más entra el insecto.</li><li><b>Dejá secar</b> antes de pintar, barnizar o instalar, según la etiqueta.</li></ol>
''' + SEG_GEN.format('Los preservantes de madera son productos químicos. Usá guantes, lentes y ropa de protección, no respirés los vapores y no los apliqués en utensilios de cocina, comederos ni bebederos. Mantenelos cerrados y fuera del alcance de niños y mascotas. Leé siempre la etiqueta.') + '''
<h2>Consejos para que dure más</h2>
<ul><li>Evitá que la madera esté en contacto directo con la tierra o con humedad constante.</li><li>Revisá cada año las zonas más expuestas: bases de columnas, marcos de puertas y aleros.</li><li>Para postes y cercas a la intemperie también existe el <b>Alquitrán León Rojo</b>.</li></ul>
<p>Mirá todos los <a href="/productos/preservantes-para-madera/">preservantes para madera León Rojo</a> o escribinos al WhatsApp 8994-4763.</p>'''))

A.append(dict(slug='como-limpiar-aros-de-aluminio', img='b2_10', kw='limpiar aros de aluminio, brillo aluminio, cajones de camión, limpiador de aluminio',
 title='Cómo limpiar aros y piezas de aluminio',
 desc='Cómo devolverle el brillo a los aros, cajones de camión, tanques y perfiles de aluminio con ALUX-500 León Rojo, paso a paso y con seguridad.',
 cta=['b2_10', 'ALUX-500 León Rojo', 'Limpiador de aluminio. En litro repuesto, litro atomizador y galón.'],
 html='''<p class="lead">El aluminio se pone opaco, manchado y gris con el polvo de la carretera, la grasa y la lluvia. En aros de carro, cajones de camión, tanques y perfiles, ese aspecto descuidado le quita valor al vehículo. Con el producto correcto el brillo vuelve.</p>
<h2>¿Por qué se opaca el aluminio?</h2>
<p>El aluminio forma una capa de óxido en la superficie que lo vuelve gris. A eso se le suma el polvo de frenos en los aros, la grasa y la suciedad del camino. El jabón normal quita la tierra, pero no esa capa opaca.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li>ALUX-500 León Rojo.</li><li>Cepillo de cerdas suaves o medianas.</li><li>Guantes y lentes de protección.</li><li>Manguera o balde con agua abundante.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Trabajá en frío y a la sombra.</b> Nunca apliqués el producto sobre aros o piezas calientes ni al sol directo.</li><li><b>Protegete</b> con guantes y lentes.</li><li><b>Mojá la superficie</b> y quitá la tierra suelta.</li><li><b>Aplicá el ALUX-500</b> siguiendo la etiqueta: ahí indica si se usa directo o diluido según el trabajo.</li><li><b>Dejalo actuar</b> el tiempo que indica la etiqueta, sin dejar que se seque sobre la pieza.</li><li><b>Restregá</b> con el cepillo, con especial atención a las esquinas y rendijas.</li><li><b>Enjuagá con abundante agua</b>, que no queden restos de producto.</li></ol>
''' + SEG_GEN.format('Usá guantes y lentes y trabajá en un lugar ventilado. No apliqués el ALUX-500 sobre pintura, vidrio ni superficies calientes, y no lo mezclés con otros productos. Mantenelo fuera del alcance de los niños y leé siempre la etiqueta.') + '''
<h2>Para que el trabajo quede completo</h2>
<ul><li>Lavá el resto del carro con <b>Shampoo para Autos León Rojo</b>, que limpia sin opacar la pintura.</li><li>Terminá las llantas con <b>Llantilux-80</b> o <b>Llantilux-1000</b> para el negro brillante.</li><li>Los plásticos y molduras negras quedan como nuevos con el <b>Restaurador de Partes Negras</b>.</li></ul>
<h2>¿Tenés un lavacar o una flotilla?</h2>
<p>El ALUX-500 viene en galón para quienes lo usan todos los días. Mirá toda la línea de <a href="/productos/productos-para-autos/">productos para autos y lavacar León Rojo</a> o pedilo al WhatsApp 8994-4763.</p>'''))

A.append(dict(slug='como-quitar-manchas-de-aceite-del-piso', img='b1_14', kw='manchas de aceite piso, grasa en el garaje, limpiar piso de taller, desengrasante',
 title='Cómo quitar manchas de aceite y grasa del piso',
 desc='Cómo quitar manchas de aceite y grasa del piso del garaje, la cochera o el taller con Desengrasante Industrial y Detergente en Polvo León Rojo.',
 cta=['b1_14', 'Desengrasante Industrial León Rojo', 'Remueve grasa, aceite y carbonilla. En litro repuesto, litro atomizador y galón.'],
 html='''<p class="lead">Una gota de aceite del carro, un cambio de aceite hecho en la cochera o años de trabajo en un taller dejan manchas oscuras en el concreto que el agua y el jabón no quitan. Con el producto adecuado se pueden sacar, o al menos aclarar mucho.</p>
<h2>Entre más fresca, más fácil</h2>
<p>El concreto es poroso: el aceite se va metiendo poco a poco. Por eso una mancha de ayer sale mucho más fácil que una de hace un año. Si se acaba de regar aceite, lo primero es absorberlo con arena, aserrín o tierra seca, dejarlo un rato y barrerlo.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li>Desengrasante Industrial León Rojo para las manchas.</li><li>Detergente en Polvo Industrial León Rojo para lavar áreas grandes.</li><li>Cepillo de cerdas duras o escoba de cerda dura.</li><li>Guantes, lentes y manguera.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Barré el área</b> y quitá la tierra suelta.</li><li><b>Prepará el desengrasante</b> según lo que indica la etiqueta para manchas de aceite en pisos.</li><li><b>Aplicalo sobre la mancha</b> y dejalo actuar unos minutos, sin que se seque.</li><li><b>Restregá con fuerza</b> con el cepillo.</li><li><b>Enjuagá con abundante agua.</b> En manchas viejas, repetí el proceso.</li><li>Para áreas grandes como talleres, aceras o patios, lavá todo el piso con el <b>Detergente en Polvo Industrial</b> disuelto en agua según la etiqueta.</li></ol>
''' + SEG_GEN.format('Usá guantes y lentes y trabajá con ventilación. No mezclés el desengrasante con cloro ni con otros productos. Evitá que el agua con grasa vaya directo a ríos o quebradas y mantené los productos fuera del alcance de los niños. Leé siempre la etiqueta.') + '''
<h2>Consejos para el taller</h2>
<ul><li>Poné bandejas o cartón debajo de los carros cuando trabajés.</li><li>Limpiá los derrames el mismo día: es mucho menos trabajo.</li><li>Para las manos, la <b>Crema Quita Grasa León Rojo</b> quita la grasa y el aceite sin solventes.</li></ul>
<p>Si además querés limpiar el motor, te lo explicamos en <a href="/blog/como-limpiar-el-motor-del-carro/">Cómo limpiar el motor del carro</a>. Toda la línea para talleres está en <a href="/productos/desengrasante/">desengrasante industrial</a>.</p>'''))

A.append(dict(slug='como-reparar-goteras-del-techo', img='b8_09', kw='goteras techo, tapar goteras, canoas, techo de lámina, tapagoteras Costa Rica',
 title='Cómo tapar goteras en el techo y las canoas',
 desc='Cómo encontrar y tapar goteras en techos de lámina, canoas y uniones antes de la lluvia, con Tapagoteras en Pasta León Rojo. Paso a paso y con seguridad.',
 cta=['b8_09', 'Tapagoteras en Pasta León Rojo', 'Fácil aplicación, rápida y efectiva. En 1/16, 1/8 y 1/4 de galón.'],
 html='''<p class="lead">En Costa Rica, la temporada de lluvias es cuando aparecen las goteras: una mancha en el cielorraso, un balde en medio de la sala o agua bajando por la pared. La mayoría vienen de clavos flojos, uniones de lámina o canoas con agujeros, y se pueden tapar sin cambiar el techo.</p>
<h2>Primero: encontrá de dónde viene</h2>
<p>El agua casi nunca cae justo debajo del hueco: corre por la lámina o por la estructura y gotea más allá. Para encontrar el punto:</p>
<ul><li>Revisá desde adentro, con lámpara, dónde se ve húmeda la madera o el cielorraso.</li><li>Desde arriba, buscá clavos o tornillos sin empaque, láminas montadas mal, óxido con agujeros y uniones abiertas.</li><li>En las canoas, revisá uniones, esquinas y bajantes.</li></ul>
''' + SEG_GEN.format('Trabajar en techos es peligroso. Hacelo solo con el techo seco, nunca con lluvia ni con viento fuerte. Usá una escalera firme, zapatos que no resbalen y, si podés, que alguien te acompañe. Pisá siempre sobre las clavadoras, no en medio de la lámina.') + '''
<h2>Lo que vas a necesitar</h2>
<ul><li>Tapagoteras en Pasta León Rojo.</li><li>Espátula o brocha.</li><li>Cepillo de alambre y un trapo.</li><li>Guantes.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Esperá un día seco.</b> La superficie tiene que estar completamente seca.</li><li><b>Limpiá la zona:</b> quitá el óxido suelto, el polvo, las hojas y la pintura que se esté despegando.</li><li><b>Aplicá el Tapagoteras</b> con espátula o brocha, cubriendo bien el hueco, el clavo o la unión y un poco alrededor.</li><li><b>Dejá secar</b> el tiempo que indica la etiqueta antes de que llueva.</li><li><b>Revisá en el siguiente aguacero</b> desde adentro que ya no entre agua.</li></ol>
<h2>¿Qué presentación comprar?</h2>
<p>Para un par de clavos o una unión, el <b>1/16 de galón</b> alcanza. Para varias goteras o canoas, el <b>1/8</b> o el <b>1/4 de galón</b> rinden más.</p>
<h2>Prevenir antes del invierno</h2>
<ul><li>Limpiá las canoas de hojas y basura antes de que empiecen las lluvias.</li><li>Revisá una vez al año los clavos y las uniones del techo.</li><li>Las grietas en paredes se rellenan con <b>Masilla Acrílica León Rojo</b> antes de pintar.</li></ul>
<p>Mirá todos los productos para <a href="/productos/aditivos-para-construccion/">construcción y reparaciones León Rojo</a> o pedilo en tu ferretería de confianza.</p>'''))

A.append(dict(slug='que-no-mezclar-con-cloro', img='b4_11', kw='mezclar cloro, cloro y vinagre, gases tóxicos limpieza, seguridad productos de limpieza',
 title='Qué NUNCA mezclar con cloro: guía de seguridad',
 desc='Las mezclas de productos de limpieza que nunca se deben hacer, por qué son peligrosas y qué hacer si alguien respira los gases. Guía de seguridad León Rojo.',
 cta=['b4_11', 'Cloro León Rojo', 'Doméstico 3% y 4%, industrial 12%. En galón.'],
 html='''<p class="lead">Muchos accidentes en la casa pasan por buena intención: "le echo un poco de esto y otro poco de aquello para que limpie más". Algunas mezclas de productos de limpieza liberan gases que irritan los ojos y los pulmones y pueden ser muy peligrosos en un baño cerrado. Esta guía es para que no te pase.</p>
<h2>La regla de oro</h2>
<p><b>Nunca mezclés productos de limpieza entre sí.</b> Cada producto está hecho para trabajar solo. Mezclarlos no limpia más: en el mejor caso se anulan, y en el peor liberan gases tóxicos.</p>
<h2>Mezclas que nunca se deben hacer</h2>
<ul><li><b>Cloro + vinagre</b> (o cualquier ácido): libera gas cloro, muy irritante.</li><li><b>Cloro + ácido muriático:</b> igual, libera gas cloro.</li><li><b>Cloro + amoníaco</b> o productos que lo contengan: forma gases tóxicos.</li><li><b>Cloro + desatoradores:</b> pueden reaccionar violentamente.</li><li><b>Dos desatoradores distintos</b>, por ejemplo uno ácido y uno de soda cáustica: la reacción genera calor y salpicaduras.</li><li><b>Cloro + alcohol:</b> también forma compuestos peligrosos.</li></ul>
<h2>Otros cuidados importantes</h2>
<ul><li>No usés un producto inmediatamente después de otro en la misma superficie o el mismo desagüe: enjuagá bien con agua entre uno y otro.</li><li>No pasés productos a botellas de refresco o de agua: es la causa número uno de intoxicaciones de niños.</li><li>Guardá los químicos en su envase original, bien cerrados y en alto.</li><li>Ventilá siempre al limpiar baños y espacios pequeños.</li></ul>
<h2>Señales de que respiraste un gas tóxico</h2>
<p>Ardor en ojos, nariz o garganta, tos fuerte, dificultad para respirar o mareo. Si pasa:</p>
<ol><li>Salí de inmediato al aire libre y sacá a las demás personas.</li><li>No vuelvas a entrar hasta que el lugar esté ventilado.</li><li>Si los síntomas no pasan rápido o son fuertes, buscá atención médica o llamá al 911.</li><li>En Costa Rica, el Centro Nacional de Control de Intoxicaciones atiende al <b>2223-1028</b>.</li></ol>
''' + SEG_GEN.format('Leé siempre la etiqueta de cada producto antes de usarlo y seguí sus indicaciones. Usá guantes y lentes, ventilá y mantené todos los productos de limpieza fuera del alcance de niños y mascotas.') + '''
<h2>Entonces, ¿cómo limpio bien?</h2>
<p>Usando el producto correcto para cada cosa: el <b>Cloro León Rojo</b> para desinfectar y blanquear, el <b>Vinagre de Limpieza</b> para la limpieza diaria y los malos olores, el <b>Limpiador de Azulejos</b> para el baño y el <b>Desinfectante</b> para los pisos. Uno a la vez, enjuagando entre uno y otro. Mirá la guía completa de <a href="/productos/productos-de-limpieza/">productos de limpieza León Rojo</a>.</p>'''))

A.append(dict(slug='como-desinfectar-corrales-y-establos', img='b8_05', kw='desinfectar corral, establo, lechería, creolina, desinfectante para fincas',
 title='Cómo desinfectar corrales, establos y lecherías',
 desc='Guía práctica para limpiar y desinfectar corrales, establos, lecherías y porquerizas con Creolina, Desinfectante y Detergente en Polvo León Rojo.',
 cta=['b8_05', 'Creolina León Rojo', 'Desinfectante de ágil acción para corrales y establos. En 240 ml, 1/2 litro, litro y galón.'],
 html='''<p class="lead">En una finca, la limpieza no es solo cuestión de apariencia: corrales, establos y lecherías limpios ayudan a reducir malos olores, moscas y focos de contaminación. Con una rutina sencilla y los productos adecuados, la desinfección se vuelve parte del trabajo diario.</p>
<h2>Limpiar primero, desinfectar después</h2>
<p>El error más común es echar desinfectante sobre el estiércol y el barro. La materia orgánica "protege" a los microbios y gasta el producto. Por eso el orden es: <b>sacar, lavar, desinfectar</b>.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li><b>Detergente en Polvo Industrial León Rojo</b> para lavar pisos y paredes.</li><li><b>Creolina León Rojo</b> para corrales, establos, desagües y áreas exteriores.</li><li><b>Desinfectante León Rojo</b> para lecherías, plantas y áreas donde se busca además buen olor.</li><li>Pala, escoba de cerda dura, manguera, guantes, botas y lentes.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Retirá a los animales</b> del área mientras limpiás.</li><li><b>Sacá el estiércol, la paja y la basura</b> con pala y escoba.</li><li><b>Lavá con Detergente en Polvo Industrial</b> disuelto en agua según la etiqueta, restregando pisos, paredes, comederos y bebederos.</li><li><b>Enjuagá bien</b> y dejá escurrir.</li><li><b>Desinfectá</b> con Creolina o Desinfectante diluidos según lo que indica la etiqueta para cada uso.</li><li><b>Dejá secar y ventilar</b> antes de que vuelvan a entrar los animales, siguiendo el tiempo que indique la etiqueta.</li></ol>
''' + SEG_GEN.format('Usá guantes, botas y lentes. No mezclés la Creolina ni el Desinfectante con cloro u otros químicos. No apliqués los productos directamente sobre los animales ni dentro del agua o el alimento, y enjuagá comederos y bebederos según la etiqueta. Guardá todo fuera del alcance de niños y animales.') + '''
<h2>Rutina recomendada</h2>
<ul><li><b>Diario:</b> retirar estiércol y barrer las áreas de más tránsito.</li><li><b>Semanal:</b> lavado con detergente y desinfección de pisos, desagües y pasillos.</li><li><b>Entre lotes de animales:</b> limpieza y desinfección profunda de todo el corral.</li></ul>
<h2>Otros productos útiles en la finca</h2>
<ul><li><b>Alquitrán León Rojo</b> para proteger postes de cerca y corrales de madera.</li><li><b>Pentacell</b> para vigas y estructuras de madera.</li><li><b>Sulfato de Cobre</b> para el control de algas en estanques y reservorios, según la etiqueta.</li></ul>
<p>¿Tenés una lechería o una granja y comprás por volumen? Escribinos al WhatsApp 8994-4763. Ver la <a href="/productos/creolina/">ficha de la Creolina</a>.</p>'''))

A.append(dict(slug='llantas-negras-y-brillantes', img='b5_06', kw='abrillantador de llantas, llantas negras, lavacar, llantilux',
 title='Cómo dejar las llantas negras y brillantes',
 desc='Cómo limpiar y abrillantar las llantas del carro para que queden negras y brillantes, y cuál Llantilux escoger para casa o para lavacar.',
 cta=['b5_06', 'Llantilux-80 León Rojo', 'Deja las llantas negras y brillantes. En litro y galón.'],
 html='''<p class="lead">Un carro puede estar recién lavado, pero si las llantas se ven grises y opacas, parece descuidado. Las llantas negras y brillantes son el detalle que hace que un carro se vea "de lavacar". Lograrlo en casa es fácil si se hace en el orden correcto.</p>
<h2>¿Por qué se ponen grises las llantas?</h2>
<p>El sol, el polvo de frenos y la suciedad del camino resecan el hule y le quitan el color. El abrillantador devuelve el tono negro y le da brillo, pero solo funciona bien sobre una llanta limpia.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li>Shampoo para Autos León Rojo.</li><li>Cepillo para llantas.</li><li>Llantilux-80 o Llantilux-1000 León Rojo.</li><li>Aplicador, esponja o atomizador.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Lavá la llanta</b> con agua y Shampoo para Autos, restregando con el cepillo para quitar el polvo de frenos y la tierra.</li><li><b>Enjuagá</b> y dejá secar por completo.</li><li><b>Aplicá el Llantilux</b> con aplicador, esponja o atomizador, siguiendo la etiqueta.</li><li><b>Distribuilo parejo</b> por toda la cara de la llanta, sin que chorree al aro.</li><li><b>Dejá secar</b> antes de rodar, para que no se pegue el polvo ni salpique la carrocería.</li></ol>
<h2>¿Llantilux-80 o Llantilux-1000?</h2>
<ul><li><b>Llantilux-80:</b> para el uso diario, en casa o en el lavacar.</li><li><b>Llantilux-1000:</b> la versión de alto poder, pensada para lavacar y detallado profesional.</li></ul>
<p>Los dos vienen en litro y galón.</p>
''' + SEG_GEN.format('No apliqués el abrillantador sobre la banda de rodamiento (la parte que toca el piso) ni sobre los pedales o el volante. Evitá el contacto con los ojos, guardalo fuera del alcance de los niños y leé la etiqueta antes de usar.') + '''
<h2>El detallado completo</h2>
<ul><li><b>Aros:</b> ALUX-500 si son de aluminio.</li><li><b>Plásticos negros exteriores:</b> Restaurador de Partes Negras.</li><li><b>Interiores:</b> Abrillantador de Superficies para tablero y vinil.</li><li><b>Pintura:</b> Polish en Pasta y luego Cera en Pasta o Cera Líquida.</li><li><b>Para terminar:</b> Aromatizante León Rojo, en 10 aromas.</li></ul>
<p>Mirá la guía completa de <a href="/productos/productos-para-autos/">productos para autos y lavacar León Rojo</a>.</p>'''))

A.append(dict(slug='como-pulir-y-encerar-el-carro', img='b5_01', kw='pulir carro, encerar carro, polish, cera para autos, microarañazos',
 title='Cómo pulir y encerar el carro paso a paso',
 desc='La diferencia entre polish y cera, y cómo pulir y encerar el carro en casa para quitar microarañazos y dejar la pintura brillante y protegida.',
 cta=['b5_01', 'Polish en Pasta León Rojo', 'Restaura el brillo y elimina microarañazos. En 1/16, 1/8 y 1/4 de galón.'],
 html='''<p class="lead">Con el sol de Costa Rica, la pintura del carro se opaca rápido, y los lavados con esponjas o trapos sucios dejan microarañazos que se notan en la luz. Pulir y encerar devuelve el brillo y protege la pintura. Se puede hacer en casa con paciencia y los productos correctos.</p>
<h2>Polish y cera no son lo mismo</h2>
<ul><li><b>Polish:</b> es una pasta pulidora que corrige la superficie. Quita la capa opaca y los microarañazos. Es el paso que "arregla".</li><li><b>Cera:</b> deja una capa de protección y brillo encima de la pintura. Es el paso que "protege".</li></ul>
<p>El orden siempre es: <b>lavar, pulir, encerar</b>.</p>
<h2>Lo que vas a necesitar</h2>
<ul><li>Shampoo para Autos León Rojo.</li><li>Polish en Pasta León Rojo.</li><li>Cera en Pasta o Cera Líquida para Autos León Rojo.</li><li>Paños de microfibra limpios y aplicadores.</li><li>Una sombra para trabajar.</li></ul>
<h2>Paso a paso</h2>
<ol><li><b>Lavá el carro</b> con Shampoo para Autos y secalo bien con microfibra.</li><li><b>Trabajá a la sombra</b> y con la pintura fría.</li><li><b>Puli por secciones:</b> aplicá un poco de Polish en un paño o aplicador y trabajá con movimientos circulares sobre una sección pequeña, hasta que salga el brillo.</li><li><b>Retirá el residuo</b> con un paño de microfibra limpio.</li><li><b>Encerá:</b> aplicá una capa delgada de Cera en Pasta por secciones, o rociá la Cera Líquida si buscás algo más rápido.</li><li><b>Dale brillo</b> con otro paño limpio cuando la cera opaque un poco.</li></ol>
<h2>Consejos para un mejor resultado</h2>
<ul><li>No trabajés al sol: el producto se seca muy rápido y deja manchas.</li><li>Usá paños distintos para el polish y para la cera.</li><li>Un rayón que llegó a la base o al metal no se quita con polish: necesita trabajo de pintura.</li><li>Entre una encerada y otra, lavá siempre con shampoo para autos, no con jabón de platos.</li></ul>
''' + SEG_GEN.format('Evitá el contacto con los ojos y la piel sensible, trabajá en un lugar ventilado y guardá los productos fuera del alcance de los niños. Leé siempre la etiqueta antes de usar.') + '''
<p>Completá el trabajo con las llantas: te lo explicamos en <a href="/blog/llantas-negras-y-brillantes/">Cómo dejar las llantas negras y brillantes</a>. Todo para el carro en <a href="/productos/productos-para-autos/">productos para autos León Rojo</a>.</p>'''))

A.append(dict(slug='thinner-aguarras-o-espiritu-mineral', img='b1_18', kw='thinner o aguarrás, diferencia thinner aguarrás, diluyente pintura, espíritu mineral',
 title='¿Thinner, aguarrás o espíritu mineral? Cuál usar',
 desc='La diferencia entre thinner, aguarrás, espíritu mineral y canfín, y cuál usar con cada tipo de pintura, laca o barniz. Guía práctica León Rojo.',
 cta=['b1_18', 'Thinner Industrial NC León Rojo', 'Diluyente para lacas y limpieza de pistolas. En 1/2 litro, litro y galón.'],
 html='''<p class="lead">En la ferretería es una de las preguntas más comunes: "¿qué le echo a esta pintura?". Usar el diluyente equivocado puede arruinar el acabado: la pintura no seca, se arruga, se corta o queda pegajosa. Aquí te explicamos cuál va con cada cosa.</p>
<h2>La regla principal</h2>
<p>El diluyente correcto depende del <b>tipo de pintura</b>, y quien lo define es el fabricante de la pintura. Revisá siempre la etiqueta de tu pintura, laca o barniz: ahí dice con qué se diluye y en qué proporción.</p>
<h2>Thinner Industrial NC</h2>
<p>Es el diluyente para <b>lacas nitrocelulosa</b>, las que se usan mucho en carpintería y en algunos trabajos de pintura automotriz. También se usa para <b>limpiar pistolas y equipo de pintura</b> después de trabajar con lacas.</p>
<h2>Aguarrás</h2>
<p>Es el diluyente clásico para <b>pinturas y esmaltes base aceite</b>. También sirve para limpiar brochas y rodillos después de pintar con esmalte.</p>
<h2>Espíritu Mineral</h2>
<p>Es un solvente para <b>diluir pinturas y barnices</b> y limpiar herramientas. Muchos fabricantes de pintura de aceite y barniz lo recomiendan; de nuevo, revisá la etiqueta de tu pintura.</p>
<h2>Canfín (keroseno)</h2>
<p>No es un diluyente de pintura. Se usa para <b>encendido, lámparas y limpieza de piezas</b> con grasa.</p>
<h2>¿Y la pintura de agua?</h2>
<p>Las pinturas a base de agua (látex, acrílicas) se diluyen con agua, no con solventes. Si querés quitar pintura vieja base aceite de un mueble o una puerta, lo que necesitás es el <b>Removedor de Pintura León Rojo</b>.</p>
''' + SEG_GEN.format('Thinner, aguarrás, espíritu mineral y canfín son inflamables. Usalos lejos de llamas, chispas, cigarros y fuentes de calor, en lugares bien ventilados, con guantes y lentes. No respirés los vapores, nunca los pasés a botellas de bebidas y guardalos bien cerrados y fuera del alcance de los niños.') + '''
<h2>Resumen rápido</h2>
<ul><li><b>Laca nitrocelulosa:</b> Thinner Industrial NC.</li><li><b>Esmalte o pintura de aceite:</b> Aguarrás o Espíritu Mineral, según indique el fabricante de la pintura.</li><li><b>Barniz:</b> lo que indique su etiqueta, normalmente Espíritu Mineral o Aguarrás.</li><li><b>Pintura de agua:</b> agua.</li><li><b>Quitar pintura de aceite vieja:</b> Removedor de Pintura.</li></ul>
<p>Mirá la guía de <a href="/productos/thinner-y-solventes/">thinner y solventes León Rojo</a> o pedilos en tu ferretería de confianza.</p>'''))

posts = json.load(open(os.path.join(ROOT, 'posts.json'), encoding='utf-8'))
have = {p['slug'] for p in posts}
n = 0
for a in A:
    open(os.path.join(ROOT, 'posts', a['slug'] + '.html'), 'w', encoding='utf-8').write(a['html'].strip() + '\n')
    if a['slug'] not in have:
        posts.append({'slug': a['slug'], 'title': a['title'], 'desc': a['desc'], 'img': a['img'], 'date': FECHA, 'cta': a['cta'], 'kw': a['kw']}); n += 1
json.dump(posts, open(os.path.join(ROOT, 'posts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('nuevos', n, 'total', len(posts))
