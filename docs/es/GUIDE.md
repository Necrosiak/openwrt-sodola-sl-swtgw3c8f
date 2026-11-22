[English](../en/GUIDE.md) · [Français](../INSTALLATION.md) · [Deutsch](../de/GUIDE.md) · [Español](../es/GUIDE.md) · [Italiano](../it/GUIDE.md) · [Português](../pt/GUIDE.md)

# Instalación, actualizaciones y seguridad

## Antes de instalar

Usar únicamente el hardware SL-SWTGW3C8F compatible. Comprobar placa, memoria y distribución de la flash. Conservar copias verificadas de las particiones originales y una consola serie compatible. Verificar conexiones y niveles eléctricos: el cable de consola no se conecta a un puerto Ethernet cualquiera.

Comprobar las sumas de la versión con `sha256sum -c SHA256SUMS`. Probar primero initramfs en RAM. Los comandos del gestor de arranque dependen de la revisión. No adivinar direcciones ni sobrescribir las particiones del gestor de arranque o de identidad. La imagen pública completa todavía no se ha arrancado en hardware real.

## Primer acceso

La administración obtiene una dirección del servidor DHCP de la red. Buscar `switch-sodola` en las concesiones. Para conexión directa, asignar temporalmente `169.254.1.2/24` al PC y abrir `https://169.254.1.1/`.

Root está bloqueado inicialmente. Establecer una contraseña propia con `passwd` desde la consola serie. Las claves SSH y el certificado HTTPS autofirmado se generan para cada dispositivo. Confirmar su identidad antes de confiar en el certificado. Ajustar la hora antes de descargar por HTTPS.

## Actualizaciones y funciones opcionales

Desde este OpenWrt, verificar una imagen compatible con `sysupgrade -T /tmp/image-sysupgrade.bin` y guardar la configuración. Continuar solo si la comprobación tiene éxito. No forzar imágenes incompatibles. Revisar los ajustes conservados tras actualizar.

El flujo diario crea candidatos sin probar; no instala nada en el switch y no garantiza corregir todas las CVE. Evitar firmware genérico y actualizaciones globales de paquetes para esta placa personalizada.

Adblock-fast está desactivado. Para filtrar, los clientes deben utilizar su servidor DNS. tcpdump-mini no necesariamente ve el tráfico conmutado directamente por hardware. La duplicación de puertos debe validarse; mantener privadas las capturas.

Home Assistant: se proporcionan instrucciones y una ACL de solo lectura. La integración completa y el control de puertos/VLAN no están validados. No hay cuenta HA ni permisos administrativos nuevos activos por defecto.

Instalar únicamente el idioma deseado. Las traducciones incompletas utilizan el inglés como alternativa.

---

[GitHub](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f) · [Releases](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases)
