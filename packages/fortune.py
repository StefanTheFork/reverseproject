import random

def tell():
    fortunes = [
        # Funny fortunes
        "A computer once beat me at chess, but it was no match for me at kick boxing.",
        "I haven't slept for ten days, because that would be too long.",
        "The early bird might get the worm, but the second mouse gets the cheese.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don't scientists trust atoms? Because they make up everything.",
        "I'm reading a book about anti-gravity. It's impossible to put down.",
        "The problem with trouble shooting is that trouble shoots back.",
        "A day without sunshine is like, you know, night.",
        "I used to hate facial hair, but then it grew on me.",
        "I'm terrified of elevators, so I'm going to start taking steps to avoid them.",
        "The math teacher called in sick with algebra.",
        "I wondered why the baseball kept getting bigger. Then it hit me.",
        "Broken pencils are pointless.",
        "I'm addicted to brake fluid, but I can stop anytime.",
        "The graveyard is so crowded, people are dying to get in.",
        "I stayed up all night wondering where the sun went. Then it dawned on me.",
        "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
        "I bought some shoes from a drug dealer. I don't know what he laced them with, but I've been tripping all day.",
        "Time flies like an arrow; fruit flies like a banana.",
        "I'm writing a book called 'The History of Glue.' I just can't seem to put it down.",
        
        # Normal fortunes
        "The journey of a thousand miles begins with a single step.",
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Your limitation—it's only your imagination.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Don't wait for opportunity. Create it.",
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Dream bigger. Do bigger.",
        "Don't stop when you're tired. Stop when you're done.",
        "Wake up with determination. Go to bed with satisfaction.",
        "Do something today that your future self will thank you for.",
        "Little things make big days.",
        "It's going to be hard, but hard does not mean impossible.",
        "Don't wish it were easier; wish you were better.",
        "Good things happen to those who hustle.",
        "Champions keep playing until they get it right.",
        "The key to success is to focus on goals, not obstacles."
    ]
    fortune = random.choice(fortunes)
    print(fortune)
