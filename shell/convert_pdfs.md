# some command is very helpfull

convert all file in current directory

```sh
$ ls -t | xargs -t -n 1 -I % ps2pdf % after_%
```
