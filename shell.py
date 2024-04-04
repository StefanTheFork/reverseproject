# basic shell

import base
import spm
import os

while True:

	line = input("> ")
	
	if line == "pls update":
		spm.update_base()
		spm.finalize_base_update()
		spm.cleanup()

	if line == "setup file-system":
		base.setup_filesystem()
    
	if line == "clear":
		base.clear_screen()

	if line == "exit":
		break



