# basic shell

import kernel
import spm
import os

while True:

	line = input("> ")
	
	if line == "pls update":
		spm.update_kernel()
		spm.finalize_kernel_update()
		spm.cleanup()

	if line == "setup file-system":
		kernel.setup_filesystem()
    
	if line == "clear":
		kernel.clear_screen()

	if line == "exit":
		break
		os.exit()



