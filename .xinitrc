#!/bin/sh

systemctl --user import-environment DISPLAY

rm ~/awesome-startup
exec awesome
