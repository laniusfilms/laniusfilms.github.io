# Lanius Films — GitHub Pages

Web estática lista para publicar. No necesita instalación, dependencias ni JavaScript en el navegador.

## Subir a GitHub
Descomprime el ZIP y sube su contenido a la raíz de `laniusfilms/laniusfilms.github.io`, sustituyendo los archivos del mismo nombre. `index.html` debe quedar en la raíz, no dentro de otra carpeta. Conserva Pages en main / root. No necesitas cambiar el dominio.

## Actualizar contenido
Edita `content.json` y ejecuta `python3 build.py` desde esta carpeta. Después sube los HTML regenerados, las imágenes y el contenido actualizado. También puedes editar directamente los HTML, pero una regeneración sobrescribirá esos cambios.

- `projects`: orden de los proyectos, títulos, descripciones, categorías y galerías.
- `image`: nombre de imagen en `assets`, sin extensión; las imágenes son JPG.
- `alt`: descripción accesible de la portada.
- `cover_url`: portada externa opcional (usada en Spec AI Campaigns).
- `more_work`: selección adicional de películas de la home.
- `reel_thumbnail`: miniatura del showreel.
- `video_url`: URL real del vídeo; vacío muestra “Film link coming soon”, sin enlace falso.
- `reel_url`: URL del reel; vacío conserva el CTA al canal de YouTube.
- `email`, `youtube`, `archive`: datos conservados de la web publicada.
- `styles.css`: estilos, colores y adaptación a móvil.

## Imágenes
Se utilizan las diez imágenes recuperadas de la conversación. Se han exportado copias JPG optimizadas (máximo 2000 px) sin modificar los originales. Portadas: coche bajo la lluvia, pescador entrando al mar, Valeria con vestido verde al atardecer y Alura en hotel con copa. Las otras imágenes aparecen en las galerías de sus respectivos proyectos.

El logo original se conserva sin modificar en `assets/lanius-logo.png`, utilizado en cabecera, pie y favicon. Las miniaturas del showreel y de los vídeos usan las URLs públicas de YouTube: requieren conexión y se pueden sustituir por nuevas URLs en `content.json`. Spec AI Campaigns usa la miniatura de The Morning After.

La selección incluye 17 películas y el showreel de 2026. Se conserva el orden principal: The Passenger, Vex Darkness, Valeria Satie, Alura Thorne y Spec AI Campaigns. No se han inventado clientes, resultados ni créditos.

## Vista local
Abre `index.html` directamente o ejecuta `python3 -m http.server 8000` y visita http://localhost:8000.

## Varios vídeos por proyecto
`videos` contiene objetos con `title`, `url`, `thumbnail` y `category`. La home enlaza la pieza principal y la colección; cada página de proyecto muestra todas sus películas con miniaturas. `video_url` queda como respaldo para proyectos sin lista.
