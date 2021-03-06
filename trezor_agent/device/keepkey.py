"""KeepKey-related code (see https://www.keepkey.com/)."""

from . import trezor
from .. import formats


def _verify_support(identity, ecdh):
    """Make sure the device supports given configuration."""
    protocol = identity.identity_dict['proto']
    if protocol not in {'ssh'}:
        raise NotImplementedError(
            'Unsupported protocol: {}'.format(protocol))
    if ecdh:
        raise NotImplementedError('No support for ECDH')
    if identity.curve_name not in {formats.CURVE_NIST256}:
        raise NotImplementedError(
            'Unsupported elliptic curve: {}'.format(identity.curve_name))


class KeepKey(trezor.Trezor):
    """Connection to KeepKey device."""

    from . import keepkey_defs as defs

    required_version = '>=1.0.4'

    def pubkey(self, identity, ecdh=False):
        """Return public key."""
        _verify_support(identity, ecdh)
        return trezor.Trezor.pubkey(self, identity=identity, ecdh=ecdh)

    def ecdh(self, identity, pubkey):
        """No support for ECDH in KeepKey firmware."""
        _verify_support(identity, ecdh=True)
