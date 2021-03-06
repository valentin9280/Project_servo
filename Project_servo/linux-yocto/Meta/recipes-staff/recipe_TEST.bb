SUMMARY = "Test recipe python"
SECTION = "python"
LICENSE = "INSSET"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=4d92cd373abda3937c2bc47fbc49d690"

SRC_URI = "file://Test_1-0.py"
S = "${WORKDIR}"

PACKAGE_ARCH = "${MACHINE_ARCH}"
INHIBIT_DEFAULT_DEPS = "1"

do_install() {
	     # Only install file if it has a contents
             install -d ${D}${sysconfdir}/formfactor/
             install -m 0644 ${S}/config ${D}${sysconfdir}/formfactor/
	     if [ -s "${S}/machconfig" ]; then
	             install -m 0644 ${S}/machconfig ${D}${sysconfdir}/formfactor/
	     fi
     }
