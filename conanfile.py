from conan import ConanFile
from conan.tools.files import copy
from conan.tools.microsoft import MSBuild, vs_layout
import os

class O2ProfilerConan(ConanFile):
    # 1. BASIC INFO
    name = "o2profiler"
    version = "0.1.0"

    # 2. BUILD SETTINGS
    settings = "os", "compiler", "build_type", "arch"

    # 3. GENERATORS (for consumers)
    generators = "MSBuildDeps", "MSBuildToolchain"

    # 4. SOURCE CODE
    # This tells conan create to copy our project files
    # into its build environment.
    exports_sources = (
        "O2Profiler.sln",
        "O2Profiler/O2Profiler.vcxproj",
        "O2Profiler/include/*",
        "O2Profiler/src/*"
    )

    # 5. LAYOUT
    # This tells Conan to expect the Visual Studio layout
    # (e.g., .sln in root, .vcxproj in subfolder)
    def layout(self):
        vs_layout(self)

    # 6. BUILD METHOD
    # This tells Conan how to build your code
    def build(self):
        msbuild = MSBuild(self)
        # Build the .vcxproj file directly, not the .sln
        project_file = os.path.join(self.source_folder, "O2Profiler", "O2Profiler.vcxproj")
        msbuild.build(project_file)

    # 7. PACKAGE METHOD
    # This is the most important part.
    # It copies build files into the final package.
    def package(self):
        # --- THE HEADER FIX ---
        # Copy all .h files FROM the project subfolder...
        copy(
            self, "*",
            src=os.path.join(self.source_folder, "O2Profiler", "include"),
            # ...TO the "include" folder in the package
            dst=os.path.join(self.package_folder, "include")
        )

        # --- THE LIBRARY FILE ---
        # Copy the .lib file
        copy(
            self, "*.lib",
            src=self.build_folder,
            dst=os.path.join(self.package_folder, "lib"),
            keep_path=False
        )

    # 8. PACKAGE INFO (for consumers)
    # This tells consumers what to link against.
    def package_info(self):
        # Default to the release name
        lib_name = "O2Profiler"

        # If the consumer is in Debug, change the name
        if self.settings.build_type == "Debug":
            lib_name += "-d"

        # Tell the consumer to link that specific library
        self.cpp_info.libs = [lib_name]