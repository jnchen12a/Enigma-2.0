import modes
import random

class InvalidCypherText(Exception):
    pass

class CharNotSupported(Exception):
    pass

class GoofyException(Exception):
    pass

class Machine():
    def __init__(self, mode) -> None:
        # 5 wheels     10
        self.wheel0 = [10, 69, 56, 23, 4, 1, 17, 82, 36, 71, 20, 53, 51, 12, 74, 95, 5, 34, 41, 8, 27, 7, 67, 15, 61, 80, 59, 33, 3, 28, 52, 72, 92, 94, 81, 47, 91, 29, 84, 58, 31, 16, 79, 19, 25, 44, 48, 18, 54, 93, 62, 76, 0, 89, 2, 66, 32, 87, 77, 39, 46, 37, 57, 86, 42, 14, 35, 73, 26, 22, 64, 45, 90, 9, 75, 38, 21, 68, 85, 70, 43, 78, 55, 13, 30, 65, 63, 49, 50, 11, 6, 24, 88, 40, 60, 83]
        self.wheel1 = [9, 6, 72, 29, 61, 81, 50, 89, 5, 85, 56, 76, 41, 18, 47, 7, 4, 33, 13, 70, 93, 42, 27, 45, 74, 95, 25, 73, 78, 36, 69, 48, 20, 88, 67, 35, 59, 64, 14, 65, 10, 49, 23, 32, 86, 34, 21, 82, 55, 51, 1, 12, 77, 91, 71, 60, 75, 52, 38, 16, 46, 15, 63, 37, 3, 40, 84, 68, 57, 94, 66, 0, 58, 79, 39, 26, 90, 11, 22, 8, 62, 17, 43, 19, 87, 44, 53, 83, 24, 2, 28, 54, 80, 30, 92, 31]
        self.wheel2 = [38, 48, 67, 10, 43, 58, 65, 39, 12, 76, 85, 57, 34, 95, 11, 51, 70, 73, 7, 89, 64, 80, 68, 74, 46, 31, 93, 1, 3, 82, 44, 79, 14, 84, 2, 21, 63, 72, 33, 13, 50, 54, 49, 22, 81, 47, 83, 24, 6, 36, 19, 8, 59, 9, 77, 37, 55, 40, 41, 26, 0, 87, 35, 28, 20, 27, 88, 66, 90, 25, 53, 71, 45, 5, 30, 18, 61, 56, 62, 29, 78, 42, 69, 86, 92, 23, 17, 91, 15, 75, 16, 4, 52, 60, 94, 32]
        self.wheel3 = [21, 1, 3, 32, 5, 45, 23, 0, 13, 92, 39, 7, 76, 9, 27, 60, 94, 72, 46, 50, 15, 87, 64, 70, 53, 31, 8, 67, 20, 10, 30, 63, 83, 34, 69, 80, 75, 19, 42, 28, 4, 81, 12, 57, 78, 86, 91, 29, 51, 43, 73, 65, 88, 33, 2, 6, 41, 24, 59, 52, 22, 36, 93, 54, 37, 68, 16, 66, 47, 38, 61, 11, 62, 49, 90, 48, 35, 17, 71, 85, 56, 55, 84, 58, 25, 74, 82, 18, 79, 40, 77, 26, 44, 95, 89, 14]
        self.wheel4 = [77, 75, 46, 57, 23, 62, 86, 90, 30, 59, 68, 31, 74, 79, 87, 28, 14, 66, 1, 89, 0, 20, 61, 51, 91, 29, 85, 44, 54, 13, 36, 9, 55, 84, 43, 18, 17, 92, 35, 56, 5, 47, 39, 64, 40, 58, 48, 33, 16, 45, 88, 34, 82, 60, 26, 93, 95, 50, 32, 22, 7, 63, 65, 73, 21, 2, 15, 71, 72, 8, 81, 25, 12, 49, 42, 4, 80, 41, 24, 70, 27, 37, 10, 76, 3, 11, 38, 19, 69, 94, 78, 53, 52, 6, 67, 83]
        self.allWheels = [self.wheel0, self.wheel1, self.wheel2, self.wheel3, self.wheel4]

        if not self._checkWheels():
            raise Exception("Error: wheels have been tampered with! Please double check wheel integrety!") # accounted for

        # wheel positions
        self.firstPos = 0
        self.secondPos = 0
        self.thirdPos = 0

        # set mode
        self.mode = mode

    def encode(self, text) -> str:
        # generate code
        wheelsToUse = random.sample([0, 1, 2, 3, 4], 3)
        firstWheel = self.allWheels[wheelsToUse[0]]
        secondWheel = self.allWheels[wheelsToUse[1]]
        thirdWheel = self.allWheels[wheelsToUse[2]]

        # encode text
        self._resetWheelPositions()
        res = ""
        for c in text:
            encodedLetter = self._passThroughWheelsEncode(c, firstWheel, secondWheel, thirdWheel) # CharNotSupported
            if self.mode == modes.NORMAL:
                encodedLetter = chr(encodedLetter + 32)
            else:
                encodedLetter = self._numToGoofy(encodedLetter) + " " # GoofyException
            self._shiftWheels()
            res += encodedLetter
        
        # prepend code
        code = ""
        for num in wheelsToUse:
            # generate number where number % 5 = num
            if self.mode == modes.NORMAL:
                code += chr(self._encodeWheels(num))
            else:
                word = self._numToGoofy(self._encodeWheels(num) - 32) # GoofyException
                while word[0].lower() == 's':
                    word = self._numToGoofy(self._encodeWheels(num) - 32)
                code += word + ' '
        res = code + res

        if self.mode == modes.GOOFY:
            return res.strip()
        else:
            # normal cyphertext should not end in a whitespace
            if res != res.strip():
                return self.encode(text)
            return res

    def decode(self, text) -> str:
        # get wheels to use
        if self.mode == modes.NORMAL:
            code = text[:3]
            message = text[3:]
            firstWheel = self.allWheels[self._decodeWheels(code[0])]
            secondWheel = self.allWheels[self._decodeWheels(code[1])]
            thirdWheel = self.allWheels[self._decodeWheels(code[2])]
        else:
            message = text.split()
            for word in message:
                if not self._checkGoofy(word):
                    raise InvalidCypherText()
            
            code = message[:3]
            message = message[3:]
            firstWheel = self.allWheels[(self._goofyToNum(code[0], '') + 32) % 5] # InvalidCypherText
            secondWheel = self.allWheels[(self._goofyToNum(code[1], '') + 32) % 5]
            thirdWheel = self.allWheels[(self._goofyToNum(code[2], '') + 32) % 5]

        # decode message
        self._resetWheelPositions()
        res = ""
        if self.mode == modes.NORMAL:
            for c in message:
                encodedLetter = self._passThroughWheelsDecode(c, firstWheel, secondWheel, thirdWheel) # CharNotSupported
                self._shiftWheels()
                res += encodedLetter
        else:
            # message = message.split()
            stinky = ''
            for word in message:
                if word.lower() == "stinky":
                    stinky = word
                    continue
                encodedLetter = self._passThroughWheelsDecode(chr(self._goofyToNum(word, stinky) + 32), firstWheel, secondWheel, thirdWheel)
                self._shiftWheels()
                res += encodedLetter
                stinky = ""

        # return message
        return res

    def _resetWheelPositions(self) -> None:
        self.firstPos = 0
        self.secondPos = 0
        self.thirdPos = 0

    # scrambles char into range [0-95]
    def _passThroughWheelsEncode(self, char, firstWheel, secondWheel, thirdWheel) -> int:
        # convert char to number 0-95
        num = ord(char)
        if num < 32 or num > 127:
            raise CharNotSupported(char)
        
        num -= 32

        # pass number through wheels
        forward = thirdWheel[(secondWheel[(firstWheel[(num + self.firstPos) % 96] + self.secondPos) % 96] + self.thirdPos) % 96]
        backward = firstWheel[(secondWheel[(thirdWheel[(forward + self.thirdPos) % 96] + self.secondPos) % 96] + self.firstPos) % 96]

        return backward
    
    # decodes char into range [0-95]
    def _passThroughWheelsDecode(self, char, firstWheel, secondWheel, thirdWheel) -> int:
        # convert char to number 0-95
        num = ord(char)
        if num < 32 or num > 127:
            raise CharNotSupported(char)
        
        num -= 32

        # pass number through wheels
        forward = (thirdWheel.index((secondWheel.index((firstWheel.index(num) - self.firstPos) % 96) - self.secondPos) % 96) - self.thirdPos) % 96
        backward = (firstWheel.index((secondWheel.index((thirdWheel.index(forward) - self.thirdPos) % 96) - self.secondPos) % 96) - self.firstPos) % 96

        return chr(backward + 32)

    def _shiftWheels(self) -> None:
        self.firstPos += 1
        if self.firstPos > 95:
            self.firstPos = 0
            self.secondPos += 1
            if self.secondPos > 95:
                self.secondPos = 0
                self.thirdPos += 1
                if self.thirdPos > 95:
                    self.thirdPos = 0

    # returns an int from [32, 127]
    def _encodeWheels(self, n) -> int:
        seed = random.randint(7, 24)
        return int(seed * 5) + n
    
    def _decodeWheels(self, s) -> int:
        return ord(s) % 5
    
    def _checkWheels(self) -> bool:
        for wheel in self.allWheels:
            if len(wheel) != 96:
                return False
            for num in range(96):
                if num not in wheel:
                    return False
        
        return True
    
    def _translateWheelNum(self, n):
        return n % 96
    
    # number represented as Goofy, from [0, 95]
    def _numToGoofy(self, n) -> str:
        original = n
        # get firstDigit
        if n > 48:
            firstDigit = True
            n -= 48
        else:
            firstDigit = False

        # get thirdDigit
        thirdDigit = n % 7
        n = n // 7

        # get secondDigit
        secondDigit = n

        ret = ""
        if secondDigit == 0:
            # poo
            ret = "p" + ("o" * (thirdDigit + 2))
        elif secondDigit == 1:
            # poop
            ret = "p" + ("o" * (thirdDigit + 2)) + "p"
        elif secondDigit == 2:
            # pee
            ret = "p" + ("e" * (thirdDigit + 2))
        elif secondDigit == 3:
            # poopoo
            firstSection = random.randint(0, thirdDigit)
            secondSection = thirdDigit - firstSection
            ret = "p" + ("o" * (firstSection + 2)) + "p" + ("o" * (secondSection + 2))
        elif secondDigit == 4:
            # peepee
            firstSection = random.randint(0, thirdDigit)
            secondSection = thirdDigit - firstSection
            ret = "p" + ("e" * (firstSection + 2)) + "p" + ("e" * (secondSection + 2))
        elif secondDigit == 5:
            # poopy
            ret = "p" + ("o" * (thirdDigit + 2)) + "py"
        elif secondDigit == 6: # == 6
            # stinky poo
            ret = "stinky p" + ("o" * (thirdDigit + 2))
        else:
            raise GoofyException()

        if firstDigit:
            return ret.capitalize()
        return ret
    
    # return number encoded as char [0, 95]
    def _goofyToNum(self, phrase, stinky)-> int:
        num = 0
        if stinky != '':
            thirdDigit = len(phrase) - 3
            num = 42 + thirdDigit
            if stinky[0] == "S":
                num += 48
            
            return num
        
        if phrase[-1] == 'y':
            # poopy
            thirdDigit = len(phrase) - 5
            num = 35 + thirdDigit
            if phrase[0] == 'P':
                num += 48
        elif phrase[-1] == 'p':
            # poop
            thirdDigit = len(phrase) - 4
            num = 7 + thirdDigit
            if phrase[0] == 'P':
                num += 48
        elif phrase[-1] == 'o':
            # poo or poopoo
            if phrase[0] == 'P':
                num += 48
            
            countP = phrase.lower().count('p')
            if countP == 1:
                #poo
                thirdDigit = len(phrase) - 3
                num += thirdDigit
            elif countP == 2:
                # poopoo
                thirdDigit = phrase.count('o') - 4
                num += 21 + thirdDigit
            else:
                raise InvalidCypherText()
        elif phrase[-1] == 'e':
            # pee or peepee
            if phrase[0] == 'P':
                num += 48
            
            countP = phrase.lower().count('p')
            if countP == 1:
                # pee
                thirdDigit = len(phrase) - 3
                num += 14 + thirdDigit
            elif countP == 2:
                # peepee
                thirdDigit = phrase.count('e') - 4
                num += 28 + thirdDigit
            else:
                raise InvalidCypherText()
        else:
            raise InvalidCypherText()

        return num
    
    def _checkGoofy(self, phrase) -> bool:
        if phrase.lower() == 'stinky':
            return True
        # first letter should always be p
        if phrase[0].lower() != 'p':
            return False
        if phrase[-1] == 'y':
            # should be poopy
            for c in phrase[1:-2]:
                if c != 'o':
                    return False
        # all characters should be p, o, or e
        else:
            acceptable = set(['p', 'o', 'e'])
            for c in phrase.lower():
                if c not in acceptable:
                    return False
        
        return True
    
    def setMode(self, mode) -> None:
        if mode == modes.GOOFY or mode == modes.NORMAL:
            self.mode = mode