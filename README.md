# wordle_bot
A bot to play wordle

# Quick Start

1. Checkout and install requirements
```
    git clone https://github.com/jsearcy1/wordle_bot.git 
    pip install -r requirements.txt 
```

2. In your package directory
```
python minmax.py
```
3. To play enter the word from the bot into the wordle website
```
Enter:  arise  
Enter Worlde Output String 5x(x/y/g): 
```
4. Enter the the results from website as a 5 character string 
   * x if the character is grey
   * y if the character is yellow
   * g if the character is green
5. Repeat - As you get close to the end the program will print the possible answers left
### Example Game 
```
>> python minmax.py
Enter:  arise  
Enter Worlde Output String 5x(x/y/g): xyxxy
Enter:  volet  
Enter Worlde Output String 5x(x/y/g): xxxyx
Enter:  dumky  
Enter Worlde Output String 5x(x/y/g): xxxgg
['jerky', 'perky']
Enter:  jerky  
Enter Worlde Output String 5x(x/y/g): xgggg 
['perky']
Enter:  perky  
Enter Worlde Output String 5x(x/y/g): ggggg 
['perky']
Win! 5
```
