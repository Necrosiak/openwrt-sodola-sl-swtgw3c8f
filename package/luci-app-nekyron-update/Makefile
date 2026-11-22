# SPDX-License-Identifier: Apache-2.0
include $(TOPDIR)/rules.mk
PKG_NAME:=luci-app-nekyron-update
PKG_VERSION:=1.0.0
PKG_RELEASE:=1
PKG_LICENSE:=Apache-2.0
PKGARCH:=all
include $(INCLUDE_DIR)/package.mk

define Package/luci-app-nekyron-update
 SECTION:=luci
 CATEGORY:=LuCI
 TITLE:=Nekyron signed firmware updates
 DEPENDS:=+luci-base +rpcd-mod-ucode +curl +usign
endef

define Package/luci-app-nekyron-update/conffiles
/etc/config/nekyron-update
endef

define Build/Compile
endef

define Package/luci-app-nekyron-update/install
	$(CP) ./files/* $(1)/
endef
$(eval $(call BuildPackage,luci-app-nekyron-update))
