#  Copyright (c) 2024 UltiMaker
#  curaengine_grpc_definitions is released under the terms of the MIT

import os
from pathlib import Path

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.env import VirtualBuildEnv
from conan.tools.files import copy, update_conandata
from conan.tools.microsoft import check_min_vs, is_msvc_static_runtime, is_msvc
from conan.tools.scm import Version, Git

required_conan_version = ">=1.58.0"


class CuraEngine_gRPC_DefinitionsConan(ConanFile):
    name = "curaengine_grpc_definitions"
    license = "MIT"
    author = "UltiMaker"
    url = "https://github.com/Ultimaker/curaengine_grpc_definitions"
    description = "The gRPC definitions for CuraEngine plugins."
    topics = ("cura", "protobuf", "gcode", "grpc", "curaengine", "plugin", "3D-printing")
    exports = "LICENSE*"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True
    package_type = "library"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }

    def set_version(self):
        if not self.version:
            self.version = self.conan_data["version"]

    def export(self):
        git = Git(self)
        update_conandata(self, {"version": self.version, "commit": git.get_commit()})

    @property
    def _min_cppstd(self):
        return 20

    @property
    def _compilers_minimum_version(self):
        return {
            "gcc": "11",
            "clang": "14",
            "apple-clang": "13",
            "msvc": "192",
            "visual_studio": "17",
        }

    def export_sources(self):
        copy(self, "CMakeLists.txt", self.recipe_folder, self.export_sources_folder)
        copy(self, "*.proto", self.recipe_folder, self.export_sources_folder)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        self.options["boost"].header_only = True

        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.options["grpc"].csharp_plugin = False
        self.options["grpc"].node_plugin = False
        self.options["grpc"].objective_c_plugin = False
        self.options["grpc"].php_plugin = False
        self.options["grpc"].python_plugin = False
        self.options["grpc"].ruby_plugin = False
        self.options["asio-grpc"].local_allocator = "recycling_allocator"

    def layout(self):
        cmake_layout(self)
        gen = self.conf.get("tools.cmake.cmaketoolchain:generator")
        if gen:
            multi = "Visual" in gen or "Xcode" in gen or "Multi-Config" in gen
        else:
            compiler = self.settings.get_safe("compiler")
            if compiler in ("Visual Studio", "msvc"):
                multi = True
            else:
                multi = False
        build_type = str(self.settings.build_type)
        if multi:
            self.cpp.build.includedirs = ["{}/generated".format(build_type)]
        else:
            self.cpp.build.includedirs = ["./generated"]

    def requirements(self):
        self.requires("protobuf/3.21.12", transitive_headers = True)
        self.requires("boost/1.83.0")
        self.requires("asio-grpc/2.9.2")
        self.requires("grpc/1.54.3", transitive_headers = True)
        self.requires("openssl/3.2.1")

    def validate(self):
        # validate the minimum cpp standard supported. For C++ projects only
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, self._min_cppstd)
        check_min_vs(self, 191)
        if not is_msvc(self):
            minimum_version = self._compilers_minimum_version.get(str(self.settings.compiler), False)
            if minimum_version and Version(self.settings.compiler.version) < minimum_version:
                raise ConanInvalidConfiguration(
                    f"{self.ref} requires C++{self._min_cppstd}, which your compiler does not support."
                )
        if is_msvc(self) and self.options.shared:
            raise ConanInvalidConfiguration(f"{self.ref} can not be built as shared on Visual Studio and msvc.")

    def build_requirements(self):
        self.tool_requires("protobuf/3.21.9")

    def generate(self):
        tc = CMakeToolchain(self)
        if is_msvc(self):
            tc.variables["USE_MSVC_RUNTIME_LIBRARY_DLL"] = not is_msvc_static_runtime(self)
        tc.cache_variables["CMAKE_POLICY_DEFAULT_CMP0077"] = "NEW"
        tc.variables["GRPC_PROTOS"] = ";".join([str(p).replace("\\", "/") for p in Path(self.source_path).rglob("*.proto")])
        tc.generate()

        tc = CMakeDeps(self)
        tc.generate()

        tc = VirtualBuildEnv(self)
        tc.generate(scope="build")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self,
             pattern = "*.dll",
             dst = os.path.join(self.package_folder, "bin"),
             src = os.path.join(self.build_folder),
             keep_path=False)
        copy(self,
             pattern = "*.so*",
             dst = os.path.join(self.package_folder, "lib"),
             src = os.path.join(self.build_folder),
             keep_path=False)
        copy(self,
             pattern = "*.lib",
             dst = os.path.join(self.package_folder, "lib"),
             src = os.path.join(self.build_folder),
             keep_path=False)
        copy(self,
             pattern = "*.a",
             dst = os.path.join(self.package_folder, "lib"),
             src = os.path.join(self.build_folder),
             keep_path=False)

        copy(self,
             pattern = "*.h",
             dst = os.path.join(self.package_folder, "include"),
             src = os.path.join(self.build_folder, "generated"))
        copy(self,
             pattern = "LICENSE*",
             dst = os.path.join(self.package_folder, "license"),
             src = self.source_folder)
        copy(
            self,
            pattern = "*.proto",
            dst = os.path.join(self.package_folder, "res"),
            src = self.source_folder)

    def package_info(self):
        self.cpp_info.libs = ["curaengine_grpc_definitions"]
