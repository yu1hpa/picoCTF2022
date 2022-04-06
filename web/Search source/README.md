# Search source
### Description
> The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is here

### Solution
From problem title, You can infer that flag is hidden in the source code.
But, because the source code has many number of lines, searching own take time.
So, you think that you do mirroring the problem web page by using `wget` command and
search the web page's directory in local.
`wget` command can do mirroring by using `--mirror` option.
```
$ wget --mirror http://saturn.picoctf.net:56849/
```

You execute shell command that search wanted string from the web page's directory by combining `find`, `xargs` and `grep`.
```
$ find saturn.picoctf.net\:56849/ -type f | xargs grep "pico"
saturn.picoctf.net:56849/css/style.css:/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_74784981} **/
```

Therefore, flag is `picoCTF{1nsp3ti0n_0f_w3bpag3s_74784981}`.

### Writer
Yajirushi