# Pykeys (WIP)

Python key and password generator tool.

## Requirements

Python 3.6+.

## Usage

### Key generation

To generate three keys with 256 characters:

```
python3 -m pykeys 3 256
```

To generate the default single key with 16 characters:

```
python3 -m pykeys
```

The maximum number of keys and characters that can be generated is 100 and 256:

```
python3 -m pykeys 100 256
```

### Errors

Passing string literals as arguments will throw an error.

### Output

The output of the keys is printed to stdout and stored in a file called "pykeys.txt" in your 
current working directory.

## Contributing

See [the contributing guide](contributing.md).
