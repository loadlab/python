#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `loadLab` package."""


import unittest
from click.testing import CliRunner

from loadlab import LoadLab
from loadlab import cli
from unittest import mock


@mock.patch('loadlab.loadlab.Resource.get')
class TestLoadlabClient(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        self.loadlab = LoadLab()

    def test_plans(self, get):
        """Test plans """
        get.return_value = {}
        resp = self.loadlab.plans.get()
        self.assertEqual(resp, {})

    def test_jobs(self, get):
        """Test jobs """
        get.return_value = {}
        resp = self.loadlab.jobs.get()
        self.assertEqual(resp, {})

    def test_sites(self, get):
        """Test sites """
        get.return_value = {}
        resp = self.loadlab.sites.get()
        self.assertEqual(resp, {})


class TestLoadlabCLI(unittest.TestCase):

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'loadlab.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
