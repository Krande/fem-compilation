argv = ['./waf.engine', '--use-config=wafcfg_conda',
        '--use-config-dir=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/config',
        '--prefix=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho',
        '--pythondir=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/aster',
        '--embed-metis', '--with-data=data', '--without-hg', 'configure', '--out=build/std', '--jobs=4']
config_cmd = 'configure'
environ = {
    'DEBUG_FFLAGS': '-march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-all -fno-plt -Og -g -Wall -Wextra -fcheck=all -fbacktrace -fimplicit-none -fvar-tracking-assignments -ffunction-sections -pipe',
    'GCC_RANLIB': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-ranlib',
    'INCLUDES_METIS': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/metis-aster/include',
    'CONDA_EXE': '/home/kristoffer/mambaforge/envs/conda-build/bin/conda', '_CE_M': '',
    'PKG_BUILD_STRING': 'h24ae451_0',
    'PKG_CONFIG_PATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/pkgconfig',
    'build_alias': 'x86_64-conda-linux-gnu', 'PYTHONNOUSERSITE': '1', 'WAFLOCK': '.lock-std_build',
    'CMAKE_ARGS': '-DCMAKE_AR=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ar -DCMAKE_CXX_COMPILER_AR=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-ar -DCMAKE_C_COMPILER_AR=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-ar -DCMAKE_RANLIB=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ranlib -DCMAKE_CXX_COMPILER_RANLIB=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-ranlib -DCMAKE_C_COMPILER_RANLIB=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-ranlib -DCMAKE_LINKER=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ld -DCMAKE_STRIP=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-strip -DCMAKE_BUILD_TYPE=Release -DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER -DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY -DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY -DCMAKE_FIND_ROOT_PATH=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho;/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/x86_64-conda-linux-gnu/sysroot -DCMAKE_INSTALL_PREFIX=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_PROGRAM_PATH=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin;/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/bin',
    'CONDA_LIBRARY_PATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/lib',
    'PREFIX': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho',
    'MAKE_TERMOUT': '1',
    'GPROF': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gprof',
    'CONDA_TOOLCHAIN_BUILD': 'x86_64-conda-linux-gnu',
    '_CONDA_PYTHON_SYSCONFIGDATA_NAME': '_sysconfigdata_x86_64_conda_cos6_linux_gnu', 'CONDA_PERL': '5.26',
    'STDLIB_DIR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/python3.10',
    'STRINGS': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-strings',
    'CPP': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-cpp',
    'CONDA_NPY': '122', 'SHLIB_EXT': '.so', 'PY3K': '1', 'CPU_COUNT': '16',
    'CONDA_BACKUP_BUILD': 'x86_64-conda_cos6-linux-gnu', 'DIRTY': '', 'CONDA_PY': '310', 'build_platform': 'linux-64',
    'XML_CATALOG_FILES': 'file:///home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/etc/xml/catalog file:///etc/xml/catalog file:///home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/etc/xml/catalog file:///etc/xml/catalog',
    'FFLAGS': '-march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix',
    'PKG_NAME': 'code-aster',
    'PWD': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work',
    'GSETTINGS_SCHEMA_DIR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/share/glib-2.0/schemas',
    'CONDA_PREFIX': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env',
    'PIP_NO_BUILD_ISOLATION': 'False', 'PIP_NO_INDEX': 'True',
    'GSETTINGS_SCHEMA_DIR_CONDA_BACKUP': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/share/glib-2.0/schemas',
    'CXX': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-c++',
    'CXXFLAGS': '-fvisibility-inlines-hidden -fmessage-length=0 -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix -fdiagnostics-color=always',
    'PKG_BUILDNUM': '0', 'LUA_VER': '5', 'CONDA_TOOLCHAIN_HOST': 'x86_64-conda-linux-gnu',
    'DEBUG_CXXFLAGS': '-fvisibility-inlines-hidden -fmessage-length=0 -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-all -fno-plt -Og -g -Wall -Wextra -fvar-tracking-assignments -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix',
    'R_VER': '3.5',
    'LDFLAGS': '-Wl,-O2 -Wl,--sort-common -Wl,--as-needed -Wl,-z,relro -Wl,-z,now -Wl,--disable-new-dtags -Wl,--gc-sections -Wl,--allow-shlib-undefined -Wl,-rpath,/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib -Wl,-rpath-link,/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib -L/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib',
    'HOME': '/home/kristoffer',
    'CONDA_INCLUDE_PATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/include',
    'LANG': 'en_US.UTF-8',
    'MESON_ARGS': '--buildtype release --prefix=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho -Dlibdir=lib',
    'DEBUG_CFLAGS': '-march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-all -fno-plt -Og -g -Wall -Wextra -fvar-tracking-assignments -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix',
    'SP_DIR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/python3.10/site-packages',
    'LIBPATH_METIS': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/metis-aster/lib',
    'CONDA_BUILD': '1',
    'CXX_FOR_BUILD': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-c++',
    'CONDA_BACKUP_CFLAGS': '-fdiagnostics-color=always', 'PIP_NO_DEPENDENCIES': 'True',
    'ELFEDIT': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-elfedit',
    'CONDA_PROMPT_MODIFIER': '(/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env) ',
    'CMAKE_PREFIX_PATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho:/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/x86_64-conda-linux-gnu/sysroot/usr',
    'CPPFLAGS': '-DNDEBUG -D_FORTIFY_SOURCE=2 -O2 -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include',
    'target_platform': 'linux-64',
    'LD': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ld',
    'PKG_HASH': 'h24ae451', 'CLICOLOR_FORCE': '1', 'CONDA_LUA': '5',
    'PIP_CACHE_DIR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/pip_cache',
    'READELF': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-readelf',
    'GXX': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-g++',
    'CONDA_STACKED_3': 'true',
    'FC_FOR_BUILD': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gfortran',
    'RECIPE_DIR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster', 'AM_COLOR_TESTS': 'always',
    'GCC_AR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-ar',
    'ADDR2LINE': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-addr2line',
    'CONDA_BACKUP_CXXFLAGS': '-fdiagnostics-color=always', '_CE_CONDA': '',
    'GCC_NM': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc-nm',
    'SIZE': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-size',
    'F77': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gfortran',
    'HOST': 'x86_64-conda-linux-gnu', 'WAF_SUFFIX': 'std',
    'CC_FOR_BUILD': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-cc',
    'SUBDIR': 'linux-64', 'CONDA_SHLVL': '3', 'PERL_VER': '5.26', 'PIP_IGNORE_INSTALLED': 'True',
    'AR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ar',
    'AS': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-as',
    'ARCH': '64',
    'DEBUG_CPPFLAGS': '-D_DEBUG -D_FORTIFY_SOURCE=2 -Og -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include',
    'ROOT': '/home/kristoffer/mambaforge/envs/conda-build',
    'F95': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-f95',
    'F90': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gfortran',
    'host_alias': 'x86_64-conda-linux-gnu',
    'LIBPATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib ',
    'CMAKE_COLOR_MAKEFILE': 'ON', 'SHLVL': '3',
    'NM': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-nm',
    'LD_RUN_PATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib',
    'SYS_PYTHON': '/home/kristoffer/mambaforge/envs/conda-build/bin/python3.11',
    'GCC': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gcc',
    'DEBUG_FORTRANFLAGS': '-march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-all -fno-plt -Og -g -Wall -Wextra -fcheck=all -fbacktrace -fimplicit-none -fvar-tracking-assignments -ffunction-sections -pipe',
    'HTTPS_PROXY': '', 'HTTP_PROXY': '',
    'FORTRANFLAGS': '-march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix',
    'CONDA_R': '3.5', 'CONDA_BUILD_STATE': 'BUILD',
    'INCLUDES': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include ',
    'SRC_DIR': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work',
    'LD_GOLD': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ld.gold',
    'CONDA_PYTHON_EXE': '/home/kristoffer/mambaforge/envs/conda-build/bin/python',
    'TFELHOME': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho',
    'BUILD_PREFIX': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env',
    'NPY_DISTUTILS_APPEND_FLAGS': '1',
    'GFORTRAN': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gfortran',
    'SYS_PREFIX': '/home/kristoffer/mambaforge/envs/conda-build',
    'CONDA_DEFAULT_ENV': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env',
    'OBJCOPY': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-objcopy',
    'PKG_VERSION': '15.8.0', 'REQUESTS_CA_BUNDLE': '',
    'FC': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-gfortran',
    'PY_VER': '3.10',
    'STRIP': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-strip',
    'OBJDUMP': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-objdump',
    'PATH': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin:/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/bin:/home/kristoffer/mambaforge/envs/conda-build/condabin:/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env:/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin:/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho:/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/bin:/home/kristoffer/mambaforge/envs/conda-build/bin:/home/kristoffer/mambaforge/condabin:/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/kristoffer/.local/share/JetBrains/Toolbox/scripts',
    'CC': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-cc',
    'CFLAGS': '-march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/include -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work=/usr/local/src/conda/code-aster-15.8.0 -fdebug-prefix-map=/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho=/usr/local/src/conda-prefix -fdiagnostics-color=always',
    'CXXFILT': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-c++filt',
    'BUILD': 'x86_64-conda-linux-gnu', 'CONDA_PREFIX_1': '/home/kristoffer/mambaforge/envs/conda-build',
    'CONDA_PREFIX_2': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho',
    'CMAKE_GENERATOR': 'Unix Makefiles',
    'RANLIB': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/bin/x86_64-conda-linux-gnu-ranlib',
    'CONDA_BUILD_SYSROOT': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_build_env/x86_64-conda-linux-gnu/sysroot',
    'NPY_VER': '1.22', '_': './waf.engine', 'TERM': 'vt100'}
files = [
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/bibfor/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/code_aster/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/run_aster/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/bibcxx/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/bibc/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/mfront/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/i18n/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/data/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/doc/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/astest/wscript',
    '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/wscript']
hash = b'\r\xea\xdb \xed\x01\xcf&\xe87 G\x9d\x8e\xe6X'
launch_dir = '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work'
options = {'colors': 'yes', 'jobs': 4, 'keep': 0, 'verbose': 0, 'zones': '', 'profile': 0, 'pdb': 0, 'whelp': 0,
           'out': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/build/std',
           'top': '', 'no_lock_in_run': '', 'no_lock_in_out': '', 'no_lock_in_top': '',
           'prefix': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho',
           'bindir': None, 'libdir': None, 'progress_bar': 0, 'targets': '', 'files': '', 'destdir': '', 'force': False,
           'distcheck_args': None, 'download': False, 'use_config': 'wafcfg_conda',
           'use_config_dir': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/config', 'EXEC_PREFIX': '',
           'BINDIR': '', 'SBINDIR': '', 'LIBEXECDIR': '', 'SYSCONFDIR': '', 'SHAREDSTATEDIR': '', 'LOCALSTATEDIR': '',
           'LIBDIR': '', 'INCLUDEDIR': '', 'OLDINCLUDEDIR': '', 'DATAROOTDIR': '', 'DATADIR': '', 'INFODIR': '',
           'LOCALEDIR': '', 'MANDIR': '', 'DOCDIR': '', 'HTMLDIR': '', 'DVIDIR': '', 'PDFDIR': '', 'PSDIR': '',
           'custom_fc_sig': False, 'check_c_compiler': None, 'check_cxx_compiler': None, 'check_fortran_compiler': None,
           'parallel': None, 'openmp': None, 'pyc': 1, 'pyo': 1, 'nopycache': None, 'python': None,
           'pythondir': '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/aster',
           'pythonarchdir': None, 'maths_libs': None, 'embed_math': False, 'med_libs': 'med', 'embed_med': False,
           'enable_med': True, 'hdf5_libs': 'hdf5', 'embed_hdf5': None, 'enable_hdf5': True, 'enable_metis': True,
           'metis_libs': 'metis', 'embed_metis': True, 'enable_parmetis': None, 'parmetis_libs': None,
           'embed_parmetis': False, 'enable_mumps': True,
           'mumps_libs': 'dmumps zmumps smumps cmumps mumps_common pord mpiseq', 'embed_mumps': False,
           'enable_scotch': True, 'scotch_libs': 'esmumps scotch scotcherr', 'embed_scotch': False,
           'enable_petsc': None, 'petsc_libs': None, 'embed_petsc': False, 'enable_petsc4py': None, 'testname': None,
           'outputdir': None, 'exectool': None, 'time_limit': None, 'without_repo': True, 'boost_includes': '',
           'boost_libs': '', 'boost_mt': False, 'boost_abi': '', 'boost_linkage_autodetect': None, 'boost_toolset': '',
           'boost_python': '310', 'embed_aster': True, 'enable_mfront': True, 'enable_i18n': None, 'legacy': True,
           'singularityimage': None, 'with_data': 'data', 'with_prog_gmsh': None, 'with_prog_salome': None,
           'with_prog_run_miss3d': None, 'with_prog_homard': None, 'with_prog_ecrevisse': None,
           'with_prog_xmgrace': None, 'with_prog_gracebat': None, 'with_prog_mfront': None, 'with_prog_mdump': None,
           'with_py_med': None, 'with_py_medcoupling': None, 'with_py_mpi4py': None, 'enable_doc': None,
           'enable_pdf': None, 'with_validation': None, 'install_tests': False, 'embed_all': False, 'enable_all': None}
out_dir = '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work/build/std'
run_dir = '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work'
top_dir = '/home/kristoffer/code/condapackaging/src/code_aster/code_aster/temp/build/code-aster-0_1691482045132/work'
