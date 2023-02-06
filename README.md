# Losung Conky

## usage
Running the config:
```bash
git clone https://github.com/miladsdev/losung_conky.git ~/.config/
cd .config/losung_conky
conky -c conky.conf
```

Adding losung_simple (without system monitor) to autoload:
```bash
cd .config/losung_conky
cp .losung_simple.desktop ../autostart/
```

Adding losung_monitor (with system monitor) to autoload:
```bash
cd .config/losung_conky
cp .losung_monitor.desktop ../autostart/
```
