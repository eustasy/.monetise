Locksmith
=========

## Offline License Types

| Name | Description |
|:--|:--|
| Perpetual   | License works forever for any version, on any machine.
| Maintenance | License works for a specific major version only. New major versions usually available at a discount to existing customers.
| Node-locked | License works on a specific machine-id, generated from hardware signatures.
| User-locked | License works on a specific userPrincipleName (domain users only, not recommended).

## File Descriptions

| File | Description |
|:--|:--|
| setup.py    | Setup your license server by generating a private/public keypair.
| generate.py | Generate a new license key based on a user email.
| activate.py | Run on application start to verify license key.
| helpers.py  | Helper class for machine and user locking.
