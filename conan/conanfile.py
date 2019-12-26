#############################################################################
## Copyright (C) 2010-2019 Klaralvdalens Datakonsult AB, a KDAB Group company, info@kdab.com.
## All rights reserved.
##
## This file is part of the KD Chart library.
##
## Licensees holding valid commercial KD Soap licenses may use this file in
## accordance with the KD Soap Commercial License Agreement provided with
## the Software.
##
##
## This file may be distributed and/or modified under the terms of the
## GNU Lesser General Public License version 2.1 and version 3 as published by the
## Free Software Foundation and appearing in the file LICENSE.LGPL.txt included.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
## Contact info@kdab.com if any conditions of this licensing are not
## clear to you.
##
######################################################################/

from conans import ConanFile, CMake, tools

class KdchartConan(ConanFile):
    name = "KDChart"
    version = "2.6.50"
    license = ("https://raw.githubusercontent.com/KDAB/KDChart/master/LICENSE.txt,"
               "https://raw.githubusercontent.com/KDAB/KDChart/master/LICENSE.GPL.txt")
    author = "Klaralvdalens Datakonsult AB (KDAB) info@kdab.com"
    url = "https://github.com/KDAB/KDChart.git"
    description = "KD Chart is a tool for creating business and scientific charts."
    generators = "cmake"

    def requirements(self):
        # Kdab uses a custom qt build
        # To build qt with with extra modules enabled use qt package from:
        #   https://github.com/bincrafters/conan-qt
        # Build the command:
        #   conan create -ks -o qt:qtsvg=True -o qt:qtdeclarative=True -o qt:qtremoteobjects=True -o qt:qtscxml=True . 5.13.2@kdab/stable
        self.requires("qt/5.13.2@kdab/stable")

    def source(self):
        git = tools.Git(folder="")
        git.clone(self.url)
        #We want cmake support, so use master for now
        #git.checkout("kdchart-%s-release"%self.version)

    def configure(self):
        # Use kdab flags to match qt package hash
        # ~$ conan create -ks -o qt:qttools=True -o qt:qtsvg=True -o qt:qtdeclarative=True -o qt:qtremoteobjects=True -o qt:qtscxml=True . 5.13.2@kdab/stable
        self.options["qt"].qtsvg = True
        self.options["qt"].qtdeclarative = True
        self.options["qt"].qtremoteobjects = True
        self.options["qt"].qtscxml = True
        self.options["qt"].qttools = True

    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure()
        self.cmake.build()

    def package(self):
        self.cmake.install()

    def package_info(self):
        self.env_info.CMAKE_PREFIX_PATH.append(self.package_folder)