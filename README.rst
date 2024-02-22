===========
QEMU-PATCHED
===========

Intended use with Hyper-V.

.. code-block:: shellhttps://github.com/kila58/qemu-patched

  <domain type="kvm">
    <name>win11</name>
    <uuid>7abc4c7a-51db-4461-a38c-b15442e62e2a</uuid>
    <metadata>
      <libosinfo:libosinfo xmlns:libosinfo="http://libosinfo.org/xmlns/libvirt/domain/1.0">
        <libosinfo:os id="http://microsoft.com/win/11"/>
      </libosinfo:libosinfo>
    </metadata>
    <memory unit="KiB">23437312</memory>
    <currentMemory unit="KiB">23437312</currentMemory>
    <memoryBacking>
      <hugepages/>
    </memoryBacking>
    <vcpu placement="static">16</vcpu>
    <iothreads>1</iothreads>
    <cputune>
      <vcpupin vcpu="0" cpuset="0"/>
      <vcpupin vcpu="1" cpuset="10"/>
      <vcpupin vcpu="2" cpuset="1"/>
      <vcpupin vcpu="3" cpuset="11"/>
      <vcpupin vcpu="4" cpuset="2"/>
      <vcpupin vcpu="5" cpuset="12"/>
      <vcpupin vcpu="6" cpuset="3"/>
      <vcpupin vcpu="7" cpuset="13"/>
      <vcpupin vcpu="8" cpuset="4"/>
      <vcpupin vcpu="9" cpuset="14"/>
      <vcpupin vcpu="10" cpuset="5"/>
      <vcpupin vcpu="11" cpuset="15"/>
      <vcpupin vcpu="12" cpuset="6"/>
      <vcpupin vcpu="13" cpuset="16"/>
      <vcpupin vcpu="14" cpuset="7"/>
      <vcpupin vcpu="15" cpuset="17"/>
      <emulatorpin cpuset="8-9,18-19"/>
      <iothreadpin iothread="1" cpuset="8-9,18-19"/>
    </cputune>
    <sysinfo type="smbios">
      <bios>
        <entry name="vendor">TOSHIBA</entry>
        <entry name="version">2.90</entry>
      </bios>
    </sysinfo>
    <os firmware="efi">
      <type arch="x86_64" machine="pc-q35-8.1">hvm</type>
      <firmware>
        <feature enabled="yes" name="enrolled-keys"/>
        <feature enabled="yes" name="secure-boot"/>
      </firmware>
      <loader readonly="yes" secure="yes" type="pflash" format="qcow2">/usr/share/edk2/ovmf/OVMF_CODE_4M.secboot.qcow2</loader>
      <nvram template="/usr/share/edk2/ovmf/OVMF_VARS_4M.secboot.qcow2" format="qcow2">/var/lib/libvirt/qemu/nvram/win11_VARS.qcow2</nvram>
      <boot dev="hd"/>
      <smbios mode="sysinfo"/>
    </os>
    <features>
      <acpi/>
      <apic/>
      <hyperv mode="custom">
        <relaxed state="on"/>
        <vapic state="on"/>
        <spinlocks state="on" retries="8191"/>
        <vpindex state="on"/>
        <runtime state="on"/>
        <synic state="on"/>
        <stimer state="on"/>
        <reset state="on"/>
        <vendor_id state="on" value="GenuineIntel"/>
        <frequencies state="on"/>
      </hyperv>
      <kvm>
        <hidden state="on"/>
      </kvm>
      <vmport state="off"/>
      <smm state="on"/>
    </features>
    <cpu mode="custom" match="exact" check="none">
      <model fallback="allow">SandyBridge</model>
      <topology sockets="1" dies="1" cores="8" threads="2"/>
      <feature policy="disable" name="hypervisor"/>
      <feature policy="disable" name="aes"/>
      <feature policy="disable" name="x2apic"/>
      <feature policy="require" name="invtsc"/>
    </cpu>
    <clock offset="localtime">
      <timer name="rtc" tickpolicy="catchup"/>
      <timer name="pit" tickpolicy="discard"/>
      <timer name="hpet" present="yes"/>
      <timer name="hypervclock" present="yes"/>
      <timer name="tsc" present="yes" mode="native"/>
    </clock>
    <on_poweroff>destroy</on_poweroff>
    <on_reboot>restart</on_reboot>
    <on_crash>destroy</on_crash>
    <pm>
      <suspend-to-mem enabled="no"/>
      <suspend-to-disk enabled="no"/>
    </pm>
    <devices>
      <emulator>/usr/bin/qemu-system-x86_64</emulator>
      <disk type="file" device="disk">
        <driver name="qemu" type="qcow2" discard="unmap"/>
        <source file="/var/lib/libvirt/images/win11.qcow2"/>
        <target dev="sda" bus="sata"/>
        <address type="drive" controller="0" bus="0" target="0" unit="0"/>
      </disk>
      <controller type="usb" index="0" model="qemu-xhci" ports="15">
        <address type="pci" domain="0x0000" bus="0x02" slot="0x00" function="0x0"/>
      </controller>
      <controller type="pci" index="0" model="pcie-root"/>
      <controller type="pci" index="1" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="1" port="0x10"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x0" multifunction="on"/>
      </controller>
      <controller type="pci" index="2" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="2" port="0x11"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x1"/>
      </controller>
      <controller type="pci" index="3" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="3" port="0x12"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x2"/>
      </controller>
      <controller type="pci" index="4" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="4" port="0x13"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x3"/>
      </controller>
      <controller type="pci" index="5" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="5" port="0x14"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x4"/>
      </controller>
      <controller type="pci" index="6" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="6" port="0x15"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x5"/>
      </controller>
      <controller type="pci" index="7" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="7" port="0x16"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x6"/>
      </controller>
      <controller type="pci" index="8" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="8" port="0x17"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x02" function="0x7"/>
      </controller>
      <controller type="pci" index="9" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="9" port="0x18"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x0" multifunction="on"/>
      </controller>
      <controller type="pci" index="10" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="10" port="0x19"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x1"/>
      </controller>
      <controller type="pci" index="11" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="11" port="0x1a"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x2"/>
      </controller>
      <controller type="pci" index="12" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="12" port="0x1b"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x3"/>
      </controller>
      <controller type="pci" index="13" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="13" port="0x1c"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x4"/>
      </controller>
      <controller type="pci" index="14" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="14" port="0x1d"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x5"/>
      </controller>
      <controller type="pci" index="15" model="pcie-root-port">
        <model name="pcie-root-port"/>
        <target chassis="15" port="0x1e"/>
        <address type="pci" domain="0x0000" bus="0x00" slot="0x03" function="0x6"/>
      </controller>
      <controller type="pci" index="16" model="pcie-to-pci-bridge">
        <model name="pcie-pci-bridge"/>
        <address type="pci" domain="0x0000" bus="0x04" slot="0x00" function="0x0"/>
      </controller>
      <controller type="sata" index="0">
        <address type="pci" domain="0x0000" bus="0x00" slot="0x1f" function="0x2"/>
      </controller>
      <controller type="virtio-serial" index="0">
        <address type="pci" domain="0x0000" bus="0x03" slot="0x00" function="0x0"/>
      </controller>
      <interface type="network">
        <mac address="4c:77:cb:83:bb:ab"/>
        <source network="default"/>
        <model type="e1000e"/>
        <address type="pci" domain="0x0000" bus="0x01" slot="0x00" function="0x0"/>
      </interface>
      <input type="mouse" bus="ps2"/>
      <input type="keyboard" bus="ps2"/>
      <input type="evdev">
        <source dev="/dev/input/by-id/usb-Logitech_USB_Receiver-event-mouse"/>
      </input>
      <input type="evdev">
        <source dev="/dev/input/by-id/usb-Nordic_Semiconductor_nRF52_USB_Product_000000000000-event-kbd" grab="all" grabToggle="alt-alt" repeat="on"/>
      </input>
      <tpm model="tpm-tis">
        <backend type="emulator" version="2.0"/>
      </tpm>
      <graphics type="spice" autoport="yes">
        <listen type="address"/>
        <image compression="off"/>
      </graphics>
      <sound model="ich9">
        <address type="pci" domain="0x0000" bus="0x00" slot="0x1b" function="0x0"/>
      </sound>
      <audio id="1" type="spice"/>
      <video>
        <model type="none"/>
      </video>
      <hostdev mode="subsystem" type="pci" managed="yes">
        <source>
          <address domain="0x0000" bus="0x02" slot="0x00" function="0x0"/>
        </source>
        <address type="pci" domain="0x0000" bus="0x05" slot="0x00" function="0x0"/>
      </hostdev>
      <hostdev mode="subsystem" type="pci" managed="yes">
        <source>
          <address domain="0x0000" bus="0x02" slot="0x00" function="0x1"/>
        </source>
        <address type="pci" domain="0x0000" bus="0x06" slot="0x00" function="0x0"/>
      </hostdev>
      <redirdev bus="usb" type="spicevmc">
        <address type="usb" bus="0" port="2"/>
      </redirdev>
      <redirdev bus="usb" type="spicevmc">
        <address type="usb" bus="0" port="3"/>
      </redirdev>
      <watchdog model="itco" action="reset"/>
      <memballoon model="none"/>
      <shmem name="looking-glass">
        <model type="ivshmem-plain"/>
        <size unit="M">128</size>
        <address type="pci" domain="0x0000" bus="0x10" slot="0x01" function="0x0"/>
      </shmem>
    </devices>
  </domain>

This is my personal xml from libvirt, you will have to pull the pertinent parts out and implement them into your own configuration.
===========
QEMU README
===========

QEMU is a generic and open source machine & userspace emulator and
virtualizer.

QEMU is capable of emulating a complete machine in software without any
need for hardware virtualization support. By using dynamic translation,
it achieves very good performance. QEMU can also integrate with the Xen
and KVM hypervisors to provide emulated hardware while allowing the
hypervisor to manage the CPU. With hypervisor support, QEMU can achieve
near native performance for CPUs. When QEMU emulates CPUs directly it is
capable of running operating systems made for one machine (e.g. an ARMv7
board) on a different machine (e.g. an x86_64 PC board).

QEMU is also capable of providing userspace API virtualization for Linux
and BSD kernel interfaces. This allows binaries compiled against one
architecture ABI (e.g. the Linux PPC64 ABI) to be run on a host using a
different architecture ABI (e.g. the Linux x86_64 ABI). This does not
involve any hardware emulation, simply CPU and syscall emulation.

QEMU aims to fit into a variety of use cases. It can be invoked directly
by users wishing to have full control over its behaviour and settings.
It also aims to facilitate integration into higher level management
layers, by providing a stable command line interface and monitor API.
It is commonly invoked indirectly via the libvirt library when using
open source applications such as oVirt, OpenStack and virt-manager.

QEMU as a whole is released under the GNU General Public License,
version 2. For full licensing details, consult the LICENSE file.


Documentation
=============

Documentation can be found hosted online at
`<https://www.qemu.org/documentation/>`_. The documentation for the
current development version that is available at
`<https://www.qemu.org/docs/master/>`_ is generated from the ``docs/``
folder in the source tree, and is built by `Sphinx
<https://www.sphinx-doc.org/en/master/>`_.


Building
========

QEMU is multi-platform software intended to be buildable on all modern
Linux platforms, OS-X, Win32 (via the Mingw64 toolchain) and a variety
of other UNIX targets. The simple steps to build QEMU are:


.. code-block:: shell

  mkdir build
  cd build
  ../configure
  make

Additional information can also be found online via the QEMU website:

* `<https://wiki.qemu.org/Hosts/Linux>`_
* `<https://wiki.qemu.org/Hosts/Mac>`_
* `<https://wiki.qemu.org/Hosts/W32>`_


Submitting patches
==================

The QEMU source code is maintained under the GIT version control system.

.. code-block:: shell

   git clone https://gitlab.com/qemu-project/qemu.git

When submitting patches, one common approach is to use 'git
format-patch' and/or 'git send-email' to format & send the mail to the
qemu-devel@nongnu.org mailing list. All patches submitted must contain
a 'Signed-off-by' line from the author. Patches should follow the
guidelines set out in the `style section
<https://www.qemu.org/docs/master/devel/style.html>`_ of
the Developers Guide.

Additional information on submitting patches can be found online via
the QEMU website

* `<https://wiki.qemu.org/Contribute/SubmitAPatch>`_
* `<https://wiki.qemu.org/Contribute/TrivialPatches>`_

The QEMU website is also maintained under source control.

.. code-block:: shell

  git clone https://gitlab.com/qemu-project/qemu-web.git

* `<https://www.qemu.org/2017/02/04/the-new-qemu-website-is-up/>`_

A 'git-publish' utility was created to make above process less
cumbersome, and is highly recommended for making regular contributions,
or even just for sending consecutive patch series revisions. It also
requires a working 'git send-email' setup, and by default doesn't
automate everything, so you may want to go through the above steps
manually for once.

For installation instructions, please go to

*  `<https://github.com/stefanha/git-publish>`_

The workflow with 'git-publish' is:

.. code-block:: shell

  $ git checkout master -b my-feature
  $ # work on new commits, add your 'Signed-off-by' lines to each
  $ git publish

Your patch series will be sent and tagged as my-feature-v1 if you need to refer
back to it in the future.

Sending v2:

.. code-block:: shell

  $ git checkout my-feature # same topic branch
  $ # making changes to the commits (using 'git rebase', for example)
  $ git publish

Your patch series will be sent with 'v2' tag in the subject and the git tip
will be tagged as my-feature-v2.

Bug reporting
=============

The QEMU project uses GitLab issues to track bugs. Bugs
found when running code built from QEMU git or upstream released sources
should be reported via:

* `<https://gitlab.com/qemu-project/qemu/-/issues>`_

If using QEMU via an operating system vendor pre-built binary package, it
is preferable to report bugs to the vendor's own bug tracker first. If
the bug is also known to affect latest upstream code, it can also be
reported via GitLab.

For additional information on bug reporting consult:

* `<https://wiki.qemu.org/Contribute/ReportABug>`_


ChangeLog
=========

For version history and release notes, please visit
`<https://wiki.qemu.org/ChangeLog/>`_ or look at the git history for
more detailed information.


Contact
=======

The QEMU community can be contacted in a number of ways, with the two
main methods being email and IRC

* `<mailto:qemu-devel@nongnu.org>`_
* `<https://lists.nongnu.org/mailman/listinfo/qemu-devel>`_
* #qemu on irc.oftc.net

Information on additional methods of contacting the community can be
found online via the QEMU website:

* `<https://wiki.qemu.org/Contribute/StartHere>`_
