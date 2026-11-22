[English](../en/GUIDE.md) · [Français](../INSTALLATION.md) · [Deutsch](../de/GUIDE.md) · [Español](../es/GUIDE.md) · [Italiano](../it/GUIDE.md) · [Português](../pt/GUIDE.md)

# Instalação, atualizações e segurança

## Antes da instalação

Utilizar apenas hardware SL-SWTGW3C8F compatível. Verificar placa, memória e partições da flash. Guardar cópias verificadas das próprias partições originais e uma consola série compatível. Confirmar a pinagem e os níveis elétricos: o cabo de consola não deve ser ligado a qualquer porta Ethernet.

Verificar as somas da versão com `sha256sum -c SHA256SUMS`. Testar primeiro initramfs em RAM. Os comandos do gestor de arranque dependem da revisão. Não adivinhar endereços nem sobrescrever o gestor de arranque ou as partições de identidade. A imagem pública completa ainda não foi iniciada em hardware real.

## Primeiro acesso

A administração recebe um endereço do servidor DHCP da rede. Procurar `switch-sodola` na lista de concessões. Para ligação direta, atribuir temporariamente `169.254.1.2/24` ao PC e abrir `https://169.254.1.1/`.

Root começa bloqueado. Definir uma palavra-passe própria com `passwd` através da consola série. As chaves SSH e o certificado HTTPS autoassinado são gerados em cada dispositivo. Confirmar a identidade antes de confiar no certificado. Ajustar a hora antes de transferências HTTPS.

## Atualizações e funções opcionais

A partir deste OpenWrt, verificar uma imagem compatível com `sysupgrade -T /tmp/image-sysupgrade.bin` e guardar a configuração. Continuar apenas se a verificação for bem-sucedida. Não forçar imagens incompatíveis. Rever as definições preservadas após atualizar.

O workflow diário gera candidatos não testados; não instala firmware no switch e não garante corrigir todas as CVE. Evitar firmware genérico e atualizações globais de pacotes nesta placa personalizada.

Adblock-fast está desativado. Os clientes precisam de utilizar o respetivo servidor DNS para serem filtrados. tcpdump-mini pode não ver tráfego comutado diretamente pelo hardware. A duplicação de portas precisa de validação; manter as capturas privadas.

Home Assistant: estão disponíveis instruções e uma ACL apenas de leitura. A integração completa e o controlo de portas/VLAN não estão validados. Nenhuma conta HA ou nova permissão administrativa está ativa por predefinição.

Instalar apenas o idioma pretendido. As traduções em falta são apresentadas em inglês.

---

[GitHub](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f) · [Releases](https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases)
