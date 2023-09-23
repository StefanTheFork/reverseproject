#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
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
    std::cout << " |_|  \\___| \\_/ \\___|_|  |___/\\___/_/  " << std::endl;
    std::cout << "              reverse7 on c++              " << std::endl;
}

void logo2()
{
    std::cout << "reverse7 on c++" << std::endl;
}

void logo3()
{
    std::cout << "reverseditor" << std::endl;
}

void droplet()
{
    cout << "do it yourself if you dont want to wait.";
}

void clearscreen()
{
    system(clearcmd);
    logo2();
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

void fuckmesideways() {
    time_t t = time(NULL);
    tm* timePtr = localtime(&t);
    //thank you inferno for giving me this power
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

void reverseditor()
{
    logo3();
    createtextfile();
}

#define rtf() readtextfile();
#define ctf() createtextfile();
#define editor() reverseditor();

int main(void)
{
	cout << "initialised\n";
    system(clearcmd);
    logo();
    while (true)
    {
        string command;
        cout << "admin > ";
        getline(cin, command);

        if (command == "text create")   
        {
            ctf();
        }

        if (command == "editor")
        {
            editor();
        }

        if (command == "text read")
        {
            rtf();
        }

        if (command == "clear")
        {
            clearscreen();
        }

        if (command == "clock")
        {
            fuckmesideways();
        }

        if (command == "droplet")
        {
            droplet();
        }

        if (command == "exit")
        {
            break;
        }

        if (command == "help")
        {
            cout << "all commands are: text create;text read;clear;clock;droplet;exit;help;editor\n";
            cout << "for now editor and text create do the same thing. editor will be a small cfg editor ill prob make for reverse v2\n";
        }
    }
	return 0;
}

// thank you inferno for helping with the clock.
// made by yours truly, stefan the fork (aka background)
// 2023 september 6th :P
