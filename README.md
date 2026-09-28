# Lanius Films — GitHub Pages

Web estática lista para publicar. No necesita instalación, dependencias ni JavaScript en el navegador.

## Subir a GitHub
Descomprime el ZIP y sube su contenido a la raíz de `laniusfilms/laniusfilms.github.io`, sustituyendo los archivos del mismo nombre. `index.html` debe quedar en la raíz, no dentro de otra carpeta. Conserva Pages en main / root. No necesitas cambiar el dominio.

## Actualizar contenido
Edita `content.json` y ejecuta `python3 build.py` desde esta carpeta. Después sube los HTML regenerados, las imágenes y el contenido actualizado. También puedes editar directamente los HTML, pero una regeneración sobrescribirá esos cambios.

- `projects`: orden de los proyectos, títulos, descripciones, categorías y galerías.
- `image`: nombre de imagen en `assets`, sin extensión; las imágenes son JPG.
- `alt`: descripción accesible de la portada.
- `video_url`: URL real del vídeo; vacío muestra “Film link coming soon”, sin enlace falso.
- `reel_url`: URL del reel; vacío conserva el CTA al canal de YouTube.
- `email`, `youtube`, `archive`: datos conservados de la web publicada.
- `styles.css`: estilos, colores y adaptación a móvil.

## Imágenes
Se utilizan las diez imágenes recuperadas de la conversación. Se han exportado copias JPG optimizadas (máximo 2000 px) sin modificar los originales. Portadas: coche bajo la lluvia, pescador entrando al mar, Valeria con vestido verde al atardecer y Alura en hotel con copa. Las otras imágenes aparecen en las galerías de sus respectivos proyectos.

Spec AI Campaigns utiliza una composición tipográfica provisional, ya que no se aportó una imagen identificada para esa categoría. Se han añadido The Passenger, Jarjacha (Vex Darkness), Sant Joan y Madeira (Valeria Satie), y The Morning After (Spec AI Campaigns). Siguen pendientes el vídeo de Alura Thorne y el reel. No se han inventado clientes, resultados ni créditos.

## Vista local
Abre `index.html` directamente o ejecuta `python3 -m http.server 8000` y visita http://localhost:8000.

## Varios vídeos por proyecto
`videos` contiene una lista de objetos con `title` y `url`. Sus botones aparecen tanto en la home como en la página del proyecto. `video_url` queda como respaldo para proyectos sin lista.
