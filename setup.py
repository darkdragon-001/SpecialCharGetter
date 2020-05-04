from setuptools import setup

setup(name='special-char-getter',
      version='0.1',
      description='Easily lookup and copy UTF-8 symbols.',
      url='http://github.com/darkdragon-001/SpecialCharGetter',
      author='Dark Dragon',
      author_email='darkdragon-001@web.de',
      license='MIT',
      install_requires=[
        'setuptools',
        'pyperclip',
      ],
      packages=['scg'],
      #package_dir={'scg': 'src'},
      package_data={'scg': ['chars.ini']},
      #include_package_data=True,
      scripts=[],
      entry_points = {'console_scripts':['scg = scg:main',]},
      zip_safe=False)
