c.fileselect.handler = "external"
c.fileselect.single_file.command = ["wezterm", "-e", "yazi", "--chooser-file={}"]
c.fileselect.multiple_files.command = ["wezterm", "-e", "yazi", "--chooser-file={}"]
c.fileselect.folder.command = ["wezterm", "-e", "yazi", "--chooser-file={}"]

c.editor.command = [ "wezterm", "-e", "nvim", "-f", "{file}", "-c", "normal {line}G{column0}l"]
