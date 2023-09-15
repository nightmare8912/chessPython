RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class Accessories:
    def printInColor(self, text, color):
        match color.lower():
            case "r":
                print(RED + text + RESET, end = "")
            case "g":
                print(GREEN + text + RESET, end = "")
            case "y":
                print(YELLOW + text + RESET, end = "")
            case "b":
                print(BLUE + text + RESET, end = "")
    def printSL(self, text, sep, end = ""):
        print(text, sep, end)
