#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#include <cstdio>
#ifdef _WIN32
#define clearcmd "cls"
#else
#define clearcmd "clear"
#endif
using namespace std;

void logo()
{
    std::cout << "                                  ______   " << std::endl;
    std::cout << "                                 |____  |  " << std::endl;
    std::cout << "  _ __ _____   _____ _ __ ___  ___   / /   " << std::endl;
    std::cout << " | '__/ _ \\ \\ / / _ \\ '__/ __|/ _ \\ / /" << std::endl;
    std::cout << " | | |  __/\\ V /  __/ |  \\__ \\  __// /  " << std::endl;
    std::cout << " |_|  \\___| \\_/ \\___|_|  |___/\\___/_/ v2 " << std::endl;
}

void clearscreen()
{
    system(clearcmd);
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

void deletetextfile() {
    std::string filename;

    std::cout << "enter the filename to delete > ";
    getline(std::cin, filename);

    std::cout << "u sure you want to use the ultimate deleter 9000 on said file? \"" << filename << "\"? (use y/n or alr/nah) ";
    std::string response;
    getline(std::cin, response);

    if (response == "Y" || response == "y" || response == "alr") {
        if (std::remove(filename.c_str()) == 0) {
            std::cout << "file nuked succesfully!!!: " << filename << std::endl;
        }
        else {
            std::cout << "unable to nuke the file: " << filename << std::endl;
        }
    }
    else {
        std::cout << "file deletor 9000 stopped" << std::endl;
    }
}

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

#define rtf() readtextfile();
#define ctf() createtextfile();
#define etf() edittextfile();
#define dtf() deletetextfile();

int main(void)
{
	cout << "initialised\n";
    system(clearcmd);
    logo();
    while (true)
    {
        string command;
        cout << " > ";
        getline(cin, command);

        if (command == "text")
        {
            cout << "did you mean \"text create\" or \"text read\" or \"text edit\" or \"text delete\"?" << "\n";
        }
        
        if (command == "text create")
        {
            ctf();
        }

        if (command == "text read")
        {
            rtf();
        }

        if (command == "text edit")
        {
            etf();
        }

        if (command == "text delete")
        {
            dtf();
        }

        if (command == "clear")
        {
            clearscreen();
        }

        if (command == "clock")
        {
            timerightnow();
        }

        if (command == "help")
        {
            cout << "\n";
            cout << "--info--\n";
            cout << "commands are:";
            cout << "text editor stuff: text create ; text read ; text edit; text delete\n";
            cout << "other stuff: clock ; clear ; changelog ; exit\n";
            cout << "\n";
        }

        if (command == "changelog")
        {
            cout << "\n";
            cout << "--Changelog--\n";
            cout << "12/9/23 reverse7 v2 aka toasted cherries\n";
            cout << "1 removed reverseditor and useless droplet thing\n";
            cout << "2 added changelog\n";
            cout << "3 removed admin text before the > sign\n";
            cout << "4 removed the reverse7 on c++ tag on the bottom of the main logo\n";
            cout << "5 removed logo 2 and logo3, making clear alot \"cleaner\" and logo3 was unused" << "\n";
            cout << "6 added thing that asks you if you meant text create or text read\n";
            cout << "6.1 might get removed when i make a new text editor\n";
            cout << "7 renamed clock to \"timerightnow\"" << "\n";
            cout << "8 droplet is coming soon.\n";
            cout << "9 added edit feature to the text editor\n";
            cout << "9.1 ill add a text editor on waterfall\n";
            cout << "10 added the ability to delete files using \"THE ULTIMATE DELETER 9000\"\n";
            cout << "11 reworked help thing\n";
            cout << "---------------------\n";
            cout << "\n";
        }
        
        if (command == "exit")
        {
            break;
        }
    }
}

/*
thank you inferno for helping with the clock.
made by stefan the fork (aka background)
2023 september 12th :P
*/
