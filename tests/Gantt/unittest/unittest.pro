TARGET = TestUnittests

include( $${TOP_SOURCE_DIR}/examples/examples.pri )

DEPENDPATH += . $${TOP_SOURCE_DIR}/include
INCLUDEPATH += . $${TOP_SOURCE_DIR}/include
CONFIG += console
QT += svg
macx:CONFIG -= app_bundle
static { macx:QMAKE_LFLAGS += -Wl,-rpath,$$[QT_INSTALL_LIBS] }

# Input
SOURCES += main.cpp
