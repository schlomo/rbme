DPKG=dpkg
DPKG_OPTS=-b
.PHONY: info repo deb

TOPLEVEL = rbme rbme.conf DEBIAN

GITREV := HEAD

VERSION := $(shell git rev-list $(GITREV) -- $(TOPLEVEL) 2>/dev/null| wc -l)$(EXTRAREV)

info: deb
	dpkg-deb -I out/*_all.deb
	dpkg-deb -c out/*_all.deb

deb:	clean
	rm -Rf build
	mkdir -p out build/DEBIAN
	setfacl -b out build
	chmod -vR g-s+rx,o+rx build
	install -m 0644 rbme.conf -D build/etc/rbme.conf
	install -m 0755 rbme -D build/usr/bin/rbme
	sed -i -e 's/VERSION=.*/VERSION=$(VERSION)/' build/usr/bin/rbme
	install -m 0644 -t build/DEBIAN DEBIAN/*
	sed -i -e 's/Version:.*/Version: $(VERSION)/' build/DEBIAN/control
	mkdir -p build/usr/share/doc/rbme
	mv build/DEBIAN/copyright build/usr/share/doc/rbme/copyright
	git log | gzip -n9 >build/usr/share/doc/rbme/changelog.gz
	chmod -R g-w build
	fakeroot ${DPKG} ${DPKG_OPTS} build out
	rm -Rf build
	lintian --suppress-tags binary-without-manpage -i out/*_all.deb
	git add -A

repo: deb
	../putinrepo.sh out/*_all.deb

clean:
	rm -fr out build


