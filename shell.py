# basic shell

import base
import spm
import os

try:
	while True:
		line = input("> ")
	
		if line == "pls update":
			spm.update_kernel()
			spm.finalize_kernel_update()
			spm.cleanup()

		elif line == "setup file-system":
			base.setup_filesystem()
    
		elif line == "clear":
			base.clear_screen()

		elif line == "exit":
			break
		
		else:
			print("invalid command")

except KeyboardInterrupt:
	print("\n")
	os._exit(0)
