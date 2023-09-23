#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <filesystem>

#ifdef _WIN32
#define clearcmd "cls"
#define makedir "mkdir"
#else
#define clearcmd "clear"
#define makedir "mkdir"
#endif


using namespace std;
namespace fs = std::filesystem;

void startlogo()
{
    std::cout << "                                  ______   " << std::endl;
    std::cout << "  use help to get help(?)        |____  |  " << std::endl;
    std::cout << "  _ __ _____   _____ _ __ ___  ___   / /   " << std::endl;
    std::cout << " | '__/ _ \\ \\ / / _ \\ '__/ __|/ _ \\ / /" << std::endl;
    std::cout << " | | |  __/\\ V /  __/ |  \\__ \\  __// /  " << std::endl;
    std::cout << " |_|  \\___| \\_/ \\___|_|  |___/\\_v3/0/  " << std::endl;
}

void logo()
{
  string attention;
  cout << "!!!!!THE LOGO IS VERY BIG. DONT GET MAD AT ME IF ITS TOO BIG FOR YOUR TERMINAL/SCREEN!!!!!";
  getline(cin,attention);
  std::cout << R"(
                                                                                    
                                                                                
                                                                                
                            %%%%%%%&&&&&&&&&@@@@@@&&&&&&#.                      
                       %%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&@@@@@@%.                  
                    %%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&%                 
                 %%%%%#############%%%%%%%%%%%%%%%%&&&&&&&&&&&&#                
             &&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%#                
           %%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&@@@@#                   
          %%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&#                 
        #########################%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&#                
      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@%              
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&,       %&&&&@@@@@@@@@&              
     ####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,           #&&&&&&&&&&#              
    #######################%%%%%%%%%%%%%%,               #&&&&&#                
   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                                      
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.                                     
   ###%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,                                    
   ########################%%%%%%%%%%%%%%%%%*                                   
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*                                
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&,                               
   %%%%%#%%%#%%%##################%%%%%%%%%%%%%%%%*                             
   #######################%%%%%%%%%%%%%%%%%%%%%%%%%%/                           
   &@@@@@@@@@@@@@@@@@@@@@@&@&&&&&&@@@@@@@@@@@@@@@@@@@@@&((*                     
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%&&&&&&&&&&&&&&&#                  
     %%%%%%############################%%%%%%%%%%%%%%&&&&&&&&&&&&%              
     ####################%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&%%#          
      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&**** 
        %%%%%%                   %%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%*  
         %#                             ###%%%%%%%%%%%&&&&&&&&&&@&&&&&&%%%#     
                                               #&&&&&&&&&&&&&&&&&&&&%.

  )";
  std::cout << R"(

              ████████                                █████                          ██████            ████  ████ 
             ███░░░░███                              ░░███                          ███░░███          ░░███ ░░███ 
 █████ █████░░░    ░███    █████ ███ █████  ██████   ███████    ██████  ████████   ░███ ░░░   ██████   ░███  ░███ 
░░███ ░░███    ██████░    ░░███ ░███░░███  ░░░░░███ ░░░███░    ███░░███░░███░░███ ███████    ░░░░░███  ░███  ░███ 
 ░███  ░███   ░░░░░░███    ░███ ░███ ░███   ███████   ░███    ░███████  ░███ ░░░ ░░░███░      ███████  ░███  ░███ 
 ░░███ ███   ███   ░███    ░░███████████   ███░░███   ░███ ███░███░░░   ░███       ░███      ███░░███  ░███  ░███ 
  ░░█████   ░░████████      ░░████░████   ░░████████  ░░█████ ░░██████  █████      █████    ░░████████ █████ █████
   ░░░░░     ░░░░░░░░        ░░░░ ░░░░     ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░      ░░░░░      ░░░░░░░░ ░░░░░ ░░░░░ 
                                                                                                                  

)";
}


void clearscreen()
{
    system(clearcmd);
}

void info()
{
    logo();
    cout << " <reverse7 v3 aka waterfall>\n";
}

void createtextfile() {
    std::string filename;
    std::string contents;
    std::string line;

    std::cout << "enter file name (should be smth like example.extention) > ";
    getline(std::cin, filename);
    std::cout << "(use EOF as the ending line)\n";

    while (true) {
        getline(std::cin, line);
        if (line == "EOF") {
            break;
        }
        contents += line + "\n";
    }
    std::ofstream myfile(filename);
    if (myfile.is_open()) {
        myfile << contents;
        myfile.close();
        std::cout << "file created successfully!" << std::endl;
    }
    else {
        std::cout << "unable to create the file" << std::endl;
    }
}

void readtextfile() {
    std::string line;
    std::string filename;

    std::cout << "enter filename > ";
    getline(std::cin, filename);

    std::ifstream myfile(filename);

    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            std::cout << line << '\n';
        }
        myfile.close();
    }
    else {
        std::cout << "unable to open file" << std::endl;
    }
}

void edittextfile() {
    std::string filename;
    std::string contents;
    std::string line;

    std::cout << "enter filename > ";
    getline(std::cin, filename);

    std::ifstream myfile(filename);

    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            contents += line + "\n";
        }
        myfile.close();

        std::cout << "editing file > " << filename << std::endl;
        std::cout << "current content: \n" << contents;

        std::cout << "wanna keep the old contents in the file? (use y/n or alr/nah) ";
        std::string response;
        getline(std::cin, response);

        if (response == "Y" || response == "y" || response == "alr") {
            std::string newContent;
            while (true) {
                getline(std::cin, line);
                if (line == "EOF") {
                    break;
                }
                newContent += line + "\n";
            }
            contents += newContent;
        }
        else {
            std::cout << "old file contents will be replaced! anyways enter the new ones here\n";
            contents = "";
            while (true) {
                getline(std::cin, line);
                if (line == "EOF") {
                    break;
                }
                contents += line + "\n";
            }
        }

        std::ofstream outputFile(filename);
        if (outputFile.is_open()) {
            outputFile << contents;
            outputFile.close();
            std::cout << "stuff is saved, exiting editor thing" << std::endl;
        }
        else {
            std::cout << "unable to open the file and write" << std::endl;
        }
    }
    else {
        std::cout << "unable to open file and edit" << std::endl;
    }
}

void deletefile() {
    std::string filename;

    std::cout << "enter the filename to delete > ";
    getline(std::cin, filename);

    std::cout << "u sure you want to use the ultimate deleter 9000 on said file? \"" << filename << "\"? (use y/n or alr/nah) ";
    std::string response;
    getline(std::cin, response);

    if (response == "Y" || response == "y" || response == "alr") {
        if (std::remove(filename.c_str()) == 0) {
            std::cout << "file nuked succesfull!!!: " << filename << std::endl;
        }
        else {
            std::cout << "unable to nuke the file: " << filename << std::endl;
        }
    }
    else {
        std::cout << "file deletor 9000 stopped" << std::endl;
    }
}

#define rtf() readtextfile();
#define ctf() createtextfile();
#define etf() edittextfile();
#define rm() deletefile();

void timerightnow() {
    time_t t = time(NULL);
    tm* timePtr = localtime(&t);
    int seconds = (timePtr->tm_sec);
    int minutes = (timePtr->tm_min);
    int hrs = (timePtr->tm_hour);

    cout << "current time is ";
    cout << hrs << ":" << minutes << endl;

    if (minutes >= 60)
    {
        minutes = 0;
        hrs++;
    }

    if (hrs > 24)
    {
        hrs = 00;
    }
}

void texteditor() {
    string choice;
    cout << "Waterfall text editor" << "\n";
    cout << "1 create\n";
    cout << "2 read\n";
    cout << "3 edit\n";
    cout << " enter choise > ";
    getline(cin, choice);
    if (choice == "1" || choice == "create")
    {
        ctf();
    }

    if (choice == "2" || choice == "read")
    {
        rtf();
    }

    if (choice == "3" || choice == "edit")
    {
        etf();
    }
}

void createdirectory()
{
    string dirname;
    cout << "enter directory name > ";
    getline(cin,dirname);

    if (fs::create_directory(dirname)) {
        std::cout << "directory created " << dirname << std::endl;
    } else {
        std::cout << "failed to create directory " << dirname << std::endl;
    }

}

int main(void)
{
    cout << "initialised\n";
    system(clearcmd);
    startlogo();
    while (true)
    {
        string command;
        cout << " > ";
        getline(cin, command);
      
        if (command == "text")
        {
            texteditor();
        }

        if (command == "clear")
        {
            clearscreen();
        }

        if (command == "clock")
        {
            timerightnow();
        }

        if (command == "remove")
        {
            rm();
        }

        if (command == "logo")
        {
            logo();
        }
        
        if (command == "info")
        {
            info();
        }

        if (command == "makedir")
        {
            createdirectory();
        }

        if (command == "lorem ipsum")
        {
            cout << "\n";
            cout << "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n";
            cout << "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n";
            cout << "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.\n";
            cout << "Duis aute irure dolor in reprehenderit in voluptate velit esse.\n";
            cout << "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.\n";
            cout << "\n";
            // YES THIS IS INDEED INTENTIONAL. ITS HERE BECAUSE I LOVE PUTTING IN EASTEREGGS!!!!!!!
        }

        if (command == "help")
        {
            cout << "\n";
            cout << "--info--\n";
            cout << "commands are:";
            cout << "text\n";
            cout << "other stuff: clock ; clear ; changelog ; exit ; remove ; makedir ; features\n";
            cout << "\n";
        }

        if (command == "features" || command == "feturs")
        {
            cout << "\n";
            cout << "--Quirks-and-Features--\n";
            cout << "1 help thing\n";
            cout << "2 text editor\n";
            cout << "3 THE ULTIMATE DELETOR 9000\n";
            cout << "4 2 logos \n";
            cout << "5 info thigy that is useless\n";
            cout << "6 making files and directories\n";
            cout << "---------------------\n";
            cout << "\n";
        }

        if (command == "changelog" || command == "changelkog")
        {
            cout << "\n";
            cout << "--Changelog--\n";
            cout << "9/23/23 reverse7 v3 waterfall\n";
            cout << "1 added secondary changelog and features commands.\n";
            cout << "2 added text editor menu. open it using \"text\"\n";
            cout << "3 made THE ULTIMATE DELETOR 9000 its own thing\n";
            cout << "4 droplet is cancelled until further notice\n";
            cout << "5 added ability to print out the logo\n";
            cout << "6 added info command that outputs the version and the ascii logo. might change/remove it in a later update\n";
            cout << "7 added makedir command that makes a directory in the parent folder of the executable. (completely useless)\n";
            cout << "8 added features thigy.\n";
            cout << "sorry for the \"small\" update, i just dont have motivation to work on reverse.\n";
            cout << "---------------------\n";
            cout << "\n";
        }

        if (command == "exit")
        {
            break;
            clearscreen();
        } 
    }
}
// just short of 400 lines
