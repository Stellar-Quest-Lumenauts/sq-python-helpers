from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='sq-python-helpers',
    version='0.0.1',
    description='Python module that simplifies solving Stellar Quests',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n',
    license='MIT',
    packages=find_packages(),
    author='',
    author_email='',
    keywords=['Stellar', 'Stellar Quest'],
    url='https://github.com/Stellar-Quest-Lumenauts/sq-python-helpers',
    download_url='',
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.',
  ],
)

install_requires = [
    'requests',
    'stellar-sdk'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)