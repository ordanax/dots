# Скрипт: openweathermap-fullfeatured

Скрипт для тектового отображения погоды для Polybar

![openweathermap-fullfeatured](https://i.imgur.com/wxg5roM.png)


## Зависимости

* [weather-icons](https://github.com/erikflowers/weather-icons)
* `jq`


## Настройки

Зарегистрируйтесь на сайте https://openweathermap.org
Скопируйте название вашего города и API.

Измените в скрипте данные на свои:

```sh
KEY=""
CITY=""
UNITS="metric"
SYMBOL="°C"
```


## Модуль

```ini
[bar/polybar]
...
font-2 = Weather Icons:size=12;1
...
```

```ini
[module/openweathermap-fullfeatured]
type = custom/script
exec = ~/.config/polybar/scripts/openweathermap-fullfeatured.sh
interval = 600
label-font = 3
```
