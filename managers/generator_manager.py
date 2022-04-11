# Important to include: pip install image
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
import os
from managers.file_explorer_manager import FileExplorerManager
from managers.excel_manager import ExcelManager
from managers.generated_drawings_manager import GeneratedDrawingsManager
from managers.pdf_manager import PdfManager
from models.drawing_full_name import DrawingFullName

class GeneratorManager:
    '''def resize_img_save_to_temp(path_img: str, path_img_temp: str, baseheight: int):
        from PIL import Image as PImage
        p_img = PImage.open(path_img)
        hpercent = (baseheight / float(p_img.size[1]))
        wsize = int((float(p_img.size[0]) * float(hpercent)))
        p_img = p_img.resize((wsize, baseheight), PImage.ANTIALIAS)
        p_img.save(path_img_temp)'''


    '''def generate(
                template_file="",
                pipe_line_folder="",
                pipe_line="",
                spool="",
                drawing_short="",
                measurements="",
                date="",
                name="",
                path_signature=""
        ):
        lst_measurements = GeneratorManager.measurements_split_into_list(measurements)
        drawing = f"CWT.{pipe_line}-{drawing_short}.00"
        path =""
        try:
            path = GeneratorManager.get_existing_dir_path(pipe_line_folder, f"CWT.{pipe_line}-{drawing_short.split('.')[0]}")
        except Exception as e:
            print(f"Oops. Can't find directory where to save generated files. {e}")
            return False
        dim_check_path = GeneratorManager.into_dim_check_dir(path)
        excel_file = os.path.join(dim_check_path, f"{drawing}_DimChecklist.xlsx")
        pdf_file_name = f"{drawing}_signed.pdf"

        if not GeneratorManager.my_filter(template_file, pipe_line_folder, pipe_line,
                spool, drawing_short, lst_measurements,
                date, name, path_signature): 
            print("Wrong inputs, check yor entries")
            return False

        is_xlsx_generated = GeneratorManager.create_xlsx(
                template_file,
                excel_file,
                pipe_line,
                spool,
                drawing,
                lst_measurements,
                date,
                name,
                path_signature)
        if not is_xlsx_generated:
            return False
        
        GeneratorManager.convert_xlsx_to_pdf(excel_file, pdf_file_name)
        GeneratorManager.add_sign_to_pdf(os.path.join(os.path.dirname(excel_file), pdf_file_name), path_signature, len(lst_measurements))
        GeneratorManager.append_to_txt_file(drawing)
        return True


    def my_filter(
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


    def generate_files(
        template_file="",
        pipe_line_folder="",
        pipe_line="",
        spool="",
        drawing_short="",
        lst_measurements=[],
        date="",
        name="",
        path_signature=""
    )-> Result[bool, str]:
        '''Input is assumed to be valid'''
        
        drawing_full_name = DrawingFullName.from_valid_input(pipe_line, drawing_short)
        drawing = drawing_full_name.name_with_zeros()
        res_path = FileExplorerManager.get_first_dir_path_containing_text(pipe_line_folder, drawing_full_name.dir_project_spool_name())
        if not is_successful(res_path):
            return res_path
        dim_check_path = FileExplorerManager.into_dimcheck_dir(res_path.unwrap())
        excel_file = os.path.join(dim_check_path, drawing_full_name.name_xlsx())
        pdf_file_name = drawing_full_name.name_signed_pdf()

        res_create_xlsx = ExcelManager.create_xlsx(
                template_file,
                excel_file,
                pipe_line,
                spool,
                drawing,
                lst_measurements,
                date,
                name)
        if not is_successful(res_create_xlsx):
            return res_create_xlsx
        
        res_convert = ExcelManager.convert_xlsx_to_pdf(excel_file, pdf_file_name)
        if not is_successful(res_convert):
            return res_convert
        res_add_sig = PdfManager.add_signature_to_pdf(os.path.join(os.path.dirname(excel_file), pdf_file_name), path_signature, len(lst_measurements))
        if not is_successful(res_add_sig):
            return res_add_sig
        gdm=GeneratedDrawingsManager()
        res_update_txt = gdm.update_with(drawing)
        if not is_successful(res_update_txt):
            return res_update_txt
        return Success(True)
