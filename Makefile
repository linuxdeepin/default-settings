all: 

install:
	mkdir -p $(DESTDIR)/usr/share
	mkdir -p $(DESTDIR)/etc/fonts/conf.d
	cp -r etc.d/* $(DESTDIR)/etc/
	chmod 755 $(DESTDIR)/etc/X11/xinit/xinitrc.d/50-systemd-user.sh
	cp -r usr.share.d/* $(DESTDIR)/usr/share
	install -Dm755 dde-first-run $(DESTDIR)/usr/bin/dde-first-run
	for i in `ls $(DESTDIR)/usr/share/fontconfig/conf.avail/ | grep .conf$$`;do \
		ln -sf /usr/share/fontconfig/conf.avail/$${i} $(DESTDIR)/etc/fonts/conf.d/$${i}; \
	done
