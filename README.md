## About
tpt - text presentation tool.
Inspired by [suckless sent](https://tools.suckless.org/sent/).

## Usage
**$** tpt

**$** tpt example.txt

**$** cat example.txt | tpt

**$** printf "Slide 1\\n\\nSlide 2" | tpt

## Dependencies
* Python.
* The customtkinter python library.

## Configuration
The configuration on linux systems is done through creating a custom .ini file located at ~/.config/tpt/config.ini which overwrites the default configuration. 
An example configuration file containing all values can be copied from /usr/share/tpt/config.ini on linux systems.
Following are some values from the configuration file:

| Section              | Key                | Default                | Notes                                              |
|----------------------|--------------------|------------------------|----------------------------------------------------|
| `[appearance]`       | `appearance_mode`  | `dark`                 | Theme. May be `dark`, `light` or `system`.         |
| `[appearance]`       | `show_progress`    | `true`                | Shows how much more of your presentation has to be endured. |
| `[appearance]`       | `progress_style`   | `bar`                  | How progress is shown. May be `text` or `bar`.     |
