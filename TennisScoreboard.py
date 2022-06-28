class TennisScoreboard:
    def __init__(self,
                 points = [0, 15, 30, 40],
                 score = [0, 0],
                 gameOverFlag = 0):
        self.__player1 = str(input('Enter player 1 name: '))
        self.__player2 = str(input('Enter player 2 name: '))
        self.__server = int(input('Who is serving (1 or 2)?: '))
        self.__points = points
        self.__score = score
        self.__gameOverFlag = gameOverFlag
        self.__gamePlayer()

    def __gamePlayer(self):
        
        # Print who is serving
        if self.__gameOverFlag == 0 and self.__server == 1:
            print(self.__player1, 'to serve.')
        elif self.__gameOverFlag == 0:
            print(self.__player2, 'to serve.')
        else:
            print('Game over.')
        
        # Game player
        while self.__gameOverFlag == 0:
            pointWinner = int(input('Who won the point (1 or 2)?: '))
            if pointWinner == self.__server:
                if self.__score == [40, 40]:
                    self.__score[0] = 'Adv'
                else:
                    try:
                        self.__score[0] = self.__points[self.__points.index(self.__score[0] + 1)]
                        print('The score is', self.__score)
                    except:
                        self.__gameOverFlag == 1
                        return 'Server holds.'
            else:
                if self.__score == [40, 40]:
                    self.__score[1] = 'Adv'
                    try:
                        self.__score[1] = self.__points[self.__points.index(self.__score[1] + 1)]
                        print('The score is', self.__score)
                    except:
                        self.__gameOverFlag == 1
                        return 'Server broken!'                             
            
    # def __pointWinner(self):
    #     pointWinner = int(input('Who won the point (1 or 2)?'))
    #     return pointWinner
        
    # def __pointIncrement(self):
    #     if self.__score == (40, 40):
    #         pointWinnerScore = 'Adv'
    #     else:
    #         try:
    #             pointWinnerScore = self.__points[self.__points.index(self.__score[self.__pointWinner] + 1)]
    #         except:
    #             pointWinnerScore = 'Game'
    #     return pointWinnerScore