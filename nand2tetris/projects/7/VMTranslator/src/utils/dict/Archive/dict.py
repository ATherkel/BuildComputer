import importlib
import importlib.util

class dictLoader:

    def __init__(self, module_path : str) -> None:
        self.module_path = module_path
        self.module = self.load_module()

    def load_module(self):
        spec = importlib.util.spec_from_file_location("module", self.module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def get_dict(self, dict_name):
        if hasattr(self.module, dict_name):
            return getattr(self.module, dict_name)
        else:
            raise AttributeError(f"Dictionary '{dict_name} not found in module '{self.module_path}'")
        
loader = dictLoader("nand2tetris/projects/7/VMTranslator/src/utils/dict/dict_commandType.py")
loader.get_dict("dict_commandType")
