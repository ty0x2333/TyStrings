-- tystrings.scpt
--
-- The MIT License (MIT)
-- 
-- Copyright (c) 2017 luckytianyiyan
-- 
-- Permission is hereby granted, free of charge, to any person obtaining a copy
-- of this software and associated documentation files (the "Software"), to deal
-- in the Software without restriction, including without limitation the rights
-- to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-- copies of the Software, and to permit persons to whom the Software is
-- furnished to do so, subject to the following conditions:
-- 
-- The above copyright notice and this permission notice shall be included in all
-- copies or substantial portions of the Software.
-- 
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-- IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-- FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-- AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-- LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-- OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-- SOFTWARE.
--

set currentPath to getCurrentPath() as alias

activateiTerms()
setWindowTitle("TyStrings Demo")

# cd to repo root path
runCommand("cd " & (quoted form of POSIX path of currentPath) & "../")
runCommand("source venv/bin/activate")
runCommand("cd tests/example/")
clear()
runCommand("ttyrec ../../resource/recording")
delay 0.5
runTyStringsSubCommand("generate", {"$(find . -name \\*.m)", "-o", "en.lproj zh-Hans.lproj"})
delay 2
clear()
runTyStringsSubCommand("translate", {"strings/base_translator.strings", "zh-Hans.lproj/base_translator.strings", "--dst-lang", "zh", "--src-lang", "en", "--appid", "20160709000024959", "--secret", "ke4UYwwvvgV9iQEIVjrC"})
delay 2
clear()
runTyStringsSubCommand("diff", {"strings/diff1.strings", "strings/diff2.strings"})
delay 2
clear()
runTyStringsSubCommand("lint", {"strings/lint.strings"})
delay 2
runCommand("exit")
delay 0.5
runCommand("cd " & (quoted form of POSIX path of currentPath) & "../")
runCommand("deactivate")
runCommand("ttygif resource/recording -f")
runCommand("mv tty.gif resource/tystrings.gif")

# clean
runCommand("rm -rf tests/example/en.lproj")
runCommand("rm -rf tests/example/zh-Hans.lproj")

# ------- TyStrings Helper ------- 

on runTyStringsSubCommand(subcommand, args)
	typingString("tys")
	typingStringWithDelay("trings ", 0)
	typingString(subcommand & " ")
	repeat with i from 1 to count of args
		typingStringWithDelay(item i of args & " ", 0.02)
	end repeat
	# typing '\n'
	typingString("
")
	
end runTyStringsSubCommand

# ------- Core ------- 

on typingString(content)
	typingStringWithDelay(content, 0.1)
end typingString

on typingStringWithDelay(content, dy)
	tell application "iTerm"
		tell current session of current window
			set charList to (characters 1 thru (length of content) of content)
			repeat with char in charList
				write text char newline no
				delay dy
			end repeat
		end tell
	end tell
end typingStringWithDelay

on runCommand(command)
	tell application "iTerm"
		tell current session of current window
			write text command
		end tell
	end tell
end runCommand

on clear()
	runCommand("clear")
	delay 0.1
end clear

on isAppRunning(appName)
	tell application "System Events" to (name of processes) contains appName
end isAppRunning

on setWindowTitle(title)
	runCommand("echo -e \"\\033];" & title & "\\007\"")
end setWindowTitle

on activateiTerms()
	if isAppRunning("iTerm") then
		tell application "iTerm"
			activate
		end tell
	else
		activate application "iTerm"
	end if
end activateiTerms

on getCurrentPath()
	tell application "Finder"
		return container of (path to me)
	end tell
end getCurrentPath
