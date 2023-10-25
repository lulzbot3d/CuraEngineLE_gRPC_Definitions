from pathlib import Path
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py

out_dir = "CuraEngineGRPC"
full_out_dir = Path("autogen", out_dir)
full_out_dir.mkdir(parents = True, exist_ok = True)

# FIXME: Make this less hacky and working
# for now you can copy the CuraEngineGRPC from the autogen folder in the site-packages and it should work

class CustomBuildCommand(build_py):

    def run(self):
        self.generate_proto_sources()
        self.add_init_files()
        self.fix_imports()
        build_py.run(self)

    def add_init_files(self):
        py_files = list(Path(full_out_dir).rglob("**/*.py"))
        module_dirs = list(set([p.parent for p in py_files]))
        for mod_dir in module_dirs:
            parent_dir = mod_dir
            while parent_dir != full_out_dir:
                init_file = parent_dir.joinpath('__init__.py')
                if not init_file.exists():
                    with open(init_file, "w"):
                        pass
                parent_dir = parent_dir.parent

    def fix_imports(self):
        py_files = list(Path(full_out_dir).rglob("**/*.py*"))
        for py_file in py_files:
            content = ""
            with open(py_file, "r") as f:
                content = f.read().replace("from cura.plugins.", "from CuraEngineGRPC.cura.plugins.").replace("import CuraEngineGRPC.cura.plugins.", "import CuraEngineGRPC.cura.plugins.")
            with open(py_file, "w") as f:
                f.write(content)

    def generate_proto_sources(self):
        protoc_command = ["python", "-m", "grpc_tools.protoc"]
        proto_glob = "**/*.proto"
        proto_files = list(Path("./cura").rglob(proto_glob))
        proto_include_dirs = ["."] + list(set([p.parent for p in proto_files]))

        for proto_file in proto_files:
            sub_out_dir = full_out_dir.joinpath(proto_file.relative_to(".").parent)
            sub_out_dir.mkdir(parents = True, exist_ok = True)
            protoc_args = protoc_command + [
                f"--proto_path={dir}"
                for dir in proto_include_dirs
            ] + [
                              f"--python_out={full_out_dir}",
                              f"--grpc_python_out={full_out_dir}",
                              f"--mypy_out={full_out_dir}",
                              str(Path(proto_file)),
                          ]
            subprocess.run(protoc_args)


setup(
    name = "CuraEngineGRPC",
    version = "0.2.0-alpha",
    description = "A gRPC package using proto files with type hints",
    author = "UltiMaker",
    author_email = "cura@ultimaker.com",
    packages = ["CuraEngineGRPC"],
    package_dir = {'': 'autogen'},
    package_data = {"CuraEngineGRPC": ["*.pyi"]},
    install_requires = ["grpcio-tools"],
    cmdclass = {
        "build_py": CustomBuildCommand,
    },
)
