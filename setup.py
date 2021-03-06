import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weibo-spider",
    version="0.0.4",
    author="Chen Lei",
    author_email="chillychen1991@gmail.com",
    description="新浪微博爬虫，用python爬取新浪微博数据。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dataabc/weiboSpider",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'lxml',
        'requests',
        'tqdm',
        'absl-py',
    ],
    python_requires='>=3.6',
)
