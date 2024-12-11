from setuptools import setup, find_packages

setup(
    name='KKanjiRecognizer',
    version='0.1',
    packages=find_packages(exclude=['packageTests*']),
    include_package_data=True,
    license='MIT',
    description='Package for recognizing Kanji characters using ResNet',
    long_description=open('README.md').read(),
    install_requires=['numpy',
                      'torch',
                      'torch.nn',
                    'torch.nn.functional',
                    'torchvision.models.resnet',
                    'torchvision',
                    'json',
                    'PIL',
                      ],
    package_data={'KKanjiRecognizerPackage': ['PackageData/model_300_weights.pth', 'PackageData/kanji_mapping.json', "PackageData/threshold.pth"]},
    url='https://github.com/VasyaR/Bachelor_work',
    author='Vasyl Rusyn',
    author_email='vasyarusynb@gmail.com'
)