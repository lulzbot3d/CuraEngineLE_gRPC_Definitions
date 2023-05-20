import os
from pathlib import Path
import subprocess
from setuptools import setup, find_packages, find_namespace_packages
from setuptools.command.install import install
from setuptools.command.build_py import build_py

if not os.path.exists("autogen"):
    os.mkdir("autogen")

out_dir = "CuraEngine_gRPC"
full_out_dir = os.path.join("autogen", out_dir)
if not os.path.exists(full_out_dir):
    os.mkdir(full_out_dir)

class CustomBuildCommand(build_py):
    def run(self):
        # Generate .py and .pyi files from protobuf files
        self.generate_proto_sources()
        # Run the default installation process
        build_py.run(self)

    def generate_proto_sources(self):
        protoc_command = ["python", "-m", "grpc_tools.protoc"]
        proto_include_dirs = ["."]
        proto_sources = ["**/*.proto"]

        with open(os.path.join(full_out_dir, "__init__.py"), 'w') as fp:
            pass

        for rglob in proto_sources:
            for proto_file in Path().rglob(rglob):
                protoc_args = protoc_command + [
                    f"--proto_path={dir}"
                    for dir in proto_include_dirs
                ] + [
                    f"--python_out={full_out_dir}",
                    f"--grpc_python_out={full_out_dir}",
                    f"--mypy_out={full_out_dir}",
                    proto_file,
                ]
                subprocess.Popen(protoc_args)
                # subprocess.check_call(protoc_args)

setup(
    name="CuraEngine_gRPC",
    version="0.1.0",
    description="A gRPC package using proto files with type hints",
    author="UltiMaker",
    author_email="cura@ultimaker.com",
    packages=["CuraEngine_gRPC"],
    package_dir = {'': 'autogen'},
    install_requires=["grpcio-tools"],
    cmdclass={
        "build_py": CustomBuildCommand,
    },
)
