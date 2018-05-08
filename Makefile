ARCH=$(shell dpkg --print-architecture)
ifeq ($(ARCH), amd64)
	ORIGIN=true
else ifeq ($(ARCH), i386)
	ORIGIN=true
endif

all: 

install:
	mkdir -p $(DESTDIR)/usr/share
	mkdir -p $(DESTDIR)/etc/fonts/conf.d
	mkdir -p $(DESTDIR)/etc/apt
	cp -r etc.d/* $(DESTDIR)/etc/
	cp -r usr.share.d/* $(DESTDIR)/usr/share
	if [ $(ORIGIN) = true ]; then install -Dm644 sources.list.origin $(DESTDIR)/etc/apt/sources.list.origin; fi
	install -Dm755 dde-first-run $(DESTDIR)/usr/bin/dde-first-run
	install -Dm644 sysctl.d/90-deepin.conf $(DESTDIR)/usr/lib/sysctl.d/deepin.conf
	install -Dm644 udev.rules.d/99-deepin.rules $(DESTDIR)/lib/udev/rules.d/99-deepin.rules
	for i in `ls $(DESTDIR)/usr/share/fontconfig/conf.avail/ | grep .conf$$`;do \
		ln -sf /usr/share/fontconfig/conf.avail/$${i} $(DESTDIR)/etc/fonts/conf.d/$${i}; \
	done
