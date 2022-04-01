# RPS
### Description
> Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.

### Solution
The first a condition to get a flag is to win 5 times in rock-scissors-paper.

Look at this code in game-redacted.c
```c
 100   │   if (strstr(player_turn, loses[computer_turn])) {
 101   │     puts("You win! Play again?");
 102   │     return true;
 103   │   } else {
 104   │     puts("Seems like you didn't win this time. Play again?");
 105   │     return false;
 106   │   }
 107   │ }
```

The bug is `strstr()`.
If `loses` array contains `player_turn`, then return `1`(true).
Therefore, payload is `rockpaperscissors`.

<details>
<summary>Solution</summary>

```
$ nc saturn.picoctf.net 53296
Welcome challenger to the game of Rock, Paper, Scissors
For anyone that beats me 5 times in a row, I will offer up a flag I found
Are you ready?
Type '1' to play a game
Type '2' to exit the program
1
1


Please make your selection (rock/paper/scissors):
rockpaperscissors
rockpaperscissors
You played: rockpaperscissors
The computer played: paper
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1
1


Please make your selection (rock/paper/scissors):
rockpaperscissors
rockpaperscissors
You played: rockpaperscissors
The computer played: scissors
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1
1


Please make your selection (rock/paper/scissors):
rockpaperscissors
rockpaperscissors
You played: rockpaperscissors
The computer played: paper
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1
1


Please make your selection (rock/paper/scissors):
rockpaperscissors
rockpaperscissors
You played: rockpaperscissors
The computer played: paper
You win! Play again?
Type '1' to play a game
Type '2' to exit the program
1
1


Please make your selection (rock/paper/scissors):
rockpaperscissors
rockpaperscissors
You played: rockpaperscissors
The computer played: scissors
You win! Play again?
Congrats, here's the flag!
picoCTF{50M3_3X7R3M3_1UCK_8525F21D}
Type '1' to play a game
Type '2' to exit the program
2
2
```
</details>

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

