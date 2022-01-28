# wordle_bot
A bot to play wordle

# Quick Start

1. Checkout

```git clone https://github.com/jsearcy1/wordle_bot.git ```

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
