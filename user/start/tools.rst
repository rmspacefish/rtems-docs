.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber
.. Copyright (C) 2020 Chris Johns
.. Copyright (C) 2020 Utkarsh Rai

.. _QuickStartTools:

Install the Tool Suite
======================

You have chosen an installation prefix, the BSP to build, the tool's
architecure and prepared the source for the RSB in the previous sections.  We
have chosen :file:`$HOME/quick-start/rtems/$RTEMS_VERSION` as the installation prefix, the
``erc32`` BSP and the SPARC architecture name of ``sparc-rtems5`` (``sparc-rtems6`` for the git clone), 
and unpacked the RSB source in :file:`$HOME/quick-start/src`.

The tool suite for RTEMS and the RTEMS sources are tightly coupled.  For
example, do not use a RTEMS version 5 tool suite with RTEMS version 4.11
sources and vice versa.

The available build sets can be displayed with:

.. code-block:: none
    
    cd $HOME/quick-start/src/rsb/rtems
    ../source-builder/sb-set-builder --list-bsets
	
Build and install the tool suite for the SPARC architecture and RTEMS version:

.. code-block:: none

    cd $HOME/quick-start/src/rsb/rtems
    ../source-builder/sb-set-builder --prefix=$HOME/quick-start/rtems/$RTEMS_VERSION $RTEMS_VERSION/rtems-sparc

This command should output something like this (omitted lines are denoted by
...). The build host appears as part of the name of the package being
built. The name you see may vary depending on the host you are using:

.. code-block:: none

    RTEMS Source Builder - Set Builder, 5.1.0
    Build Set: 5/rtems-sparc
    ...
    config: tools/rtems-binutils-2.34.cfg
    package: sparc-rtems5-binutils-2.34-x86_64-freebsd12.1-1
    building: sparc-rtems5-binutils-2.34-x86_64-freebsd12.1-1
    sizes: sparc-rtems5-binutils-2.34-x86_64-freebsd12.1-1: 305.866MB (installed: 29.966MB)
    cleaning: sparc-rtems5-binutils-2.34-x86_64-freebsd12.1-1
    reporting: tools/rtems-binutils-2.34.cfg -> sparc-rtems5-binutils-2.34-x86_64-freebsd12.1-1.txt
    reporting: tools/rtems-binutils-2.34.cfg -> sparc-rtems5-binutils-2.34-x86_64-freebsd12.1-1.xml
    config: tools/rtems-gcc-7.5.0-newlib-fbaa096.cfg
    package: sparc-rtems5-gcc-7.5.0-newlib-fbaa096-x86_64-freebsd12.1-1
    building: sparc-rtems5-gcc-7.5.0-newlib-fbaa096-x86_64-freebsd12.1-1
    ....
    Build Sizes: usage: 5.684GB total: 1.112GB (sources: 143.803MB, patches: 21.348KB, installed 995.188MB)
    Build Set: Time 0:21:35.626294

Once the build has successfully completed you can check if the cross C compiler
works with the following command (replace 5 with 6 for RTEMS 6):

.. code-block:: none

    $HOME/quick-start/rtems/5/bin/sparc-rtems5-gcc --version

This command should output something like below.  The version informtion helps
you to identify the exact sources used to build the cross compiler of your
RTEMS tool suite.  In the output you see the version of RTEMS or the hash from
the RSB repository if you are building using a Git repository clone. The Newlib
hash is the version of Newlib in the RTEMS's github
`sourceware-mirror-newlib-cygwin
<https://github.com/RTEMS/sourceware-mirror-newlib-cygwin>`_ repository. The
``sources`` and ``patches`` directories created by the RSB contain all the
source code used.

.. code-block:: none

    sparc-rtems5-gcc (GCC) 7.5.0 20191114 (RTEMS 5, RSB 5.1.0, Newlib fbaa096)
    Copyright (C) 2017 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.



Add ``--verbose`` to the GCC command for the the verbose version details.

Need for RTEMS-Specific Cross-Compiler
---------------------------------------------------------

New users are often confused as to why they cannot use their distribution's
cross-compiler for their target on RTEMS, e.g., the riscv64-linux-gnu or the
arm-none-eabi-gcc. Below mentioned are some of the reasons for using
the RTEMS cross-compiler.

 Correct configuration of Newlib
     Newlib is a C standard library implementation intended for use on embedded
     systems. Most of the POSIX and libc support for RTEMS is derived from
     Newlib. The RTEMS cross-compiler configures Newlib correctly for RTEMS.

 Threading in GCC support libraries
     Several threading packages in GCC such as Go threads (libgo), OpenMP
     (libgomp), and OpenACC need to be customized according to RTEMS. This is
     done by the RTEMS specific cross-compiler.

 Provide preprocessor define __rtems__
     The  ``__rtems__``  preprocessor define is used to provide conditional code
     compilation in source files that are shared with other projects e.g. in
     Newlib or imported code from FreeBSD.

 Multilib variants to match the BSP
     RTEMS configures GCC to create separate runtime libraries for each
     supported instruction set, floating point unit, vector unit, word size
     (e.g. 32-bit and 64-bit), endianness, ABI, processor errata workarounds,
     and so on in the architecture. These libraries are termed as :ref:`Multilib
     <TargetArchitectures>` variants. Multilib variants to match the BSP are set
     by selecting a specific set of machine options using the RTEMS
     cross-compiler.
