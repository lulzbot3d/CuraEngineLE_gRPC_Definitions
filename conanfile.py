#  Copyright (c) 2023 UltiMaker
#  curaengine_grpc_definitions is released under the terms of the MIT

import os

from conan import ConanFile
from conan.tools.files import copy

required_conan_version = ">=1.56.0"


class CuraEngine_gRPC_DefinitionsConan(ConanFile):
    name = "curaengine_grpc_definitions"
    license = "MIT"
    author = "UltiMaker"
    url = "https://github.com/Ultimaker/curaengine_grpc_definitions"
    description = ""
    topics = ("cura", "protobuf", "gcode", "grpc", "curaengine", "plugin", "3D-printing")
    exports = "LICENSE*"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True

    def export_sources(self):
        copy(self, "*.proto", self.recipe_folder, self.export_sources_folder)

    def package(self):
        copy(self,
             pattern = "LICENSE*",
             dst = os.path.join(self.package_folder, "license"),
             src = self.source_folder)
        copy(
            self,
            pattern = "*.proto",
            dst = os.path.join(self.package_folder, "res"),
            src = self.source_folder)

    def package_id(self):
        self.info.clear()
