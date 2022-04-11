from returns.result import Result, Success, Failure
from returns.pipeline import is_successful

class DrawingFullName:

    def __init__(self, pipe_line, drawing_short) -> None:
        '''
        pipe_line: MP21-77
        drawing_short: 32.01
        '''
        self.pipe_line = pipe_line
        self.drawing_short = drawing_short


    @classmethod
    def from_valid_input(cls, pipe_line: str, drawing_short: str):
        return cls(pipe_line, drawing_short)

    @classmethod
    def from_full_name_string(cls, s: str):
        '''Example: CWT.MP21-77-32.01.00'''
        pl, ds = s.strip().split(".", 1)[1].rsplit(".", 1)[0].rsplit("-", 1)
        return cls(pl, ds)


    @staticmethod
    def is_pipe_line_valid(pipe_line: str)-> Result[str,str]:
        '''Example: MP21-77'''
        s = pipe_line
        if len(s)<7:
            return Failure(f"Project id is too short '{s}'")
        elif len(s)>13:
            return Failure(f"Project id is too long '{s}'")
        elif "-" not in s:
            return Failure("Project id should contain '-' symbol")
        else:
            return Success(s)

    @staticmethod
    def is_drawing_short_valid(drawing_short: str)-> Result[str,str]:
        '''Example: 32.01'''
        s = drawing_short
        if len(s)>10:
            return Failure(f"Drawing id is too long '{s}'")
        elif len(s)<4:
            return Failure(f"Drawing id is too short '{s}'")
        elif "." not in s:
            return Failure(f"Drawing id should contain '.' symbol")
        else:
            return Success(s)


    def name_with_zeros(self):
        '''Example: CWT.MP21-77-32.01.00'''
        return f"CWT.{self.pipe_line}-{self.drawing_short}.00"

    def dir_project_spool_name(self):
        '''Example: CWT.MP21-77-32'''
        return f"CWT.{self.pipe_line}-{self.drawing_short.split('.')[0]}"

    def name_signed_pdf(self):
        '''Example: CWT.MP21-77-32.01.00_signed.pdf'''
        return f"{self.name_with_zeros()}_signed.pdf"

    def name_dicheck_with_scan_pdf(self):
        '''Example: CWT.MP21-77-32.01.00_DimChecklist.pdf'''
        return f"{self.name_with_zeros()}_DimChecklist.pdf"

    def name_xlsx(self):
        '''Example: CWT.MP21-77-32.01.00_DimChecklist.xlsx'''
        return f"{self.name_with_zeros()}_DimChecklist.xlsx"


    
