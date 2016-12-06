# Using TREZOR as a hardware SSH/GPG agent

[![Build Status](https://travis-ci.org/romanz/trezor-agent.svg?branch=master)](https://travis-ci.org/romanz/trezor-agent)
[![Python Versions](https://img.shields.io/pypi/pyversions/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)
[![Package Version](https://img.shields.io/pypi/v/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)
[![Development Status](https://img.shields.io/pypi/status/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)
[![Downloads](https://img.shields.io/pypi/dm/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)

See SatoshiLabs' blog posts about this feature:

- [TREZOR Firmware 1.3.4 enables SSH login](https://medium.com/@satoshilabs/trezor-firmware-1-3-4-enables-ssh-login-86a622d7e609)
- [TREZOR Firmware 1.3.6 — GPG Signing, SSH Login Updates and Advanced Transaction Features for Segwit](https://medium.com/@satoshilabs/trezor-firmware-1-3-6-20a7df6e692)
- [TREZOR Firmware 1.4.0 — GPG decryption support](https://www.reddit.com/r/TREZOR/comments/50h8r9/new_trezor_firmware_fidou2f_and_initial_ethereum/d7420q7/)

## Installation

First, make sure that the latest [trezorlib](https://pypi.python.org/pypi/trezor) Python package
is installed correctly (at least v0.6.6):

	$ apt-get install python-dev libusb-1.0-0-dev libudev-dev
	$ pip install -U setuptools
	$ pip install Cython trezor

Make sure that your `udev` rules are configured [correctly](https://doc.satoshilabs.com/trezor-user/settingupchromeonlinux.html#manual-configuration-of-udev-rules).
Then, install the latest [trezor_agent](https://pypi.python.org/pypi/trezor_agent) package:

	$ pip install trezor_agent

Or, directly from the latest source code (if `pip` doesn't work for you):

	$ git clone https://github.com/romanz/trezor-agent && cd trezor-agent
	$ python setup.py build && python setup.py install

Finally, verify that you are running the latest [TREZOR firmware](https://wallet.mytrezor.com/data/firmware/releases.json) version (at least v1.4.0):

	$ trezorctl get_features | head
	vendor: "bitcointrezor.com"
	major_version: 1
	minor_version: 4
	patch_version: 0
	...

If you have an error regarding `protobuf` imports (after installing it), please see [this issue](https://github.com/romanz/trezor-agent/issues/28).

## Usage

For SSH, see the [following instructions](README-SSH.md) (for Windows support,
see [trezor-ssh-agent](https://github.com/martin-lizner/trezor-ssh-agent) project (by Martin Lízner)).

For GPG, see the [following instructions](README-GPG.md).

See [here](https://github.com/romanz/python-trezor#pin-entering) for PIN entering instructions.

## Troubleshooting

If there is an import problem with the installed `protobuf` package,
see [this issue](https://github.com/romanz/trezor-agent/issues/28) for fixing it.

### Gitter

Questions, suggestions and discussions are welcome: [![Chat](https://badges.gitter.im/romanz/trezor-agent.svg)](https://gitter.im/romanz/trezor-agent)
