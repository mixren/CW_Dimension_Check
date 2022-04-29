from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
import os

class FileExplorerManager:
    def get_first_dir_path_containing_text(path: str, dir: str)-> Result[str, str]:
        dir_path = os.path.join(path, dir)
        if not os.path.exists(dir_path):
            dir_name = FileExplorerManager.find_similar_name_dir(path, dir)
            return dir_name.map(lambda d: os.path.join(path, d))
        return Success(dir_path)

    def find_similar_name_dir(path: str, dir: str)-> Result[str, str]:
        try:
            for _, dirs, _ in os.walk(path):
                sim_dir = [d for d in dirs if dir in d][0]
                return Success(sim_dir)
        except:
            return Failure(f"No directory similar to '{dir}'")
    
    def into_dimcheck_dir(path: str):
        '''Get into the 'Dimension Check' folder and create if it doesn't exist'''
        dir = "Dimension Check"
        return FileExplorerManager.into_nested_dir(path, dir)

    def into_nested_dir(path:str, dir:str)->str:
        '''Get into the folder and create if it doesn't exist'''
        dim_check_path = os.path.join(path, dir)
        if not os.path.exists(dim_check_path):
            try:
                os.makedirs(dim_check_path)
            except:
                print(f"Can't recreate existing directory {dim_check_path}")
        return dim_check_path
        
