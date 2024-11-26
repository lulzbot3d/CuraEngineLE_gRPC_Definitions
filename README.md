# gRPC Definitions for CuraEngineLE

[![Conan Package](https://img.shields.io/github/actions/workflow/status/lulzbot3d/CuraEngineLE_grpc_definitions/conan-package.yml?style=for-the-badge&logoColor=white&logo=conan)](https://github.com/lulzbot3d/CuraEngineLE_grpc_definitions/actions/workflows/conan-package.yml)
[![License](https://img.shields.io/badge/License-MIT-750014.svg?style=for-the-badge&logoColor=white&logo=opensourceinitiative)](LICENSE)

This repository contains the gRPC proto definitions for CuraEngineLE. These definitions are used to generate the gRPC code for the CuraEngineLE gRPC plugin system.

## Overview

As part of the [CuraEngineLE](https://github.com/lulzbot3d/CuraEngineLE) plugin system, the CuraEngineLE serves as gRPC client. The functionality of CuraEngineLE can be extended with CuraEngine plugins, which behaves as servers. The gRPC client/server uses the [Protocol Buffers](https://developers.google.com/protocol-buffers) format. This repository contains the definitions for the gRPC server and client(s).

## Usage

The gRPC definitions are available for the following languages:

### Conan

Usage in `conanfile.py`

```python
class CuraEngineLEPluginConan(ConanFile):
  ...

  def requirements(self):
    self.requires("asio-grpc/2.4.0")
    self.requires("curaenginele_grpc_definitions/(latest)@lulzbot/testing")
    ...

  def generate(self):
    tc = CMakeToolchain(self)
    cpp_info = self.dependencies["curaenginele_grpc_definitions"].cpp_info
    tc.variables["GRPC_IMPORT_DIRS"] = cpp_info.resdirs[0]
    tc.variables["GRPC_PROTOS"] = ";".join([str(p).replace("\\", "/") for p in Path(cpp_info.resdirs[0]).rglob("*.proto")])
    tc.generate()
    ...
```

Usage in `CMakeLists.txt`

```cmake
...
find_package(asio-grpc REQUIRED)

asio_grpc_protobuf_generate(PROTOS "${GRPC_PROTOS}"
  IMPORT_DIRS ${GRPC_IMPORT_DIRS}
  OUT_VAR "ASIO_GRPC_PLUGIN_PROTO_SOURCES"
  OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated"
  GENERATE_GRPC GENERATE_MOCK_CODE)

add_executable(engine_plugin_target_name ${PROTO_SRCS} ${ASIO_GRPC_PLUGIN_PROTO_SOURCES} main.cpp ...)

target_include_directories(engine_plugin_target_name
  PUBLIC
  ...
  PRIVATE
  ${CMAKE_CURRENT_BINARY_DIR}/generated
  )

target_link_libraries(simplify_boost_plugin PUBLIC asio-grpc::asio-grpc ...)
...
```

```bash
conan install . --build=missing --update
```

### Python

 ```bash
 pip install git+https://github.com/lulzbot3d/CuraEngineLE_grpc_definitions.git
 ```

```python
import grpc

from CuraEngineGRPC.cura_pb2_grpc import CuraStub
import CuraEngineGRPC.cura_pb2 as cura_pb

....
```

### Rust

Required dependencies before the gRPC definitions can be used are: [`protoc`, `protobuf`](https://github.com/hyperium/tonic#dependencies).

Then add the following package to your `Cargo.toml`:

```bash
cargo add --git https://github.com/lulzbot3d/CuraEngineLE_grpc_definitions.git
```
