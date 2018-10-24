# AIY Vision Kit Playground

- pi@10.0.0.X 
- Username: pi
- PW: raspberry


## 設定成可以remote的狀態

[Youtube](https://www.youtube.com/watch?v=L2XaFmt9xsA): How to Remote Desktop to Raspberry Pi from Apple Mac

### 首先安裝不知名的套件:總之跟remote 有關

```
$ sudo apt-get install xrdp
```

查看各種奇怪的參數
```
ifconfig
```

### 在pi上面安裝遠端存取軟體

```
sudo apt-get install netatalk
```

然後在電腦(mac)上terminal 指令

```
open afp://10.1.1.10  (replace this with your Raspberry Pi IP address)
```