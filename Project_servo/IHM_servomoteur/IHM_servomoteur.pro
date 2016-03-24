#-------------------------------------------------
#
# Project created by QtCreator 2016-03-04T10:34:07
#
#-------------------------------------------------

QT       += core gui
QT       += serialport

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = IHM_servomoteur
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    serial_config.cpp \
    protocole_serie.cpp

HEADERS  += mainwindow.h \
    serial_config.h \
    protocole_serie.h

FORMS    += mainwindow.ui \
    serial_config.ui

DISTFILES +=
