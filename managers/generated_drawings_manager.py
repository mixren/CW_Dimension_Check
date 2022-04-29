import os
from returns.result import Result, Success, Failure
from models.drawing_full_name import DrawingFullName

class GeneratedDrawingsManager:
    M_DIR="repo"
    M_FILE="successfully_generated_drawings.txt"
    PATH_TXT=os.path.join(M_DIR, M_FILE)

    def open_generated_list_txt(self):
        try:
            os.startfile(os.path.abspath(self.PATH_TXT))
        except Exception as e:
            print(f"Can't open a file. {e}")


    def update_with(self, drawing_name)-> Result[bool, str]:
        if not os.path.exists(self.M_DIR):
            os.makedirs(self.M_DIR)
        try:
            f=open(self.PATH_TXT, "a+")
            f.write("\n"+drawing_name)
            f.close()
        except Exception as e:
            return Failure(f"Can't save {drawing_name} info to txt file. {e}")
        return Success(True)


    def get_path_if_exists(self)-> Result[str,bool]:
        return Success(self.PATH_TXT) if os.path.exists(self.PATH_TXT) else Failure(False)


    def get_list_drawing_names(self, file_path, is_reversed:int)-> Result[list[DrawingFullName], str]:
        try:
            with open(file_path, mode='r') as doc:
                s = doc.read()
                list = s.split()
                drawings = [DrawingFullName.from_full_name_string(l) for l in list]
                drawings = drawings[::-1] if is_reversed else drawings
                return Success(drawings)
        except Exception as e:
            return Failure(f"Can't open the .txt file. {e}")


