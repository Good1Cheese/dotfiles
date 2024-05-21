-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices

-- For example, changing the color scheme:
config.colors = {
	-- foreground = "#CBE0F0",
	-- background = "#011423",
	-- cursor_bg = "#47FF9C",
	-- cursor_border = "#47FF9C",
	-- cursor_fg = "#011423",
	selection_bg = "#706b4e",
	selection_fg = "#f3d9c4",
	-- ansi = { "#214969", "#E52E2E", "#44FFB1", "#FFE073", "#0FC5ED", "#a277ff", "#24EAF7", "#24EAF7" },
	-- brights = { "#214969", "#E52E2E", "#44FFB1", "#FFE073", "#A277FF", "#a277ff", "#24EAF7", "#24EAF7" },
}

config.color_scheme = "Everblush"
-- config.color_scheme = "Batman"
-- config.color_scheme = "Belafonte Night"
-- config.color_scheme = "Bespin (dark) (terminal.sexy)"
-- config.color_scheme = "s3r0 modified (terminal.sexy)"
-- config.color_scheme = "Sakura"
-- config.color_scheme = "Sea Shells (Gogh)"

config.font = wezterm.font("JetBrainsMono Nerd Font")
config.font_size = 13

config.window_close_confirmation = "NeverPrompt"

config.freetype_load_target = "Light"
config.freetype_render_target = "HorizontalLcd"

config.enable_tab_bar = false

return config
