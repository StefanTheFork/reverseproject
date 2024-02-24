package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
  "time"
)

var clearCmd string
var makeDirCmd string

func init() {
	if osname := os.Getenv("GOOS"); osname == "windows" {
		clearCmd = "cls"
		makeDirCmd = "mkdir"
	} else {
		clearCmd = "clear"
		makeDirCmd = "mkdir"
	}
}

func startLogo() {
	fmt.Println(`
                                  ______   
  use help to get help(?)        |____  |  
  _ __ _____   _____ _ __ ___  ___   / /   
 | '__/ _ \ \ / / _ \ '__/ __|/ _ \ / /  
 | | |  __/\ V /  __/ |  \__ \  __// /  
 |_|  \___| \_/ \___|_|  |___/\_v3/0/  
`)
}

func logo() {
	fmt.Println("!!!!!THE LOGO IS VERY BIG. DON'T GET MAD IF IT'S TOO BIG FOR YOUR TERMINAL/SCREEN!!!!!")
	reader := bufio.NewReader(os.Stdin)
	reader.ReadString('\n')
	fmt.Println(`
                                                                                    

              ████████                                █████                          ██████            ████  ████ 
             ███░░░░███                              ░░███                          ███░░███          ░░███ ░░███ 
 █████ █████░░░    ░███    █████ ███ █████  ██████   ███████    ██████  ████████   ░███ ░░░   ██████   ░███  ░███ 
░░███ ░░███    ██████░    ░░███ ░███░░███  ░░░░░███ ░░░███░    ███░░███░░███░░███ ███████    ░░░░░███  ░███  ░███ 
 ░███  ░███   ░░░░░░███    ░███ ░███ ░███   ███████   ░███    ░███████  ░███ ░░░ ░░░███░      ███████  ░███  ░███ 
 ░░███ ███   ███   ░███    ░░███████████   ███░░███   ░███ ███░███░░░   ░███       ░███      ███░░███  ░███  ░███ 
  ░░█████   ░░████████      ░░████░████   ░░████████  ░░█████ ░░██████  █████      █████    ░░████████ █████ █████
   ░░░░░     ░░░░░░░░        ░░░░ ░░░░     ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░      ░░░░░      ░░░░░░░░ ░░░░░ ░░░░░ 
                                                                                                                  
`)
}

func clearScreen() {
	cmd := exec.Command(clearCmd)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func info() {
	logo()
	fmt.Println(" <reverse7 v3 aka waterfall>")
}

func createTextFile() {
	var filename string
	var contents string
	var line string

	fmt.Print("Enter file name (should be something like example.extention) > ")
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		filename = scanner.Text()
	}
	fmt.Println("Use EOF as the ending line")

	for {
		if scanner.Scan() {
			line = scanner.Text()
			if line == "EOF" {
				break
			}
			contents += line + "\n"
		} else {
			break
		}
	}

	err := ioutil.WriteFile(filename, []byte(contents), 0644)
	if err == nil {
		fmt.Println("File created successfully!")
	} else {
		fmt.Println("Unable to create the file")
	}
}

func readTextFile() {
	var filename string

	fmt.Print("Enter filename > ")
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		filename = scanner.Text()
	}

	content, err := ioutil.ReadFile(filename)
	if err == nil {
		fmt.Print(string(content))
	} else {
		fmt.Println("Unable to open file")
	}
}

func editTextFile() {
	var filename string
	var contents string
	var line string

	fmt.Print("Enter filename > ")
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		filename = scanner.Text()
	}

	content, err := ioutil.ReadFile(filename)
	if err == nil {
		contents = string(content)

		fmt.Printf("Editing file > %s\n", filename)
		fmt.Println("Current content:\n" + contents)

		fmt.Print("Keep the old contents in the file? (use y/n or alr/nah) ")
		var response string
		if scanner.Scan() {
			response = scanner.Text()
		}

		if response == "Y" || response == "y" || response == "alr" {
			fmt.Println("Enter the new content (use EOF as the ending line)")
			for {
				if scanner.Scan() {
					line = scanner.Text()
					if line == "EOF" {
						break
					}
					contents += line + "\n"
				} else {
					break
				}
			}
		} else {
			fmt.Println("Old file contents will be replaced! Enter the new content:")
			contents = ""
			fmt.Println("Enter the new content (use EOF as the ending line)")
			for {
				if scanner.Scan() {
					line = scanner.Text()
					if line == "EOF" {
						break
					}
					contents += line + "\n"
				} else {
					break
				}
			}
		}

		err := ioutil.WriteFile(filename, []byte(contents), 0644)
		if err == nil {
			fmt.Println("File updated successfully!")
		} else {
			fmt.Println("Unable to open the file and write")
		}
	} else {
		fmt.Println("Unable to open file and edit")
	}
}

func deleteFile() {
	var filename string

	fmt.Print("Enter the filename to delete > ")
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		filename = scanner.Text()
	}

	fmt.Printf("Are you sure you want to delete the file \"%s\"? (use y/n or alr/nah) ", filename)
	var response string
	if scanner.Scan() {
		response = scanner.Text()
	}

	if response == "Y" || response == "y" || response == "alr" {
    		err := os.Remove(filename)
		if err == nil {
			fmt.Printf("File \"%s\" nuked successfully!\n", filename)
		} else {
			fmt.Printf("Unable to nuke the file \"%s\"\n", filename)
		}
	} else {
		fmt.Println("File deleter stopped")
	}
}

func timerightnow() {
	fmt.Println("Current time:")
	fmt.Println(time.Now().Format("2006-01-02 15:04:05"))
}

func main() {
	for {
		clearScreen()
		startLogo()
		fmt.Println("Enter a command:")
		fmt.Println("1. Create Text File")
		fmt.Println("2. Read Text File")
		fmt.Println("3. Edit Text File")
		fmt.Println("4. Delete File")
		fmt.Println("5. Show Current Time")
		fmt.Println("6. Quit")

		var choice int
		fmt.Print("Enter your choice > ")
		fmt.Scan(&choice)

		switch choice {
		case 1:
			createTextFile()
		case 2:
			readTextFile()
		case 3:
			editTextFile()
		case 4:
			deleteFile()
		case 5:
			timerightnow()
		case 6:
			fmt.Println("Goodbye!")
			return
		default:
			fmt.Println("Invalid choice. Please select a valid option.")
		}

		fmt.Print("Press Enter to continue...")
		bufio.NewReader(os.Stdin).ReadBytes('\n')
	}
}
