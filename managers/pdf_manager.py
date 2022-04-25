from fitz import fitz
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
from models.drawing_full_name import DrawingFullName

class PdfManager:

    def add_signature_to_pdf(pdf_path: str, signature_path: str, measurements_count: int)-> Result[bool, str]:
        '''
            Add signature of a pretetermined size to a predetermined places of a pdf document.
        '''
        try:
            pdf = fitz.open(pdf_path)
        except Exception as e:
            return Failure(f"Failed to open PDF file, it might exist and be opened. {str(e)}")

        try:
            img = open(signature_path, "rb").read()
        except Exception as e:
            return Failure(f"Failed to read the signature image. {str(e)}")
        
        page = pdf[0]

        '''The higher w , the more right-sided the image will be positioned 
           The higher h, the less the distance to the bottom of the page
           The higher x, the bigger image gets'''
    
        w_max, h_max = (page.mediabox.width, page.mediabox.height)
        w, h = (w_max*0.88, h_max*0.395)
        w_b , h_b = (w, h_max*0.829)
        x = h_max*0.05
        shift = x*0.49

        '''x       = 30
        shift   = 15
        w, h     = (700, 242)
        w_b, h_b = (w, 507)'''
        
        # Rectangles for signatures
        rects = [fitz.Rect(w, h+(shift*i), w+x, h+(shift*i)+x) for i in range(measurements_count)]
        rects.append(fitz.Rect(w_b, h_b, w_b+x, h_b+x))  # bottom signature

        if not page.is_wrapped:
            page.wrap_contents()
        for r in rects:
            page.insert_image(r, stream=img)

        try:
            pdf.saveIncr()
        except Exception as e:
            return Failure(f"Failed to save PDF with inserted signature. {str(e)}")
        
        return Success(True)


    def count_pages(pdf_path: str)-> Result[int, str]:
        try:
            with fitz.open(pdf_path) as pdf:
                return Success(pdf.page_count)
        except Exception as e:
            return Failure(f"Failed to open PDF file, it might exist and be opened. {str(e)}")


    def split_and_dispatch_pdfs(self, path_root: str, path_pdf: str, lst_names: list[DrawingFullName])-> Result[str, str]:
        '''Extract each page of the scanned PDF, name in accordance with drawing name, merge with the signed dimension checklist'''
        from functools import partial
        import concurrent.futures
        import os

        try:
            pdf = fitz.open(path_pdf)
        except Exception as e:
            pdf.close()
            return Failure(f"Failed to open PDF scan file, it might exist and be opened. {str(e)}")
        
        pdf_page_count = pdf.page_count
        if pdf_page_count != len(lst_names):
            pdf.close()
            return Failure(f"Error. Number of pdf pages ({pdf_page_count}) is different from the number of drawing names in .txt file ({len(lst_names)}). Should be equal.")
        
        print(f"Processing {len(lst_names)} pages...")

        with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:
            lst_idx_names = list(enumerate(lst_names))  #[(0, 'a'), (1, 'b'), (2, 'c')]
            idxs, names = list(zip(*lst_idx_names))     #[(0, 1, 2), ('a', 'b', 'c')]
            partial_func_1 = partial(self.save_scan_page_to_dimcheck_folder, pdf = pdf)
            partial_func_2 = partial(partial_func_1, path_root = path_root)
            results = executor.map(partial_func_2, lst_idx_names)
        
        suc=''
        for r in results:
            if not is_successful(r):
                suc = f"\n{suc}{r.failure()}"
            else:
                drawing = r.unwrap()
                print(f"Completed {drawing.name_with_zeros()}")
                pass

        pdf.close()
        return Success(suc)

        '''list_failures = []
        for i, drawing_full_name in enumerate(lst_names):
            res_save = PdfManager.save_scan_page_to_dimcheck_folder(path_root, drawing_full_name, i, pdf)
            if not is_successful(res_save):
                list_failures.append(res_save.failure())

        pdf.close()
        return Success('\n'.join(list_failures))'''

    # path_root: str, pdf, drawing_full_name: DrawingFullName, n_page: int
    def save_scan_page_to_dimcheck_folder(self, idx_name: tuple, path_root: str, pdf)-> Result[DrawingFullName, str]:
        from managers.file_explorer_manager import FileExplorerManager
        import os

        n_page: int = idx_name[0]
        drawing_full_name: DrawingFullName = idx_name[1]
        print(f"Processing {drawing_full_name.name_with_zeros()}...")

        res_path_project = FileExplorerManager.get_first_dir_path_containing_text(path_root, drawing_full_name.pipe_line)
        if not is_successful(res_path_project):
            return res_path_project
        
        res_path_spool = FileExplorerManager.get_first_dir_path_containing_text(res_path_project.unwrap(), drawing_full_name.dir_project_spool_name())
        if not is_successful(res_path_spool):
            return res_path_spool
        
        path_dimcheck = FileExplorerManager.into_dimcheck_dir(res_path_spool.unwrap())
        
        signed_pdf = os.path.join(path_dimcheck, drawing_full_name.name_signed_pdf())
        destination_pdf = os.path.join(path_dimcheck, drawing_full_name.name_dicheck_with_scan_pdf())
        if os.path.exists(signed_pdf):
            try:
                with fitz.open(signed_pdf) as new_pdf:
                    new_pdf.insert_pdf(pdf, from_page = n_page, to_page = n_page)
                    new_pdf.save(destination_pdf)
            except:
                return Failure(f"Failed to open '{signed_pdf}', it might be opened elsewhere.")
            
        else:
            with fitz.open() as new_pdf:
                new_pdf.insert_pdf(pdf, from_page = n_page, to_page = n_page)
                new_pdf.save(destination_pdf)
        
        return Success(drawing_full_name)



    def split_pdf(path_pdf: str, lst_names: list)-> Result[bool, str]:
        try:
            pdf = fitz.open(path_pdf)
        except Exception as e:
            return Failure(f"Failed to open PDF file, it might exist and be opened. {str(e)}")
        
        if pdf.page_count != len(lst_names):
            return Failure(f"Error. Number of pdf pages ({pdf.page_count}) is different from the number of drawing names in .txt file ({len(lst_names)}). Should be equal.")
        
        for i, name in enumerate(lst_names):
            new_pdf = fitz.open()
            new_pdf.insert_pdf(pdf, from_page = i, to_page = i)
            new_pdf.save(f"{name}.pdf")
        return Success(True)
        