# gRPC definitions for CuraEngine
This repository contains the gRPC proto definitions for CuraEngine. These definitions are used to generate the gRPC code for the CuraEngine gRPC plugin system.

## Overview
As part of the [CuraEngine](https://github.com/Ultimaker/CuraEngine) plugin system, the CuraEngine serves as gRPC client. The functionality of CuraEngine can be extended with CuraEngine plugins, which behaves as servers. The gRPC client/server uses the [Protocol Buffers](https://developers.google.com/protocol-buffers) format. This repository contains the definitions for the gRPC server and client(s).

## Usage
The gRPC definitions are available for the following languages:

<details>
  <summary>Conan</summary>

  Usage in `conanfile.py`
  ```python
  class CuraEnginePluginConan(ConanFile):
      ...
  
      def requirements(self):
        self.requires("asio-grpc/2.4.0")
        self.requires("curaengine_grpc_definitions/(latest)@ultimaker/testing")
        ...
  
      def generate(self):
        tc = CMakeToolchain(self)
        cpp_info = self.dependencies["curaengine_grpc_definitions"].cpp_info
        tc.variables["GRPC_PROTOS"] = ";".join([str(p) for p in Path(cpp_info.resdirs[0]).glob("*.proto")])
        tc.generate()
  
      ...  
  ```
  
  
  Usage in `CMakeLists.txt`
  ```cmake
  ...
  find_package(asio-grpc REQUIRED)
  
  asio_grpc_protobuf_generate(
        GENERATE_GRPC GENERATE_MOCK_CODE
        OUT_VAR "ASIO_GRPC_PLUGIN_PROTO_SOURCES"
        OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated"
        PROTOS "${GRPC_PROTOS}"
  
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
  
  See: https://github.com/Ultimaker/Cura/wiki/Running-Cura-from-Source#1-configure-conan how to configure Conan
  
  ```bash
  conan install . --build=missing --update
  ```
</details>

<details>
  <summary>Python</summary>

 ```bash
 pip install git+https://github.com/Ultimaker/CuraEngine_grpc_defintions.git  
 ```

```python
import grpc

from CuraEngineGRPC.cura_pb2_grpc import CuraStub
import CuraEngineGRPC.cura_pb2 as cura_pb

....
```
</details>

<details>
  <summary>Rust</summary>
  Required dependencies before the gRPC defintions can be used are: [`protoc`, `protobuf`](https://github.com/hyperium/tonic#dependencies).
  
  Then add the following package to your `Cargo.toml`:
  ```bash
  cargo add --git https://github.com/Ultimaker/curaengine_grpc_defintions.git
  ```
</details>

## License

This project is licensed under the [MIT license](LICENSE).
