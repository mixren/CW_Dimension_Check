from managers.generator_manager import GeneratorManager
from windows.my_main_window import *

def test_run():
    GeneratorManager.generate("repo/template_DimChecklist.xlsx",
            "",
            "MP21-77",
            "05-AI-blahblah",
            "38.01",
            "1,L,200,202,-\n2,L,1345,1200,150",
            "15.08.1994",
            "Dima Str",
            "repo/DS signature.png")


if __name__ == '__main__':
    myWindow = MyTkWindow()
    myWindow.initial_setup()
    #test_run()
    myWindow.start()

