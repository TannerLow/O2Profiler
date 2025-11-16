# O2Profiler
A simplistic profiler for c++. See Tester for basic examples.

## Versions
* 0.1.0 (latest)

## Conan Integration
Gitlab artifact link: https://gitlab.com/the-barrio/el-pino/-/packages/49138639

```
# install conan (recommend doing this in a venv)
pip install -r requirements.txt

# add my gitlab remote where my packages are stored
conan remote add <unique_remote_name> https://gitlab.com/api/v4/projects/76111843/packages/conan
```

---

* Create a `conanfile.txt` file with these contents in the same location as your .sln file
```
[requires]
o2profiler/0.1.0

[generators]
MSBuildDeps
MSBuildToolchain
```

---

* Run these commands to install the packages listed in the `conanfile.txt`
```
conan install . --output-folder=build -s build_type=Debug   -s arch=x86_64 -s compiler.cppstd=17

conan install . --output-folder=build -s build_type=Release -s arch=x86_64 -s compiler.cppstd=17
```

---

* Create a `Directory.Build.props` file with these contents in the same location as your .sln
```
<Project>
  <PropertyGroup>
    <ConanBuildFolder>$(MSBuildThisFileDirectory)build</ConanBuildFolder>
  </PropertyGroup>

  <Import Project="$(ConanBuildFolder)\conantoolchain.props"
          Condition="Exists('$(ConanBuildFolder)\conantoolchain.props')" />

  <Import Project="$(ConanBuildFolder)\conandeps.props"
          Condition="Exists('$(ConanBuildFolder)\conandeps.props')" />

</Project>
```

## For Maintainer Use Only
Command to upload new versions to package repository
```
conan upload o2profiler/x.y.z -r gitlab -c
```
