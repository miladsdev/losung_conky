# Losung Conky

## usage
Running the configs:
```bash
git clone https://github.com/miladsdev/losung_conky.git ~/.config/losung_conky/
cd .config/losung_conky

# simple losung
conky -c losung_simple.conf

# or losung + monitor
conky -c losung_monitor.conf
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
