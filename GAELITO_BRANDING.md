# Gaelito TV — personalización visual

Esta rama adapta la identidad visual de OwnTV para **Gaelito TV** sin cambiar el paquete Android, los servicios, las listas IPTV ni el motor de reproducción.

## Paleta propuesta
- Fondo azul noche: `#101C33`
- Superficies: `#182C49`
- Acento turquesa de marca propuesto: `#27D5C3`
- Texto claro propuesto: `#F5F7FA`

## Aplicado en esta primera fase
- Fondo de arranque en `app/src/main/res/values/colors.xml`
- Fondo y superficies de la interfaz Stage oscura en `StageTokens.kt`
- Se conserva `applicationId = tv.own.owntv` y `OwnTV_Core` sin cambios

## Pendiente para completar la identidad
1. Diseñar y aprobar logotipo, banner de Android TV y variantes de icono.
2. Sustituir los recursos de `mipmap*`, `drawable*` y las pantallas splash correspondientes; el selector de iconos depende de `OwnTV_Core`.
3. Alinear la paleta Material3: sus neutros vienen de `OwnTVPalette` en el núcleo compartido. No se han cambiado para evitar afectar dependencias.
4. Definir el acento turquesa predeterminado: el ajuste actual depende del núcleo y de las preferencias guardadas.
5. Ejecutar pruebas de Gradle, verificar contraste, splash, navegación D-pad, tema claro y oscuro en Android TV.

**Aviso:** cambios de apariencia iniciales, no una personalización completa ni un APK validado. Se mantienen las atribuciones y licencia GPLv3.

## Mascota visual aprobada (14 de noviembre de 2026)
El diseño aprobado es un bebé caricaturesco sonriente con gorra azul, guiño, pulgar arriba y televisor rotulado «Gaelito TV». Los archivos PNG preparados son `gaelito_tv_logo.png`, `gaelito_tv_icon_512.png` y `gaelito_tv_banner_1280x720.png` (entregados por separado; todavía no integrados en recursos Android de esta rama). Antes de sustituir iconos y banners, validar encuadre en launcher Android TV y adaptar variantes y splash existentes.

## Mascota aprobada — bebé divertido

Se aprobó el logotipo del bebé con gorra azul, guiño, pulgar arriba y televisor Gaelito TV.
Los archivos PNG aprobados se entregaron en `gaelito_tv_identidad_visual.zip` dentro de la conversación.
No se han subido aún los PNG binarios a GitHub: deben instalarse desde ese paquete para conservar exactamente la ilustración aprobada.

### Integración reproducible

1. Descargar y descomprimir `gaelito_tv_identidad_visual.zip`.
2. Instalar Pillow: `python3 -m pip install Pillow`.
3. Ejecutar `python3 scripts/install_gaelito_brand.py /ruta/a/la/carpeta`.
4. Revisar los nuevos PNG y los cambios en `AndroidManifest.xml` y los temas de arranque.
5. Compilar con `./gradlew :app:assembleDebug` y probar en Android TV.
6. Confirmar y subir esos archivos a la rama `branding/gaelito-tv`, no a `main`.

El script conserva los nombres de actividades y temas para no romper el selector de iconos del núcleo. No modifica reproductor, listas ni identificador Android.
