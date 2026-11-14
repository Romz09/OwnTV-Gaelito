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
