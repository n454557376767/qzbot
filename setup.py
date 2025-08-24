from setuptools import setup, find_packages

setup(
    name="qzbot",  # 库的名称（pip安装时用这个名字）
    version="0.9",  # 版本号（遵循语义化版本）
    author="nm123",  # 作者
    description="No",  # 描述
    packages=find_packages(),  # 自动发现所有包（这里即mylib）
    python_requires=">=3.6"  # 支持的Python版本
)
