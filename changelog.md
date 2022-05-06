# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [x.y.z] - yyyy-mm-dd
### Added
### Changed
### Removed
### Fixed
-->

<!-- ## [Unreleased] -->

## Released
## [0.3.0] - 2022-05-06
### Added
- This changelog file
- `mpy_cross` python package added to [`requirements.txt`](requirements.txt)

### Changed
- Instructions to cross-compile modules in [`README`](README.md), see [#4][ref-issue-4]
- `flash_led` function extracted from [`main`](main.py) into
  [`blink`](blink.py) script
- Import `flash_led` function in [`main`](main.py) from [`blink`](blink.py)
- Ignore `*.mpy` cross-compiled files

## [0.2.0] - 2022-04-24
### Added
- [`.gitignore`](.gitignore) file
- [`requirements.txt`](requirements.txt) file
- Doc string for [`boot`](boot.py) and [`main`](main.py), see [#2][ref-issue-2]

### Changed
- Replace `ampy` in [`README`](README.md) with `rshell`, see [#1][ref-issue-1]

## [0.1.0] - 2021-07-03
### Added
- Micropython [`boot`](boot.py) and [`main`](main.py) files
- [`README`](README.md) file

<!-- Links -->
[Unreleased]: https://github.com/brainelectronics/Micropython-Blink/compare/0.3.0...develop

[0.3.0]: https://github.com/brainelectronics/Micropython-Blink/tree/0.3.0
[0.2.0]: https://github.com/brainelectronics/Micropython-Blink/tree/0.2.0
[0.1.0]: https://github.com/brainelectronics/Micropython-Blink/tree/0.1.0

[ref-issue-4]: https://github.com/brainelectronics/Micropython-Blink/issues/4
[ref-issue-2]: https://github.com/brainelectronics/Micropython-Blink/issues/2
[ref-issue-1]: https://github.com/brainelectronics/Micropython-Blink/issues/1
