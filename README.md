# hosts.tmLanguage

Scrupulous Syntax Highlighting for `/etc/hosts`

![Screenshot][demo.png]

## Features

* It highlights IPv4 and IPv6 addresses rigidly. For example: it won't match the impossible movie IP-address `189.23.290.13`. This makes it easier to spot errors.
* It uses different scopes (i.e. different colors) for some [special IP ranges][reserved-ips]:
    - Loopback: `::1` and `127.0.0/8`
    - Private: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, and `fc00::/7`
* Hostnames are in the local index: <kbd>Ctrl</kbd>+<kbd>R</kbd> (MacOS: <kbd>Cmd</kbd>+<kbd>R</kbd>)
* Hoverable tooltips on [Punycode][] hostname segments to render [internationalized domain names][idna].
* Command Palette item to open Hosts file.

## Installation

Install via [Package Control](https://packagecontrol.io/).

## Acknowledgements

The regular expressions for IPv6 by David M. Syzdek were found [on stackoverflow.com](http://stackoverflow.com/a/17871737/852657). I had to rewrite them in a different format, so any faults or mistakes are probably mine.

[Michael Lyons](https://github.com/michaelblyons) provided fixes and some great additions. And after that he rewrote the whole thing to add support for IPv6 (though still based on David M. Szydek).

[demo.png]: demo/demo.png
[reserved-ips]: https://en.wikipedia.org/wiki/Reserved_IP_addresses
[punycode]: https://en.wikipedia.org/wiki/Punycode#Internationalized_domain_names
[idna]: https://en.wikipedia.org/wiki/Internationalized_domain_name
