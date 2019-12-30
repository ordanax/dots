Script: openweathermap-fullfeatured

A weather script that shows a lot of information.

It shows icons and temperatures for the current weather and the 3 hour forecast. It displays information about the next sunrise or sunset.

openweathermap-fullfeatured
Dependencies

    OpenWeatherMap-Key
    weather-icons
    jq

Configuration

If CITY is left empty, the location is retrieved via the Mozilla Location API. CITY can either be a city ID (e.g. ID of Berlin is 2950159), city name (e.g. Berlin) or city name + country code (e.g. Berlin,DE).

Change these values:

KEY=""
CITY=""
UNITS="metric"
SYMBOL="°"

Module

[bar/polybar]
...
font-2 = Weather Icons:size=12;1
...

[module/openweathermap-fullfeatured]
type = custom/script
exec = ~/polybar-scripts/openweathermap-fullfeatured.sh
interval = 600
label-font = 3
