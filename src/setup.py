from setuptools import setup
import setup_translate

pkg = 'Extensions.BabelZapper'
setup(name='enigma2-plugin-extensions-babelzapper',
       version='3.0',
       description='Control your dreambox with only the MUTE button',
       package_dir={pkg: 'BabelZapper'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'babel.png', 'babelzapper.png', 'maintainer.info', 'readme.txt']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
