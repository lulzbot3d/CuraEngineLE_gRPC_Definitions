cmake_minimum_required(VERSION 3.23)
project(curaengine_grpc_definitions)

find_package(Protobuf REQUIRED)
find_package(asio-grpc REQUIRED)


asio_grpc_protobuf_generate(PROTOS "${GRPC_PROTOS}"
        IMPORT_DIRS "${CMAKE_CURRENT_SOURCE_DIR}/"
        OUT_VAR "ASIO_GRPC_PLUGIN_PROTO_SOURCES"
        OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated"
        GENERATE_GRPC GENERATE_MOCK_CODE)

add_library(curaengine_grpc_definitions ${ASIO_GRPC_PLUGIN_PROTO_SOURCES})
target_include_directories(curaengine_grpc_definitions PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/generated)
target_link_libraries(curaengine_grpc_definitions PUBLIC asio-grpc::asio-grpc protobuf::libprotobuf)