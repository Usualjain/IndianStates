from turtle import Turtle


class Statetyper:

    def statename(self, x, y, s_name):

        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x, y)
        state.write(s_name)

    def state_checker(self, ans, lst):

        for state in lst:
            if ans == state:
                return True
        return False
