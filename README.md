# .monetise

## License Types

| Name | Description |
|:--|:--|
| Perpetual | License works forever on any version.
| Perpetual (with Maintenance) | License works forever for a specific major version only. New major versions usually available at a discount to existing customers.
| Node-locked | License works forever on a specific machine-id, generated from hardware signatures.
| User-based | 
| Offline | 

## File Descriptions

| File | Description |
|:--|:--|
| setup.py | Setup your license server by generating a private/public keypair
| generate.py | Generate a new license key based on a user email
| activate.py | Run on application start to verify license key
