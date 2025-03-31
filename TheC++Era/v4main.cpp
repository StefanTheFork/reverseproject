#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <cctype>
#include <vector>
#include <chrono>

#define RED "\033[31m"
#define GREEN "\033[32m"
#define BLUE "\033[34m"
#define RESET "\033[0m"


#ifdef _WIN32
#define clearcmd "cls"
#else
#define clearcmd "clear"
#endif

using namespace std;

std::vector<std::string> commands;
std::vector<std::string> globalCommands;

std::string currentDateTime() {
    auto now = std::chrono::system_clock::now();
    std::time_t now_c = std::chrono::system_clock::to_time_t(now);
    char buffer[80];
    std::strftime(buffer, sizeof(buffer), "%Y%m%d_%H%M%S", std::localtime(&now_c));
    return std::string(buffer);
}


void clearscreen()
{
    system(clearcmd);
}

void createtextfile() {
    std::string filename;
    std::string contents;
    std::string line;

    std::cout << "enter file name > ";
    getline(std::cin, filename);
    std::cout << GREEN << "(use EOF as the ending line)\n" << RESET;

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
        std::cout << GREEN "file created successfully!" << RESET << std::endl;
    }
    else {
        std::cout << RED << "unable to create the file" << RESET << std::endl;
    }
} // heheheheheheehehehehehheheheheheheheheehheheheehehehehehehe funni

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
        std::cout << RED << "unable to open file" << RESET << std::endl;
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

        std::cout << BLUE << "editing file > " << filename << RESET << std::endl;
        std::cout << "current content: \n" << contents;

        std::cout << GREEN << "wanna keep the old contents in the file? (use y/n or alr/nah) " << RESET;
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
            std::cout << RED << "old file contents will be replaced! anyways enter the new ones here\n" << RESET;
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
            std::cout << GREEN << "stuff is saved, exiting editor thing" << RESET << std::endl;
        }
        else {
            std::cout << RED << "unable to open the file and write" << RESET << std::endl;
        }
    }
    else {
        std::cout << RED << "unable to open file and edit" << RESET << std::endl;
    }
}

void deletefile() {
    std::string filename;

    std::cout << "enter the filename to delete > ";
    getline(std::cin, filename);

    std::cout << RED "u sure you want to use the ultimate deleter 9000 on said file? \"" << filename << "\"? (use y/n or alr/nah) " << "\n" << RESET;
    cout << "> ";
    std::string response;
    getline(std::cin, response);

    if (response == "Y" || response == "y" || response == "alr") {
        if (std::remove(filename.c_str()) == 0) {
            std::cout << RED "file nuked succesfull!!!: " << filename << RESET << std::endl;
        }
        else {
            std::cout << RED "unable to nuke the file: " << filename << RESET << std::endl;
        }
    }
    else {
        std::cout << GREEN "file deletor 9000 stopped" << RESET << std::endl;
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
    cout << hrs << BLUE ":" << RESET << minutes << endl;

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


void readcfg(std::string& username, std::string& password) {
    std::string line;
    std::string filename = "reverse.cfg";
    std::ifstream myfile(filename);

    if (myfile.is_open()) {
        bool anyLinesRead = false;
        while (getline(myfile, line)) { //this basically reads the .cfg file and scans it for USERNAME and PASSWORD
            anyLinesRead = true;
            std::istringstream iss(line);
            std::string cfgcontents;
            if (std::getline(iss, cfgcontents)) {
                if (cfgcontents.find("USERNAME") != std::string::npos) { // this scans for USERNAME
                    username = cfgcontents.substr(cfgcontents.find("=") + 1);
                }
                else if (cfgcontents.find("PASSWORD") != std::string::npos) { // and this for PASSWORD
                    password = cfgcontents.substr(cfgcontents.find("=") + 1);
                }
            }
        }
        if (anyLinesRead) {
            std::cout << GREEN << "CFG file does, indeed exist, and its been read successfully" << RESET << std::endl;
        }
        else {
            std::cout << BLUE << "CFG file does, indeed exist, but uhhh its empty...." << RESET << std::endl;
        }
        myfile.close();
    }
    else {
        std::cout << RED << "CFG file does NOT exist. please use the help menu to create and structure one!" << RESET << std::endl;
    }
}

void bye() {
    int randomChoice = rand() % 6 + 1;
    switch (randomChoice) {
    case 1:
        std::cout << GREEN << "goodbye!" << RESET << std::endl;
        break;
    case 2:
        std::cout << BLUE << "goodbye!" << RESET << std::endl;
        break;
    case 3:
        std::cout << RED << "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE" << RESET << std::endl;
        break;
    case 4:
        std::cout << GREEN << "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE" << RESET << std::endl;
        break;
    case 5:
        std::cout << BLUE << "cya!" << RESET << std::endl;
        break;
    case 6:
        std::cout << GREEN << "cya!" << RESET << std::endl;
        break;
    }
}

void actualloggingofcommands(const std::vector<std::string>& commands) 
{
    std::string fileName = "reverse_" + currentDateTime() + ".log";
    std::ofstream logFile(fileName);
    if (!logFile.is_open()) {
        std::cerr << "error opening log file" << std::endl;
        return;
    }
    for (const auto& command : commands) {
        logFile << command << std::endl;
    }
    logFile.close();
    std::cout << "log has been written to " << fileName << std::endl;
}



void startlogo()
{
    std::cout << "                                  ______   " << std::endl;
    std::cout << "  use help to get help(?)        |____  |  " << std::endl;
    std::cout << "  _ __ _____   _____ _ __ ___  ___   / /   " << std::endl;
    std::cout << " | '__/ _ \\ \\ / / _ \\ '__/ __|/ _ \\ / /" << std::endl;
    std::cout << " | | |  __/\\ V /  __/ |  \\__ \\  __// /  " << std::endl;
    std::cout << " |_|  \\___| \\_/ \\___|_|  |___/\\_v4/0/  " << std::endl;
}

void PASS()
{
    string foo = "pass";
    if (foo == "pass")
    {
        cout << foo << endl;
    }
    else
    {
        cout << "no pass :(";
    }
}

int main(void) // shell/kernel/ui/TUI/everythingthatisntafunctionthatispredefinedupthere starts HERE.
{
    cout << GREEN "initialised\n" << RESET;
    system(clearcmd);
    startlogo();
    string username, password;
    readcfg(username, password); 
    while (true)
    {
        string command;
        cout << "> ";
        getline(cin, command);
        commands.push_back(command);

        if (command == "cache")
        {
            for (const auto& command : commands) {
                cout << command << std::endl;
            }
        }

        if (command == "example")
        {
            PASS();
        }

        if (command == "text")
        {
            texteditor();
        }

        if (command == "whoami" || command == "whoamiandwhyamihere")
        {
            readcfg(username, password);
            cout << "username is: " << username << endl;
            cout << "password is: " << password << endl;
            cout << GREEN << "pass\n" << RESET;
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

        if (command == "text create")
        {
            ctf();
        }

        if (command == "text read")
        {
            rtf();
        }

        if (command == "restartCFG")
        {
            readcfg(username, password);
        }

        if (command == "lorem ipsum" || command == "colours" || command == "colour test")
        {
            cout << "-------------------------------------colour-test-------------------------------------\n";
            cout << RED << "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n";
            cout << GREEN << "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n";
            cout << BLUE << "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.\n";
            cout << RED << "Duis aute irure dolor in reprehenderit in voluptate velit esse.\n";
            cout << GREEN << "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.\n";
            cout << BLUE << "Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur.\n" << RESET;
            cout << "-------------------------------------------------------------------------------------\n";
        }

        if (command == "help" || command == "hlep")
        {
            cout << "\n";
            cout << "---------------------------help---------------------------\n";
            cout << BLUE << "commands - text ; clock ; clear ; changelog ; restartCFG ; whoami ; cache\n" << RESET;
            cout << BLUE << "use lorem ipsum to test the colours!\n" << RESET;
            cout << RED << "DO THIS OR ELSE THE SYSTEM WILL SHIT BRICKS:\n" << RESET;
            cout << "First, make a file called" << BLUE << " reverse.cfg" << RESET << ", and put \n";
            cout << BLUE "[USER] " << RESET << "as your FIRST line\n";
            cout << GREEN "USERNAME = admin" << RESET << " as your SECOND line.\n";
            cout << GREEN "PASSWORD/TOKEN = <yourpasswordhere>" << RESET << " as your THIRD line,\n";
            cout << BLUE << "if you forget your password, type whoami to get your username and password.\n";
            cout << RESET << "---------------------------------------------------------";
            cout << "\n";
        } // got a giggle out of me fr

        if (command == "changelog" || command == "changelkog")
        {
            cout << "\n";
            cout << "--Changelog--\n";
            cout << "reverse v4 \"carrotcake\" FEBRUARY 3RD 2024 \n";
            cout << "1. removed makedir, big boy logo and useless info thingy\n";
            cout << "2. added a way to see your password and username without opening your .cfg file\n";
            cout << "3. added colours as compensation for the removal of big logo and makedir\n";
            cout << RED << "   testidy test test\n";
            cout << GREEN << "   testidy test test\n";
            cout << BLUE << "   testidy test test\n" << RESET;
            cout << "4. added old text editor shell stuff because the waterfall menu sucks, but ion wanna remove it\n";
            cout << "5. added better help thingy, that explains how the cfg files work and how to make and properly structure one.\n";
            cout << "6. made lorem ipsum have a use. COLOUR TEST.\n";
            cout << "7. added 3 exit things, fully controlled by rng\n";
            cout << "8. added logging of commands entered by the user" << endl;
            cout << "8.1 upon exit they are outputted to a reverse<TIMESTAMP>.log file" << endl;
            cout << "9. added cache command, that works with the log command to contain the inputted commands" << endl;
            cout << "10. added pass function, that is meant as a placeholder command, for your own mods " << endl;
            cout << "11. removed features thing" << endl;
            cout << "12. changed the release text from \"DAY/MONTH/YEAR\" to \"MONTH DAY YEAR\" "<< endl;
            cout << "12.1. you can see what i mean on top of the changelog" << endl;
            cout << "---------------------\n";
            cout << "\n";
        }

        if (command == "exit")
        {
            bye();
            actualloggingofcommands(commands);
            break;
        }
    }
}
#if you are reading this, hello, im probably going to release RRv1f eventually - mach luv, bakagrand
