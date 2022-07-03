# touka.ssh
> touka.ssh is an ssh manager that allows you to manage all of your VPSs without keeping your password.

## Installing
```
pip3 install -U touka.ssh
```


## help 
> touka --help
```
Usage: touka.ssh [OPTIONS] COMMAND [ARGS]...

  Awesome ssh manager, especially made for anii ☂️

Options:
  -v, --version  Show the application's version and exit.
  --help                          Show this message and exit.

Commands:
  add      Add a new ssh connection with a description.
  connect  connect to server via name
  init     assign pub key to your IP machine
  list     list of all saved servers.
  purge    purge your stored servers.
```
## Init
assign pub key to your IP machine
```sh
touka init
```

## add
Add a new ssh connection with a description.
```sh
touka add -a 192.168.0.9 -n meanii-ubuntu -d "meanii modlette's server digitalocean"
```

## list
list of all saved servers.

```
Servers you have saved:

ID.  | Name  | Address  | Port  | Description  
-----------------------------------------------
1    | meanii-ubuntu | 192.168.0.9 | 22 | meanii modlette's server digitalocean 
-----------------------------------------------
```

## connect
connect to server via name
```sh
touka connect -n meanii-ubuntu
```

---
###  Copyright & License
- Copyright (C)  2022 [meanii](https://github.om/meanii )
- Licensed under the terms of the [GNU General Public License v3.0](https://github.com/meanii/touka.ssh/blob/main/LICENSE)