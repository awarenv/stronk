# Stronk
[![CircleCI](https://circleci.com/gh/hash-vault/stronk.svg?style=svg)](https://circleci.com/gh/hash-vault/stronk)
[![stronk](https://img.shields.io/pypi/v/stronk.svg)](https://pypi.org/project/stronk/)

Strong Python key and password generator tool.

## Requirements

Python 3.6+.

## Usage

### Key generation

To generate three keys with 256 characters:

```
stronk 3 256
```

To generate the default single key with 16 characters:

```
stronk
```

The maximum number of keys and characters that can be generated is 100 and 256:

```
stronk 100 256
```

Add the flag -i to generate identifiers alongside the keys for easier readibility, which also gets printed to the
file.  This is disabled by default.

```
stronk -i 3 256
```

### Errors

Passing string literals as arguments will throw an error.

### Output

The output of the keys is printed to stdout and stored in a file called "stronk.txt" in your 
current working directory.

## Contributing

See [the contributing guide](CONTRIBUTING.md).
