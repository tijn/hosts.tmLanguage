# hosts.tmLanguage

Scrupulous Syntax Highlighting for /etc/hosts

## Features

* It highlights IPv4 and IPv6 addresses rigidly. For example: it won't match the impossible movie IP-address `189.23.290.13`. This makes it easier to spot errors.
* It styles private IPv4 address-ranges and public IPs differently. It supports all three private ranges: `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.

## Installation

Install via [Package Control](https://packagecontrol.io/).

## Acknowledgements

The regular expressions for IPv6 by David M. Syzdek were found [on stackoverflow.com](http://stackoverflow.com/a/17871737/852657). I had to rewrite them in a different format so any faults or mistakes are probably mine.
