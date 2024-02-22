# test_formatters: test the formatters
#
# Copyright (C) 2021 Red Hat, Inc.
#
# SPDX-License-Identifier: GPL-2.0-or-later

import pytest

import test_utils.utils as test_utils
from pathlib import Path

from lcitool.targets import BuildTarget
from lcitool.formatters import ShellVariablesFormatter, JSONVariablesFormatter, DockerfileFormatter, ShellBuildEnvFormatter


scenarios = [
    # A minimalist application, testing package managers
    pytest.param("libvirt-go-xml-module", "debian-10", None, id="libvirt-go-xml-module-debian-10"),
    pytest.param("libvirt-go-xml-module", "almalinux-8", None, id="libvirt-go-xml-module-almalinux-8"),
    pytest.param("libvirt-go-xml-module", "opensuse-leap-15", None, id="libvirt-go-xml-module-opensuse-leap-15"),
    pytest.param("libvirt-go-xml-module", "alpine-edge", None, id="libvirt-go-xml-module-alpine-edge"),
    pytest.param("libvirt-go-xml-module", "opensuse-tumbleweed", None, id="libvirt-go-xml-module-opensuse-tumbleweed"),

    # An application using cache symlinks
    pytest.param("libvirt-go-module", "debian-10", None, id="libvirt-go-debian-10"),
    pytest.param("libvirt-go-module", "debian-10", "s390x", id="libvirt-go-debian-10-cross-s390x"),
    pytest.param("libvirt-go-module", "fedora-rawhide", "mingw64", id="libvirt-go-fedora-rawhide-cross-mingw64"),
]

layer_scenarios = [
    # Overriding default base image
    pytest.param("libvirt-go-module", "debian-10", "s390x", "debian-10-common", "all", id="libvirt-go-debian-10-common-cross-s390x"),

    # Customizing the layers
    pytest.param("libvirt-go-module", "fedora-rawhide", "mingw64", None, "all", id="libvirt-go-fedora-rawhide-cross-mingw64-combined"),
    pytest.param("libvirt-go-module", "fedora-rawhide", "mingw64", None, "native", id="libvirt-go-fedora-rawhide-cross-mingw64-native"),
    pytest.param("libvirt-go-module", "fedora-rawhide", "mingw64", None, "foreign", id="libvirt-go-fedora-rawhide-cross-mingw64-foreign"),
    pytest.param("libvirt-go-module", "fedora-rawhide", "mingw64", "fedora-rawhide-common", "foreign", id="libvirt-go-fedora-rawhide-common-cross-mingw64-foreign"),
]


@pytest.mark.parametrize("project,target,arch", scenarios)
def test_dockerfiles(assert_equal, packages, projects, targets, project, target, arch, request):
    gen = DockerfileFormatter(projects)
    target_obj = BuildTarget(targets, packages, target, arch)
    actual = gen.format(target_obj, [project])
    expected_path = Path(test_utils.test_data_outdir(__file__), request.node.callspec.id + ".Dockerfile")
    assert_equal(actual, expected_path)


@pytest.mark.parametrize("project,target,arch,base,layers", layer_scenarios)
def test_dockerfile_layers(assert_equal, packages, projects, targets, project, target, arch, base, layers, request):
    gen = DockerfileFormatter(projects, base, layers)
    target_obj = BuildTarget(targets, packages, target, arch)
    actual = gen.format(target_obj, [project])
    expected_path = Path(test_utils.test_data_outdir(__file__), request.node.callspec.id + ".Dockerfile")
    assert_equal(actual, expected_path)


@pytest.mark.parametrize("project,target,arch", scenarios)
def test_variables_shell(assert_equal, packages, projects, targets, project, target, arch, request):
    gen = ShellVariablesFormatter(projects)
    target_obj = BuildTarget(targets, packages, target, arch)
    actual = gen.format(target_obj, [project])
    expected_path = Path(test_utils.test_data_outdir(__file__), request.node.callspec.id + ".vars")
    assert_equal(actual, expected_path)


@pytest.mark.parametrize("project,target,arch", scenarios)
def test_variables_json(assert_equal, packages, projects, targets, project, target, arch, request):
    gen = JSONVariablesFormatter(projects)
    target_obj = BuildTarget(targets, packages, target, arch)
    actual = gen.format(target_obj, [project])
    expected_path = Path(test_utils.test_data_outdir(__file__), request.node.callspec.id + ".json")
    assert_equal(actual, expected_path)


@pytest.mark.parametrize("project,target,arch", scenarios)
def test_prepbuildenv(assert_equal, packages, projects, targets, project, target, arch, request):
    gen = ShellBuildEnvFormatter(projects)
    target_obj = BuildTarget(targets, packages, target, arch)
    actual = gen.format(target_obj, [project])
    expected_path = Path(test_utils.test_data_outdir(__file__), request.node.callspec.id + ".sh")
    assert_equal(actual, expected_path)
