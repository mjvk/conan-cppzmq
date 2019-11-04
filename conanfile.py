import os
from conans import ConanFile, CMake, tools


class CppZmqConan(ConanFile):
    name = "cppzmq"
    version = "4.5.0"
    url = "https://github.com/bincrafters/conan-cppzmq"
    homepage = "https://github.com/zeromq/cppzmq"
    description = "C++ binding for 0MQ"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    topics = ("conan", "cppzmq", "zmq-cpp", "zmq", "cpp-bind")
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True
    requires = "zmq/4.3.2@bincrafters/stable"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        sha256 = "64eb4e58eaf0c77505391c6c9a606cffcb57c6086f3431567a1ef4a25b01fa36"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = CMake(self)
        cmake.definitions["CPPZMQ_BUILD_TESTS"] = False
        cmake.configure()
        cmake.install()

    def package_id(self):
        self.info.header_only()
