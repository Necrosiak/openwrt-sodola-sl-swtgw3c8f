# SPDX-License-Identifier: Apache-2.0
include $(TOPDIR)/rules.mk
PKG_NAME:=luci-app-nekyron-https
PKG_VERSION:=1.0.0
PKG_RELEASE:=1
PKG_LICENSE:=Apache-2.0
PKGARCH:=all
include $(INCLUDE_DIR)/package.mk

define Package/luci-app-nekyron-https
 SECTION:=luci
 CATEGORY:=LuCI
 TITLE:=Nekyron per-device HTTPS certificates
 DEPENDS:=+luci-base +rpcd-mod-ucode +px5g-mbedtls
endef

define Package/luci-app-nekyron-https/conffiles
/etc/config/nekyron-https
endef

define Build/Compile
endef

define Package/luci-app-nekyron-https/install
	$(CP) ./files/* $(1)/
endef
$(eval $(call BuildPackage,luci-app-nekyron-https))
