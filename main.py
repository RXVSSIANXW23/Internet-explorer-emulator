<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Internet Explorer Mini 100 Respuestas Reales</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: 'MS Sans Serif', Arial, sans-serif; background-color: #d4d0c8; margin: 0; padding: 10px; display: flex; justify-content: center; }
        .ie-window { border: 2px solid #666; background-color: #d4d0c8; width: 450px; height: 500px; display: flex; flex-direction: column; box-shadow: 4px 4px 10px rgba(0,0,0,0.3); }
        .ie-header { background: linear-gradient(to right, #0058e6, #3a95ff); color: white; padding: 4px 8px; font-weight: bold; font-size: 12px; display: flex; justify-content: space-between; align-items: center; }
        .ie-buttons { display: flex; gap: 2px; }
        .ie-btn { background: #d4d0c8; border: 1px solid #fff; border-right-color: #404040; border-bottom-color: #404040; width: 16px; height: 14px; font-size: 9px; text-align: center; line-height: 12px; color: black; cursor: pointer; }
        .ie-nav-bar { background-color: #d4d0c8; padding: 4px; border-bottom: 2px solid #808080; display: flex; align-items: center; gap: 5px; font-size: 11px; }
        .address-bar { flex-grow: 1; background: white; border: 2px inset #fff; padding: 2px 5px; font-family: monospace; font-size: 11px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
        .ie-body { flex-grow: 1; background: white; border: 2px inset #fff; overflow-y: auto; padding: 12px; font-family: Arial, sans-serif; }
        .list-view button { background: none; border: none; border-bottom: 1px solid #eee; padding: 8px; text-align: left; cursor: pointer; font-size: 12px; width: 100%; display: block; color: #003399; }
        .list-view button:hover { background-color: #e5f1fb; text-decoration: underline; }
        .btn-volver { background-color: #e1e1e1; border: 1px solid #707070; padding: 5px 10px; cursor: pointer; font-size: 12px; margin-bottom: 15px; display: inline-block; }
        .btn-volver:hover { background-color: #fbdb95; }
        .answer-title { color: #003399; border-bottom: 2px solid #003399; padding-bottom: 4px; margin-top: 0; font-size: 14px; }
        .res-texto { font-size: 15px; color: #111; line-height: 1.4; margin: 15px 0; font-weight: bold; }
    </style>
</head>
<body>

<div class="ie-window">
    <div class="ie-header">
        <span>🌐 Internet Explorer Mini 100 Respuestas</span>
        <div class="ie-buttons"><div class="ie-btn">_</div><div class="ie-btn">🗖</div><div class="ie-btn">X</div></div>
    </div>
    <div class="ie-nav-bar"><span>Dirección:</span><div class="address-bar" id="url-bar">http://ie-mini.local/inicio</div></div>
    <div class="ie-body" id="contenido-web"></div>
</div>

<script>
    const baseDatos = [
        { q: "¿Por qué el cielo es azul?", a: "La atmósfera dispersa la luz solar, y la azul viaja en ondas más cortas, esparciéndose más." },
        { q: "¿Cuántos huesos tiene un adulto?", a: "Un ser humano adulto tiene exactamente 206 huesos estructurados en todo su esqueleto interno." },
        { q: "¿Quién pintó la Mona Lisa?", a: "Fue una obra maestra pintada por el polímata italiano Leonardo da Vinci en el siglo XVI." },
        { q: "¿Qué año llegó el hombre a la Luna?", a: "Ocurrió históricamente el 20 de julio de 1969 gracias a la exitosa misión espacial Apolo 11." },
        { q: "¿Cuál es la capital de Francia?", a: "París es la capital oficial, centro mundial del arte, la moda y la cultura." },
        { q: "¿Cuál es el río más largo del mundo?", a: "El río Amazonas, ubicado en Sudamérica, es el más largo y caudaloso de todo el planeta." },
        { q: "¿Qué país tiene forma de bota?", a: "Italia posee una silueta geográfica peninsular muy característica que simula una bota." },
        { q: "¿Cuál es el océano más grande?", a: "El Océano Pacífico es la masa de agua más extensa, cubriendo un tercio de la superficie terrestre." },
        { q: "¿Cuál es el planeta más cercano al Sol?", a: "Mercurio es el planeta más cercano de nuestro sistema solar y el más pequeño en tamaño." },
        { q: "¿Cuál es la capital de Australia?", a: "Es Canberra, elegida estratégicamente como un término medio entre Sídney y Melbourne." },
        { q: "¿Cuál es el edificio más alto del mundo?", a: "El rascacielos Burj Khalifa ubicado en Dubái, con una altura estructural de 828 metros." },
        { q: "¿Quién escribió Don Quijote?", a: "Miguel de Cervantes Saavedra, una de las máximas figuras de la literatura mundial." },
        { q: "¿Cuál es la velocidad de la luz?", a: "La luz se desplaza de forma constante a casi 300.000 kilómetros por segundo en el vacío." },
        { q: "¿Quién descubrió la penicilina?", a: "El científico británico Alexander Fleming en 1928 de forma completamente accidental." },
        { q: "¿Cuál es el hueso más largo?", a: "El fémur, ubicado en el muslo, es el hueso más largo, fuerte y resistente de la anatomía." },
        { q: "¿Cuántos dientes tiene un adulto?", a: "Una dentadura humana adulta y sana completa consta de un total de 32 piezas dentales." },
        { q: "¿Qué país inventó la pizza?", a: "Se originó en la hermosa ciudad de Nápoles, Italia, con su famosa variante Margarita." },
        { q: "¿Cuál es el país más grande?", a: "Rusia es la nación con mayor superficie territorial en el planeta por un amplio margen." },
        { q: "¿Cuál es la capital de Canadá?", a: "Ottawa es la capital oficial y el núcleo político del país norteamericano." },
        { q: "¿Cuántos minutos tiene un día?", a: "Un día solar completo consta de 24 horas exactas, lo que equivale a 1.440 minutos." },
        { q: "¿Qué es la fotosíntesis?", a: "Proceso de las plantas para transformar luz solar y dióxido de carbono en azúcares y energía." },
        { q: "¿Cuál es la capital de Japón?", a: "Tokio es la capital, una metrópolis que mezcla rascacielos modernos con templos antiguos." },
        { q: "¿Qué gas respiramos principalmente?", a: "El aire contiene un 78% de nitrógeno y un 21% de oxígeno, que es el que usamos para vivir." },
        { q: "¿Cuál es el animal más rápido en tierra?", a: "El guepardo o chita puede alcanzar velocidades de hasta 120 km/h en carreras de corta distancia." },
        { q: "¿Qué inventó Nikola Tesla?", a: "Diseñó el sistema moderno de electricidad por corriente alterna y la bobina de inducción." },
        { q: "¿Por qué flotan los barcos?", a: "Por el principio de Arquímedes; desplazan un volumen de agua cuyo peso es igual al del barco." },
        { q: "¿Qué es un año bisiesto?", a: "Un año de 366 días para alinear las estaciones astronómicas con nuestro calendario humano." },
        { q: "¿Cuál es el metal más caro del mundo?", a: "El rodio es el metal más caro debido a su extrema escasez y gran demanda industrial." },
        { q: "¿Qué significa ADN?", a: "Ácido Desoxirribonucleico, la molécula que porta los datos genéticos de un ser vivo." },
        { q: "¿Cuál es el mamífero más grande?", a: "La ballena azul, un gigantesco cetáceo marino que supera los 30 metros de longitud." },
        { q: "¿Cuántos continentes existen?", a: "Se consideran 6 continentes: América, Europa, Asia, África, Oceanía y la Antártida." },
        { q: "¿Qué causa las mareas del mar?", a: "La fuerza de atracción gravitatoria que ejercen la Luna y el Sol sobre la Tierra." },
        { q: "¿Cuál es la montaña más alta?", a: "El Monte Everest, con 8.848 metros sobre el nivel del mar en la cordillera del Himalaya." },
        { q: "¿Quién inventó el teléfono?", a: "Fue ideado originalmente por Antonio Meucci, aunque Graham Bell lo patentó primero." },
        { q: "¿Cómo respiran los peces?", a: "Absorbiendo el oxígeno que está disuelto en el agua a través de sus branquias." },
        { q: "¿Cuál es la capital de Italia?", a: "Roma, conocida como la Ciudad Eterna por su inmensa cantidad de monumentos antiguos." },
        { q: "¿Quién compuso la Quinta Sinfonía?", a: "El célebre e histórico compositor alemán Ludwig van Beethoven." },
        { q: "¿Cuál es el felino más grande?", a: "El tigre es el felino de mayor tamaño en el mundo, superando notablemente al león." },
        { q: "¿Qué es la gravedad?", a: "La fuerza física invisible que atrae los objetos masivos hacia el centro de la Tierra." },
        { q: "¿Cuál es la isla más grande del mundo?", a: "Groenlandia es considerada la isla más grande; Australia cuenta como masa continental." },
        { q: "¿Cómo se forma un arcoíris?", a: "Por la descomposición de la luz solar al refractarse y reflejarse en gotas de lluvia." },
        { q: "¿Qué país produce más café?", a: "Brasil lidera mundialmente la producción y exportación de granos de café de alta calidad." },
        { q: "¿Cuál es el órgano más grande humano?", a: "La piel es el órgano de mayor tamaño, protegiendo todo nuestro cuerpo del exterior." },
        { q: "¿Quién inventó la bombilla eléctrica?", a: "Thomas Alva Edison patentó la primera bombilla comercialmente viable y duradera." },
        { q: "¿Cuál es el país más poblado?", a: "La India es actualmente el estado con mayor número de habitantes en el planeta." },
        { q: "¿Qué es la Vía Láctea?", a: "Es la galaxia espiral en la que se encuentran nuestro Sistema Solar y la Tierra." },
        { q: "¿Cuál es el monumento más visitado?", a: "El Museo del Louvre en París suele liderar el récord de turistas anuales a nivel mundial." },
        { q: "¿Qué es un agujero negro?", a: "Región del espacio con una gravedad tan intensa que ni siquiera la luz puede escapar de ella." },
        { q: "¿Cuál es la moneda oficial de Japón?", a: "El Yen es la divisa económica utilizada en todo el territorio japonés." },
        { q: "¿Por qué parpadeamos?", a: "Para mantener los ojos limpios, húmedos y protegidos contra partículas externas del aire." },
        { q: "¿Qué es el calentamiento global?", a: "El aumento a largo plazo de la temperatura del sistema climático de la Tierra por gases." },
        { q: "¿Quién fue Cleopatra?", a: "Fue la última gobernante activa de la dinastía ptolemaica del Antiguo Egipto." },
        { q: "¿Cuál es el país más pequeño?", a: "El Vaticano es el estado soberano más pequeño del mundo, ubicado dentro de Roma." },
        { q: "¿Por qué sudamos?", a: "Es el mecanismo del cuerpo para regular la temperatura interna y enfriarnos." },
        { q: "¿Cuál es el ave más grande?", a: "El avestruz es el ave de mayor tamaño; no puede volar pero corre a gran velocidad." },
        { q: "¿Qué es un ecosistema?", a: "Conjunto de seres vivos que interactúan entre sí y con el medio ambiente que los rodea." },
        { q: "¿Cuál es el idioma más hablado?", a: "El inglés es el idioma más hablado a nivel mundial si contamos a los no nativos." },
        { q: "¿Por qué el mar es salado?", a: "Por el desgaste de las rocas terrestres que arrastra minerales disueltos hacia los ríos." },
        { q: "¿Cómo se genera la electricidad?", a: "Transformando energía mecánica, química o solar en flujo de electrones conductores." },
        { q: "¿Qué es la capa de ozono?", a: "Zona de la atmósfera que absorbe entre el 97% y el 99% de la radiación ultravioleta del Sol." },
        { q: "¿Cuál es el árbol más alto?", a: "La secuoya roja de California, que puede superar fácilmente los 115 metros de altura." },
        { q: "¿Quién escribió Romeo y Julieta?", a: "El dramaturgo y poeta inglés William Shakespeare a finales del siglo XVI." },
        { q: "¿Qué causa un terremoto?", a: "La liberación repentina de energía debido al movimiento de las placas tectónicas terrestres." },
        { q: "¿Cuál es el pez más grande?", a: "El tiburón ballena, un pez inofensivo que puede medir hasta 12 metros de largo." },
        { q: "¿Por qué la sangre es roja?", a: "Por la presencia de hemoglobina, una proteína que contiene hierro y transporta oxígeno." },
        { q: "¿Qué es la energía renovable?", a: "Energía que se obtiene de fuentes naturales inagotables como el sol, viento o agua." },
        { q: "¿Cuál es la capital de Egipto?", a: "El Cairo es la vibrante capital egipcia, ubicada cerca de las famosas pirámides de Guiza." },
        { q: "¿Quién inventó el telescopio?", a: "Hans Lippershey hizo los primeros diseños, pero Galileo lo apuntó al cielo por primera vez." },
        { q: "¿Qué es la inflación?", a: "El aumento generalizado y sostenido de los precios de los bienes y servicios existentes." },
        { q: "¿Por qué duelen los músculos?", a: "Por microrroturas en las fibras musculares tras realizar un esfuerzo físico intenso." },
        { q: "¿Qué es la fibra óptica?", a: "Filamento transparente de vidrio o plástico que transmite datos mediante pulsos de luz." },
        { q: "¿Quién fue Albert Einstein?", a: "Físico alemán famoso por desarrollar la Teoría de la Relatividad General y Especial." },
        { q: "¿Qué es el código binario?", a: "Sistema numérico de dos dígitos (0 y 1) utilizado por computadoras para procesar datos." },
        { q: "¿Cuál es el deporte más popular?", a: "El fútbol es el deporte rey, con miles de millones de seguidores y practicantes globales." },
        { q: "¿Cuál es el metal más ligero?", a: "El litio es el metal sólido con menor densidad y peso atómico en la tabla periódica." },
        { q: "¿Qué animal produce la miel?", a: "Las abejas melíferas recolectan néctar de flores y lo transforman en miel en su colmena." },
        { q: "¿Cuál es la flor más cultivada?", a: "La rosa es la flor más popular y cultivada en todo el mundo por su belleza y aroma." },
        { q: "¿Qué planeta tiene anillos vistosos?", a: "Saturno destaca por su espectacular sistema de anillos compuestos de hielo y roca." },
        { q: "¿Cuál es la capital de Alemania?", a: "Berlín, famosa por su historia política, museos y el antiguo e icónico muro dividido." },
        { q: "¿Qué es un año luz?", a: "La distancia gigantesca que recorre la luz en el vacío a lo largo de un año entero." },
        { q: "¿Cuántos lados tiene un hexágono?", a: "Un hexágono es una figura geométrica plana regular compuesta por 6 lados rectos." },
        { q: "¿Cuál es el país más pequeño de América?", a: "San Cristóbal y Nieves es la nación soberana de menor superficie en el continente." },
        { q: "¿Qué gas causa el efecto invernadero?", a: "El dióxido de carbono y el metano son los principales gases que retienen calor terrestre." },
        { q: "¿Qué ciencia estudia los fósiles?", a: "La paleontología se encarga de examinar los restos orgánicos del pasado geológico." },
        { q: "¿Cuál es la capital de España?", a: "Madrid es la capital del reino español, situada geográficamente en el centro del país." },
        { q: "¿Qué mamífero vuela de verdad?", a: "El murciélago es el único mamífero capaz de sostener un vuelo activo y controlado." },
        { q: "¿Cuál es el desierto cálido más grande?", a: "El desierto del Sáhara, ubicado en la zona norte del gran continente africano." },
        { q: "¿Qué inventaron los hermanos Wright?", a: "Lograron el primer vuelo propulsado y controlado de un avión en el año 1903." },
        { q: "¿Cuál es el planeta más grande?", a: "Júpiter es un coloso gaseoso y el planeta de mayor tamaño en nuestro sistema solar." },
        { q: "¿Qué instrumento mide la temperatura?", a: "El termómetro es la herramienta física calibrada que se usa para medir los grados." },
        { q: "¿Qué se celebra el 25 de diciembre?", a: "La Navidad, festividad de origen cristiano que conmemora el nacimiento de Jesús." },
        { q: "¿Cuál es el mineral más duro?", a: "El diamante es la sustancia natural más dura conocida según la escala mineral de Mohs." },
        { q: "¿Cuál es la capital de Inglaterra?", a: "Londres es la capital del Reino Unido, situada a orillas del histórico río Támesis." },
        { q: "¿Qué órgano bombea la sangre?", a: "El corazón es el músculo vital encargado de bombear sangre a todo el organismo." },
        { q: "¿Cuántas patas tiene una araña?", a: "Todas las especies de arañas pertenecen a los arácnidos y poseen exactamente 8 patas." },
        { q: "¿Cuál es la capital de México?", a: "La Ciudad de México (CDMX), construida sobre las ruinas de la antigua Tenochtitlan." },
        { q: "¿Qué sustancia congela a los 0°C?", a: "El agua pura pasa de estado líquido a sólido (hielo) al alcanzar los cero grados Celsius." },
        { q: "¿Qué instrumento musical tiene teclas?", a: "El piano es un instrumento de cuerda percutida que se activa mediante un teclado mecánico." },
        { q: "¿Cuál es la estrella del sistema solar?", a: "El Sol es la estrella enana amarilla central en torno a la cual orbitan todos los planetas." },
        { q: "¿Qué máquina procesa datos digitales?", a: "El ordenador o computadora es el dispositivo electrónico diseñado para procesar algoritmos." }
    ];

    const cuerpoWeb = document.getElementById('contenido-web');
    const urlBar = document.getElementById('url-bar');

    function irAlInicio() {
        urlBar.innerText = "http://ie-mini.local/inicio";
        let htmlLista = `<div class="list-view"><h4 style="margin-top:0; text-align:center;">Respuestas en 100 caracteres</h4>`;
        baseDatos.forEach((item, index) => {
            htmlLista += `<button onclick="verRespuesta(${index})">🔹 <strong>${index + 1}.</strong> ${item.q}</button>`;
        });
        htmlLista += `</div>`;
        cuerpoWeb.innerHTML = htmlLista;
    }

    window.verRespuesta = function(index) {
        const item = baseDatos[index];
        urlBar.innerText = `http://ie-mini.local/respuesta?id=${index + 1}`;
        
        let respuestaCortada = item.a.substring(0, 100);
        
        cuerpoWeb.innerHTML = `
            <button class="btn-volver" onclick="irAlInicio()">⬅ Volver al Inicio</button>
            <h4 class="answer-title">${item.q}</h4>
            <div class="res-texto">"${respuestaCortada}"</div>
            <p style="font-size:10px; color:green; margin:0;">✓ Longitud: ${respuestaCortada.length} caracteres.</p>
        `;
        cuerpoWeb.scrollTop = 0;
    };

    irAlInicio();
</script>

</body>
</html>
