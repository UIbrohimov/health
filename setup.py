import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='health',  
     version='0.1',
     scripts=['health'] ,
     author="Ubaydullo Ibrohimov",
     author_email="ubuhobbit@gmail.com",
     description="Computer health checking package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/UIbrohimov/health",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
