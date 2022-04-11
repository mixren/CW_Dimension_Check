from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
from managers.pdf_manager import PdfManager
from managers.generated_drawings_manager import GeneratedDrawingsManager

class SplitScanManager:
    def __init__(self) -> None:
        self.gdm = GeneratedDrawingsManager()
        self.pm = PdfManager()
        
    def do(self, path_root, path_pdf, path_drawing_list_txt, is_reversed)-> Result[str, str]:
        res_lst_drawing_names = self.gdm.get_list_drawing_names(path_drawing_list_txt, is_reversed)
        if not is_successful(res_lst_drawing_names):
            return res_lst_drawing_names

        lst_names = res_lst_drawing_names.unwrap()
        res_split = self.pm.split_and_dispatch_pdfs(path_root, path_pdf, lst_names)

        print('Split and dispatch is done.')
        return res_split
        
        # TODO:  
        #  -Check number of pages correspondence
        #  -Split PDF
        #  -Name each PDF accordingly
        #  -Deploy each file into corresponding folders
