# SPDX-License-Identifier: Apache-2.0
include $(TOPDIR)/rules.mk
PKG_NAME:=luci-theme-nekyron
PKG_VERSION:=2.1.0
PKG_RELEASE:=1
PKG_LICENSE:=Apache-2.0
PKGARCH:=all
include $(INCLUDE_DIR)/package.mk

define Package/luci-theme-nekyron
  SECTION:=luci
  CATEGORY:=LuCI
  SUBMENU:=3. Themes
  TITLE:=Nekyron Network Control
  DEPENDS:=+luci-theme-argon
endef

define Build/Compile
endef

define Package/luci-theme-nekyron/install
	$(CP) ./files/* $(1)/
endef

$(eval $(call BuildPackage,luci-theme-nekyron))
