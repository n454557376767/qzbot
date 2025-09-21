import importlib
import inspect
from pathlib import Path
from typing import Dict, TypeVar

T = TypeVar('T')
__all__: list[str] = []

# 自动发现模块
package_dir = Path(__file__).parent
modules = [
    f.stem for f in package_dir.glob('*.py') 
    if f.is_file() and not f.name.startswith('_')
]

# 动态导入并收集公共API
for module_name in modules:
    module = importlib.import_module(f'.{module_name}', __package__)
    
    # 收集模块中定义的公共对象（非下划线开头）
    for name, obj in inspect.getmembers(module):
        if not name.startswith('_') and inspect.isclass(obj) or inspect.isfunction(obj):
            globals()[name] = obj
            __all__.append(name)