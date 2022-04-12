from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
from models.drawing_full_name import DrawingFullName

import os

class MyPipeline:
    def process(self,
                template_file,
                pipe_line_folder,
                pipe_line,
                spool,
                drawing_short,
                measurements,
                date,
                name,
                path_signature) -> Result[tuple, str]:
        '''r_template_path = self.__template_process(template_file)
        r_pipe_line_folder = self.__pipe_line_folder_process(pipe_line_folder)
        r_pipe_line = self.__pipe_line_process(pipe_line)
        r_spool = self.__spool_process(spool)
        r_drawing_short = self.__drawing_short_process(drawing_short)
        r_measurements = self.__measurements_process(measurements)
        r_date = self.__date_process(date)
        r_name = self.__name_process(name)
        r_path_signature = self.__path_signature_process(path_signature)'''
        results = (   
            self.__template_process(template_file),
            self.__pipe_line_folder_process(pipe_line_folder),
            self.__pipe_line_process(pipe_line),
            self.__spool_process(spool),
            self.__drawing_short_process(drawing_short),
            self.__measurements_process(measurements),
            self.__date_process(date),
            self.__name_process(name),
            self.__path_signature_process(path_signature)
        )
        fails = [r.failure() for r in results if not is_successful(r)]
        if not fails:
            return Success(tuple(r.unwrap() for r in results))
        else:
            return Failure('\n'.join([f for f in fails]))


    def __template_process(self, s: str)-> Result[str, str]:
        if os.path.exists(s):
            return Success(s)
        return Failure(f"Template Excel file not found in '{s}'")

    
    def __pipe_line_folder_process(self, s: str)-> Result[str,str]:
        if os.path.exists(s):
            return Success(s)
        return Failure(f"Project folder not found in '{s}'")

    
    def __pipe_line_process(self, s: str)-> Result[str,str]:
        return DrawingFullName.is_pipe_line_valid(s)
        
    
    def __spool_process(self, s: str)-> Result[str,str]:
        if len(s)>28:
            return Failure(f"Spool id is too long '{s}'")
        elif len(s)<8:
            return Failure(f"Spool id is too short '{s}'")
        elif "-" not in s:
            return Failure(f"Spool id should contain '-' symbol")
        else:
            return Success(s)


    def __drawing_short_process(self, s: str)-> Result[str, str]:
        return DrawingFullName.is_drawing_short_valid(s)


    def __measurements_process(self, s: str)-> Result[list, str]:
        if not s:
            return Failure(f"Measurements field is empty")
        lst = self.__measurements_split_into_list(s)
        same_len = len(set(map(len,lst)))==1
        len_five = list(map(len,lst))[0]==5
        if not all([same_len, len_five]):
            return Failure(f"Measurements field incorrect input")
        return Success(lst)

    
    def __date_process(self, s: str)-> Result[str, str]:
        from datetime import datetime
        try:
            datetime.strptime(s, "%d.%m.%Y")
            return Success(s)
        except:
            return Failure(f"Error in date - {s}")
        
    
    def __name_process(self, s: str)-> Result[str, str]:
        if len(s.split(" "))<2:
            return Failure(f"Name should consist of first and last names")
        return Success(s)


    def __path_signature_process(self, s: str)-> Result[str, str]:
        if os.path.exists(s):
            return Success(s)
        return Failure(f"Signature .png file not found in '{s}'")


    '''def my_filter(
                template_file="",
                pipe_line_folder="",
                pipe_line="",
                spool="",
                drawing_short="",
                measurements="",
                date="",
                name="",
                signature=""
        )->bool:
        filter_template_file = lambda x: os.path.exists(x)
        filter_pipe_line_folder = lambda x: os.path.exists(x)
        filter_pipe_line = lambda x: len(x)>4 and len(x)<14 and "-" in x
        filter_spool= lambda x: len(x)>9 and len(x)<25 and "-" in x
        filter_drawing_short= lambda x: len(x)>3 and len(x)<10 and "." in str(x)
        filter_measurements= lambda x: len(set(map(len,x)))==1 and list(map(len,x))[0]==5   # 1)same length  2)len==5
        filter_date= lambda x: len(x)>7 and "." in str(x)
        filter_name= lambda x: True
        filter_signature= lambda x: os.path.exists(x)
        filters = [filter_template_file, filter_pipe_line_folder, filter_pipe_line,
                       filter_spool, filter_drawing_short, filter_measurements,
                       filter_date, filter_name, filter_signature]
        values  = [template_file, pipe_line_folder, pipe_line,
                       spool, drawing_short, measurements,
                       date, name, signature]

        filtered = [f(v) for f, v in zip(filters, values)]
        if not all(filtered):
            return False

        return True'''


    def __measurements_split_into_list(self, ms: str)->list:
        lst_meas_0 = ms.strip().split("\n")
        return list(map(lambda x: x.split(","), lst_meas_0))
    
        
