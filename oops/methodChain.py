class Train:
    def turn_on(self):
        print("The engine has Started")
        return self

    def start(self):
        print('The Train has begun to move')
        return self

    def drive(self):
        print('Locomotive starts to drive')
        return self

    def speed_up(self):
        print('Catch uo the full speed')
        return self


locomotiveBDC = Train()
locomotiveBDC.turn_on().start().start().speed_up()
