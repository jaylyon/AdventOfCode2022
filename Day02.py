from enum import Enum
from time import process_time

t = process_time()

class PlayType(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Result(Enum):
    Win = 6
    Loss = 0
    Draw = 3

StrategyGuideDictionary = {
    "A": PlayType.Rock,
    "B": PlayType.Paper,
    "C": PlayType.Scissors,
    # assumption made in part 1
    "X": PlayType.Rock,
    "Y": PlayType.Paper,
    "Z": PlayType.Scissors
}

ObjectiveDictionary = {
    "X": Result.Loss,
    "Y": Result.Draw,
    "Z": Result.Win
}

class Play:
    opponentsPlay = object
    myPlay = object
    objective = object
    def __init__(self, text) -> None:
        plays = text.split()
        self.opponentsPlay = StrategyGuideDictionary[plays[0]]
        self.myPlay = StrategyGuideDictionary[plays[1]]
        self.objective = ObjectiveDictionary[plays[1]]
    def score(self):
        s = 0
        if self.opponentsPlay == self.myPlay:
            s += Result.Draw.value
        if self.opponentsPlay == PlayType.Rock:
            if self.myPlay == PlayType.Paper:
                s += Result.Win.value
            if self.myPlay == PlayType.Scissors:
                s += Result.Loss.value
        if self.opponentsPlay == PlayType.Paper:
            if self.myPlay == PlayType.Scissors:
                s += Result.Win.value
            if self.myPlay == PlayType.Rock:
                s += Result.Loss.value
        if self.opponentsPlay == PlayType.Scissors:
            if self.myPlay == PlayType.Rock:
                s += Result.Win.value
            if self.myPlay == PlayType.Paper:
                s += Result.Loss.value
        return s + self.myPlay.value

    def AdjustForPart2(self):
        if self.objective == Result.Draw:
            self.myPlay = self.opponentsPlay
        elif self.opponentsPlay == PlayType.Rock:
            match self.objective:
                case Result.Win:
                    self.myPlay = PlayType.Paper
                case Result.Loss:
                    self.myPlay = PlayType.Scissors
        elif self.opponentsPlay == PlayType.Paper:
            match self.objective:
                case Result.Win:
                    self.myPlay = PlayType.Scissors
                case Result.Loss:
                    self.myPlay = PlayType.Rock
        elif self.opponentsPlay == PlayType.Scissors:
            match self.objective:
                case Result.Win:
                    self.myPlay = PlayType.Rock
                case Result.Loss:
                    self.myPlay = PlayType.Paper


with open("Day02Input.txt") as f:
    guide = f.read().splitlines()

plays = list()

for line in guide:
    plays.append(Play(line))

accumulator = 0
for play in plays:
    accumulator += play.score()

print("Day 2 Part 1 = " + str(accumulator))

accumulator = 0
for play in plays:
    play.AdjustForPart2()
    accumulator += play.score()

print("Day 2 Part 2 = " + str(accumulator))

print("Elapsed Time = " + str(process_time() - t))