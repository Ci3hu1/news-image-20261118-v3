#!/usr/bin/env python3
"""Tests for the news-image-20261118 v3 entry.

- The program exits 0 and writes a valid 1024x1024 PNG.
- With PIL hidden (python3 -S, no site-packages) it takes the copy path and
  produces a byte-identical file to the bundled entry.png.
- With PIL available it takes the render path and produces a byte-identical
  file to the bundled entry.png.
- Two render runs are byte-identical (deterministic).
"""
import hashlib
import os
import struct
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MAIN = os.path.join(ROOT, "main.py")
BUNDLED = os.path.join(ROOT, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(33)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    w, h = struct.unpack(">II", head[16:24])
    return w, h


class TestEntry(unittest.TestCase):
    def test_bundled_exists_and_is_1024(self):
        self.assertTrue(os.path.isfile(BUNDLED), "entry.png missing")
        self.assertEqual(png_size(BUNDLED), (1024, 1024))

    def test_copy_path_no_pil(self):
        """python3 -S hides site-packages, so PIL is unavailable."""
        with tempfile.TemporaryDirectory() as td:
            out = os.path.join(td, "out.png")
            r = subprocess.run([sys.executable, "-S", MAIN, out],
                               capture_output=True, text=True, timeout=120)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(sha256(out), sha256(BUNDLED))
            self.assertEqual(png_size(out), (1024, 1024))

    def test_render_path_with_pil(self):
        with tempfile.TemporaryDirectory() as td:
            out = os.path.join(td, "out.png")
            r = subprocess.run([sys.executable, MAIN, out],
                               capture_output=True, text=True, timeout=120)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(sha256(out), sha256(BUNDLED))
            self.assertEqual(png_size(out), (1024, 1024))

    def test_deterministic(self):
        with tempfile.TemporaryDirectory() as td:
            a = os.path.join(td, "a.png")
            b = os.path.join(td, "b.png")
            for out in (a, b):
                r = subprocess.run([sys.executable, MAIN, out],
                                   capture_output=True, text=True,
                                   timeout=120)
                self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(sha256(a), sha256(b))


if __name__ == "__main__":
    unittest.main()
