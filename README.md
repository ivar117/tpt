## About
tpt - text presentation tool.
Inspired by [suckless sent](https://tools.suckless.org/sent/).

## Usage
**$** tpt

**$** tpt file.txt

**$** cat file.txt | tpt

**$** printf "Slide 1\\n\\nSlide 2" | tpt

## Dependencies
* Python.
* The customtkinter python library.

## Configuration
The configuration on linux systems is done through creating a custom .ini file located at ~/.config/tpt/config.ini which overwrites the default configuration. 
An example configuration containing all values is located at /usr/share/tpt/config.ini
Following are some values:

| Section              | Key                | Default                | Notes                                              |
|----------------------|--------------------|------------------------|----------------------------------------------------|
| `[appearance]`       | `appearance_mode`  | `dark`                 | Theme. May be `dark`, `light` or `system`.         |
| `[appearance]`       | `show_progress`    | `false`                | Shows how much more of your presentation has to be endured. |
| `[appearance]`       | `progress_style`   | `bar`                  | How progress is shown. May be `text` or `bar`.     |
